# Smart Product Recommender

API de recomendação de produtos baseada em algoritmos de IA clássica: **Cadeia de Markov**, **Rede Bayesiana**, **Motor de Decisão** e busca **A\***.

---

## Como funciona

O sistema recebe o perfil de um cliente e seu estado de navegação, e retorna uma lista de produtos recomendados calculada em quatro etapas:

1. **Cadeia de Markov** — prevê o próximo estado de comportamento do cliente (ex: `Visitando` → `Explorando`).
2. **Rede Bayesiana** — calcula a probabilidade de compra com base no histórico, tempo no site e interação com promoções.
3. **Motor de Decisão** — define o produto objetivo da recomendação com base no estado e no produto atual.
4. **Algoritmo A\*** — encontra o melhor caminho no grafo de produtos até o objetivo.

---

## Estrutura do projeto

```
algoritmo-busca/
├── api/
│   ├── dto/            # Request e Response (Pydantic)
│   ├── routers/        # Endpoints FastAPI
│   └── services/       # Lógica de orquestração
├── astar/              # Algoritmo A*
├── bayes/              # Rede Bayesiana
├── data/               # Produtos e grafo de navegação
├── decision/           # Motor de decisão (objetivos e fatores)
├── markov/             # Cadeia de Markov
├── models/             # Entidades: Cliente, Produto, Sessão
├── tests/              # Testes unitários e de API
├── app.py              # Entrypoint FastAPI
├── main.py             # Execução via terminal
├── Dockerfile
└── requirements.txt
```

---

## Pré-requisitos

- Python 3.12+
- pip

---

## Instalação local

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/algoritmo-busca.git
cd algoritmo-busca

# Crie e ative o ambiente virtual
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Linux/Mac

# Instale as dependências
pip install -r requirements.txt
```

---

## Rodando a API

```bash
uvicorn app:app --reload
```

Acesse a documentação interativa em: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## Endpoint

### `POST /recommend`

**Body:**

```json
{
  "historico": 1,
  "tempo_site": 1,
  "clicou_promocao": 1,
  "estado_atual": "Visitando"
}
```

| Campo | Tipo | Valores válidos |
|---|---|---|
| `historico` | int | `0` ou `1` |
| `tempo_site` | int | `0` ou `1` |
| `clicou_promocao` | int | `0` ou `1` |
| `estado_atual` | string | `Visitando`, `Explorando`, `Interessado`, `Comprando`, `Saiu` |

**Resposta:**

```json
{
  "produto_atual": "Notebook Dell",
  "estado_previsto": "Explorando",
  "probabilidade_compra": 0.9,
  "objetivo": "SSD Kingston",
  "recomendacoes": [
    { "nome": "Notebook Dell", "categoria": "Notebook" },
    { "nome": "SSD Kingston",  "categoria": "Hardware" }
  ]
}
```

---

## Rodando via terminal (sem API)

```bash
python main.py
```

---

## Testes

```bash
# Instale o httpx (necessário para o TestClient do FastAPI)
pip install pytest httpx

# Rode todos os testes
pytest tests/ -v
```

Os testes cobrem:

| Arquivo | O que testa |
|---|---|
| `test_bayes.py` | Todas as 8 combinações da Rede Bayesiana |
| `test_markov.py` | Transições de estado e estado inválido |
| `test_decision.py` | Objetivos, fatores e casos de retorno None |
| `test_astar.py` | Caminhos encontrados, heurística e casos extremos |
| `test_api.py` | Endpoint `/recommend`: status, campos, validação e erros |

---

## Docker

```bash
# Build da imagem
docker build -t smart-recommender .

# Rodar o container
docker run -p 8000:8000 smart-recommender
```

A API estará disponível em [http://localhost:8000](http://localhost:8000).

---

## CI com GitHub Actions

O pipeline roda automaticamente a cada push ou pull request para `main`/`master`:

- Configura Python 3.12
- Instala dependências
- Executa `pytest tests/ -v`

Arquivo de configuração: `.github/workflows/ci.yml`
