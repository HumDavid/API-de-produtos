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

## Rotas Principais

### 1. CRUD Produtos
| Método | Rota                   | Função                         | Parâmetros                     |
|--------|------------------------|--------------------------------|--------------------------------|
| POST   | `/products/`           | Criar produto                  | JSON com todos campos*         |
| GET    | `/products/`           | Listar produtos                | `?categoria=`, `?nome=`, `?mais_barato=true` |
| GET    | `/products/{id}`       | Obter produto específico       | ID no path                     |
| PUT    | `/products/{id}`       | Atualizar produto              | Campos parciais no JSON        |
| DELETE | `/products/{id}`       | Excluir produto                | ID no path                     |

### 2. Operações de Estoque
| Método | Rota                           | Função                     | Body               |
|--------|--------------------------------|----------------------------|--------------------|
| POST   | `/products/{id}/vender`        | Vender produto             | `{"quantidade": X}`|
| POST   | `/products/{id}/comprar`       | Comprar mais unidades      | `{"quantidade": X}`|

\* Campos do produto: `nome`, `descricao`, `categoria`, `preco`, `quantidade`
