from fastapi import FastAPI

from api.routers.recomendation import router

app = FastAPI(
    title="Smart Product Recommender",
    version="1.0.0"
)

app.include_router(router)