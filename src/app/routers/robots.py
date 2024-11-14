from fastapi import APIRouter


robots_router = APIRouter()


@robots_router.get(path='/robots.txt')
async def robots_txt() -> str:
    return "User-agent: *\nDisallow: /"
