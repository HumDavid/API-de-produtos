from fastapi import FastAPI
from app.routers import products_router
from .database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(products_router, prefix="/products")

@app.get("/")
def root():
    return "Bem-vindo à API de Catálogo de Produtos"