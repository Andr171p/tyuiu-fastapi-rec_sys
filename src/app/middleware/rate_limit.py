import time

from fastapi import Request, HTTPException
from starlette.responses import Response
from starlette.types import ASGIApp
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint

from src.config import settings


class RateLimitMiddleware(BaseHTTPMiddleware):
    def __init__(self, app: ASGIApp) -> None:
        super().__init__(app)
        self.rate_limit: int = settings.security.rate_limit
        self.period: int = settings.security.period
        self.requests: dict[str, list] = {}

    async def dispatch(
            self,
            request: Request,
            call_next: RequestResponseEndpoint
    ) -> Response:
        client_ip = request.client.host
        timestamp = time.time()
        if client_ip not in self.requests:
            self.requests[client_ip] = []
        self.requests[client_ip] = [
            t
            for t in self.requests[client_ip]
            if t > timestamp - self.period
        ]
        if len(self.requests[client_ip]) >= self.rate_limit:
            raise HTTPException(
                status_code=429,
                detail="Rate limit exceed"
            )
        self.requests[client_ip].append(timestamp)
        response = await call_next(request)
        return response
