from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from .. import crud, schemas, models
from ..database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.Produto)
def criar_produto(produto: schemas.ProdutoCreate, db: Session = Depends(get_db)):
    return crud.create_produto(db, produto)

@router.get("/{produto_id}", response_model=schemas.Produto)
def ler_produto(produto_id: int, db: Session = Depends(get_db)):
    produto = crud.get_produto(db, produto_id)
    if not produto:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return produto

@router.get("/", response_model=list[schemas.Produto])
def ler_produtos(
    categoria: str | None = Query(None),
    nome: str | None = Query(None),
    mais_barato: bool | None = Query(False),
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    return crud.get_produtos(
        db,
        skip=skip,
        limit=limit,
        categoria=categoria,
        nome=nome,
        mais_barato=mais_barato
    )

@router.put("/{produto_id}", response_model=schemas.Produto)
def atualizar_produto(
    produto_id: int,
    produto_update: schemas.ProdutoUpdate,
    db: Session = Depends(get_db)
):
    produto = crud.update_produto(db, produto_id, produto_update)
    if not produto:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return produto

@router.delete("/{produto_id}")
def deletar_produto(produto_id: int, db: Session = Depends(get_db)):
    if not crud.delete_produto(db, produto_id):
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return {"message": "Produto deletado com sucesso"}

@router.post("/{produto_id}/vender", response_model=schemas.Produto)
def vender_produto(
    produto_id: int,
    operacao: schemas.OperacaoQuantidade,
    db: Session = Depends(get_db)
):
    produto = crud.vender_produto(db, produto_id, operacao.quantidade)
    if not produto:
        raise HTTPException(
            status_code=400,
            detail="Produto não encontrado ou quantidade insuficiente"
        )
    return produto

@router.post("/{produto_id}/comprar", response_model=schemas.Produto)
def comprar_produto(
    produto_id: int,
    operacao: schemas.OperacaoQuantidade,
    db: Session = Depends(get_db)
):
    produto = crud.comprar_produto(db, produto_id, operacao.quantidade)
    if not produto:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return produto