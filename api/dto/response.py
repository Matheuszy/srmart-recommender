from pydantic import BaseModel


class ProdutoResponse(BaseModel):

    nome: str

    categoria: str


class RecommendationResponse(BaseModel):

    produto_atual: str

    estado_previsto: str

    probabilidade_compra: float

    objetivo: str | None

    recomendacoes: list[ProdutoResponse]