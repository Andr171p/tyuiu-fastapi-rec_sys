from starlette.requests import Request
from starlette.responses import Response
from starlette.middleware.base import BaseHTTPMiddleware

from src.app.logs.json_logger import logger


class LogMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next: callable) -> Response:
        response = await call_next(request)
        logger.info(
            msg="Incoming request",
            extra={
                "request": {"method": request.method, "url": str(request.url)},
                "response": {"status_code": response.status_code, },
            },
        )
        return response