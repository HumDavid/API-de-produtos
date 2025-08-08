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
def create_product(produto: schemas.ProdutoCreate, db: Session = Depends(get_db)):
    return crud.create_produto(db, produto)

@router.get("/{produto_id}", response_model=schemas.Produto)
def read_product(produto_id: int, db: Session = Depends(get_db)):
    produto = crud.get_produto(db, produto_id)
    if not produto:
        raise HTTPException(status_code=404, detail="Product not found")
    return produto

@router.get("/", response_model=list[schemas.Produto])
def read_products(
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
def update_product(
    produto_id: int,
    produto_update: schemas.ProdutoUpdate,
    db: Session = Depends(get_db)
):
    produto = crud.update_produto(db, produto_id, produto_update)
    if not produto:
        raise HTTPException(status_code=404, detail="Product not found")
    return produto

@router.delete("/{produto_id}")
def delete_product(produto_id: int, db: Session = Depends(get_db)):
    if not crud.delete_produto(db, produto_id):
        raise HTTPException(status_code=404, detail="Product not found")
    return {"message": "Product deleted successfully"}

@router.post("/{produto_id}/sell", response_model=schemas.Produto)
def sell_product(
    produto_id: int,
    operacao: schemas.OperacaoQuantidade,
    db: Session = Depends(get_db)
):
    produto = crud.sell_product(db, produto_id, operacao.quantidade)
    if not produto:
        raise HTTPException(
            status_code=400,
            detail="Product not found or insufficient quantity"
        )
    return produto

@router.post("/{produto_id}/buy", response_model=schemas.Produto)
def buy_product(
    produto_id: int,
    operacao: schemas.OperacaoQuantidade,
    db: Session = Depends(get_db)
):
    produto = crud.buy_product(db, produto_id, operacao.quantidade)
    if not produto:
        raise HTTPException(status_code=404, detail="Product not found")
    return produto