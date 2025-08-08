from pydantic import BaseModel

class ProdutoBase(BaseModel):
    nome: str
    descricao: str
    categoria: str
    preco: float
    quantidade: int

class ProdutoCreate(ProdutoBase):
    pass

class Produto(ProdutoBase):
    id: int

    class Config:
        orm_mode = True

class ProdutoUpdate(BaseModel):
    nome: str | None = None
    descricao: str | None = None
    categoria: str | None = None
    preco: float | None = None
    quantidade: int | None = None

class OperacaoQuantidade(BaseModel):
    quantidade: int