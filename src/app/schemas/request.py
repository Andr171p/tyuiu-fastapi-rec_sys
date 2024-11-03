from pydantic import BaseModel, ConfigDict

from src.app.schemas.user import UserSchema


class UserRequestSchema(BaseModel):
    top_n: int
    user: UserSchema

    model_config = ConfigDict(from_attributes=True)
