# API de Catálogo de Produtos

API CRUD para gerenciamento de produtos usando FastAPI seguindo padrão MVC.
Código suportado para versões 3.10+ do Python.

### Como Executar
1. Crie o ambiente virtual e instale as dependências
2. Execute com: `fastapi dev app/main.py`
3. Acesse a documentação interativa em: http://localhost:8000/docs

### Funcionalidades
- CRUD completo de produtos
- Filtros por categoria, nome e produto mais barato
- Operações de venda (diminuir estoque)
- Operações de compra (aumentar estoque)
- Validação de dados com Pydantic
- Banco de dados SQLite com SQLAlchemy
- Documentação automática (Swagger UI)

Este projeto segue estritamente o padrão MVC:
- **Model**: Representação dos dados (models.py)
- **View**: Camada de apresentação (routers)
- **Controller**: Lógica de negócios (crud.py)

### Rotas
- Inserir Produtos
- - POST: `/products/`
    (possui os seguintes parâmetros:
    nome: str,
    descricao: str,
    categoria: str,
    preco: float,
    quantidade: int)
- Deletar Produtos
- - DELETE: `/products/{produto_id}`
- Atualizar Produtos
- - PUT: `/products/{produto_id}`
- Retornar produtos
- - GET: `/products/`
    (possui os seguintes parâmetros opcionais:
    categoria: str,
    nome: str,
    mais_barato: bool)
- - GET: `/products/{produto_id}`
- Rota para venda
- - POST: `/products/{produto_id}/sell`
- Rota para compra
- - POST: `/products/{produto_id}/buy`