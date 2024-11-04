from pydantic import BaseModel, ConfigDict

from typing import Literal

from src.app.schemas.model import ModelRecommendationSchema


class UserResponseSchema(BaseModel):
    status: Literal['ok'] = 'ok'
    data: ModelRecommendationSchema
