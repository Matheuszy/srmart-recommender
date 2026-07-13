from fastapi import APIRouter, HTTPException

from api.dto.request import ClienteRequest
from api.dto.response import RecommendationResponse
from api.services.recomendation_service import RecommendationService

router = APIRouter()

service = RecommendationService()


@router.post("/recommend", response_model=RecommendationResponse)
def recommend(request: ClienteRequest):

    try:
        return service.executar(
            request.historico,
            request.tempo_site,
            request.clicou_promocao,
            request.estado_atual
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
