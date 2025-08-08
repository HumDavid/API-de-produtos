# API de Catálogo de Produtos

API CRUD para gerenciamento de produtos usando FastAPI seguindo padrão MVC (Python 3.10+).

### Para executar siga os passos:
1. Crie o ambiente virtual
2. instale as dependências com: `pip install -r requirements.txt`
3. Execute com: `fastapi dev app/main.py`
4. Acesse a documentação interativa: http://localhost:8000/docs

### Funcionalidades
- Inserir Produtos
- Deletar Produtos
- Atualizar Produtos
- Retornar produtos
- Filtro para retornar o produto mais barato
- Filtro para retornar os produtos de uma certa categoria
- Filtro por nome
- Rota para venda (diminui a quantidade de um produto)
- Rota para compra (quantidade de produtos comprados no body)

Padrão MVC implementado:
- **Model**: Representação dos dados (models.py)
- **View**: Camada de apresentação (routers)
- **Controller**: Lógica de negócios (crud.py)

## Rotas

### 1. CRUD Produtos
- Criar produto: POST: `/products/` (Parâmetros: JSON com todos os campos obrigatórios)
- Listar produtos: GET: `/products/` (Parâmetros: `?categoria=`, `?nome=`, `?mais_barato=true`)
- Obter produto específico: GET: `/products/{id}` (Parâmetro: ID)
- Atualizar produto: PUT: `/products/{id}` (Parâmetros: JSON com nenhum campo obrigatório)
- Excluir produto: DELETE: `/products/{id}` (Parâmetro: ID)

### 2. Operações de Estoque
- Vender produto: POST: `/products/{id}/sell` (Body: `{"quantidade": X}`)
- Comprar produto: POST: `/products/{id}/buy` (Body: `{"quantidade": X}`)

\* Campos do produto: `nome`, `descricao`, `categoria`, `preco`, `quantidade`
