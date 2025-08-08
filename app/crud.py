from sqlalchemy.orm import Session
from . import models

def create_produto(db: Session, produto):
    db_produto = models.Produto(**produto.dict())
    db.add(db_produto)
    db.commit()
    db.refresh(db_produto)
    return db_produto

def get_produto(db: Session, produto_id: int):
    return db.query(models.Produto).filter(models.Produto.id == produto_id).first()

def get_produtos(
    db: Session,
    skip: int = 0,
    limit: int = 100,
    categoria: str | None = None,
    nome: str | None = None,
    mais_barato: bool = False
):
    query = db.query(models.Produto)
    
    if categoria:
        query = query.filter(models.Produto.categoria == categoria)
    
    if nome:
        query = query.filter(models.Produto.nome.contains(nome))
    
    if mais_barato:
        query = query.order_by(models.Produto.preco).limit(1)
    
    return query.offset(skip).limit(limit).all()

def update_produto(db: Session, produto_id: int, produto_update):
    db_produto = get_produto(db, produto_id)
    if db_produto:
        for key, value in produto_update.dict().items():
            if value is not None:
                setattr(db_produto, key, value)
        db.commit()
        db.refresh(db_produto)
    return db_produto

def delete_produto(db: Session, produto_id: int):
    db_produto = get_produto(db, produto_id)
    if db_produto:
        db.delete(db_produto)
        db.commit()
        return True
    return False

def vender_produto(db: Session, produto_id: int, quantidade: int):
    produto = get_produto(db, produto_id)
    if produto and produto.quantidade >= quantidade:
        produto.quantidade -= quantidade
        db.commit()
        db.refresh(produto)
        return produto
    return None

def comprar_produto(db: Session, produto_id: int, quantidade: int):
    produto = get_produto(db, produto_id)
    if produto:
        produto.quantidade += quantidade
        db.commit()
        db.refresh(produto)
        return produto
    return None