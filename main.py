from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import contextlib
import logging

from src.config import settings

from src.app.gunicorn.application import Application
from src.app.gunicorn.options import get_app_options
from src.app.middleware.globals import GlobalMiddleware, g
from src.app.routers.rec_sys import rec_sys_router
from src.app.routers.docs import docs_router
from src.app.routers.robots import robots_router

from src.preprocessing.ohe import OHE
from src.preprocessing.scaler import Scaler
from src.ml.model import RecSysModel


logging.basicConfig(
    format=settings.logging.log_format
)


@contextlib.asynccontextmanager
async def lifespan(app: FastAPI) -> None:
    ohe = OHE()
    ohe.load()
    g.set_default(name='ohe', default=ohe)
    scaler = Scaler()
    scaler.load()
    g.set_default(name='scaler', default=scaler)
    model = RecSysModel()
    g.set_default(name='model', default=model)
    logging.info("Fastapi application is startup")
    yield
    del scaler
    del model


app = FastAPI(
    title="Recommendation system for applicants",
    lifespan=lifespan
)

app.include_router(
    router=rec_sys_router,
    prefix='/rec_sys',
    tags=['Recommendation system']
)
app.include_router(
    router=docs_router,
    tags=['Docs']
)
app.include_router(
    router=robots_router,
    tags=['Robots']
)

app.add_middleware(GlobalMiddleware)
origins = ["http://localhost:3000", "http://127.0.0.1:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def main() -> None:
    application = Application(
        application=app,
        options=get_app_options(
            host=settings.app.host,
            port=settings.app.port,
            timeout=settings.app.timeout,
            log_level=settings.logging.log_level,
            workers=settings.app.workers
        )
    )
    application.run()


if __name__ == "__main__":
    main()
