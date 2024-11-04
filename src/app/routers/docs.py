from fastapi import APIRouter
from fastapi.responses import RedirectResponse


docs_router = APIRouter()


@docs_router.get(path='/')
async def docs_redirect() -> RedirectResponse:
    return RedirectResponse(url='/')
