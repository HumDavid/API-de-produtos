# API de Catálogo de Produtos

API CRUD para gerenciamento de produtos usando FastAPI seguindo padrão MVC.
Código suportado para versões 3.10+ do Python.

### Como Executar
1. Crie o ambiente virtual e instale as dependências
2. Execute com: `fastapi dev app/main.py`
3. Acesse a documentação interativa em: http://localhost:8000/docs

### Funcionalidades Implementadas
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