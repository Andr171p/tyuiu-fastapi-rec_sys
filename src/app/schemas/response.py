from pydantic import BaseModel, ConfigDict

from typing import Literal, List


class UserResponseSchema:
    status: Literal['ok'] = 'ok'
    data: List[str]
