from pydantic import BaseModel


class ClienteRequest(BaseModel):

    historico: int
    tempo_site: int
    clicou_promocao: int
    estado_atual: str


class ProdutoResponse(BaseModel):

    nome: str
    categoria: str


class RecommendationResponse(BaseModel):

    produto_atual: str
    estado_previsto: str
    probabilidade_compra: float
    objetivo: str | None
    recomendacoes: list[ProdutoResponse]