from typing import List
from pydantic import BaseModel, ConfigDict


class ModelRecommendationSchema(BaseModel):
    recommendations: List[str]

    model_config = ConfigDict(from_attributes=True)