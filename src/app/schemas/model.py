from pydantic import BaseModel, ConfigDict

from typing import List


class ModelRecommendationSchema(BaseModel):
    recommendations: List[str]

    model_config = ConfigDict(from_attributes=True)