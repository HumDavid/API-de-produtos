from sqlalchemy import Column, Integer, String, Float
from .database import Base

class Produto(Base):
    __tablename__ = "produtos"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), index=True)
    descricao = Column(String(255))
    categoria = Column(String(50), index=True)
    preco = Column(Float)
    quantidade = Column(Integer)