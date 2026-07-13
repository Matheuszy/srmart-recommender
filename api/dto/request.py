from pydantic import BaseModel


class ClienteRequest(BaseModel):

    historico: int

    tempo_site: int

    clicou_promocao: int

    estado_atual: str