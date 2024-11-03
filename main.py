from fastapi import FastAPI

import contextlib

from src.app.middleware.globals import GlobalMiddleware, g
from src.app.routers.rec_sys import rec_sys_router
from src.preprocessing.standard import StandardScalerService
from src.ml.model import RecommendSystemModel

from loguru import logger


@contextlib.asynccontextmanager
async def lifespan(app: FastAPI) -> None:
    scaler = StandardScalerService()
    scaler.load()
    model = RecommendSystemModel()
    g.set_default(
        name='scaler',
        default=scaler
    )
    g.set_default(
        name='model',
        default=model
    )
    logger.info("Fastapi application is startup")
    yield
    del scaler
    del model


app = FastAPI(
    title="Recommendation system for applicants",
    lifespan=lifespan
)
app.include_router(
    router=rec_sys_router,
    prefix='/rec_sys'
)
app.add_middleware(GlobalMiddleware)
