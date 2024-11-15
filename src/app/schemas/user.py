from typing import List, Literal
from pydantic import BaseModel, field_validator


class UserSchema(BaseModel):
    gender: Literal['М', 'Ж']
    age: int
    sport: str
    foreign: str
    gpa: float
    total_points: int
    bonus_points: int
    exams: List[str]
    education: str
    study_form: str

    @field_validator("age")
    @classmethod
    def validate_age(cls, v: int) -> int:
        if v <= 0:
            raise ValueError("Field `age` must be >0")
        return v

    @field_validator("gpa")
    @classmethod
    def validate_gpa(cls, v: float) -> float:
        if v < 3 or v > 5:
            raise ValueError("Field `gpa` must be in range [3;5]")
        return v

    @field_validator("total_points")
    @classmethod
    def validate_total_points(cls, v: int) -> int:
        if v < 0 or v > 310:
            raise ValueError("Field `total_points` must be in range [0;310]")
        return v

    @field_validator("bonus_points")
    @classmethod
    def validate_bonus_points(cls, v: int) -> int:
        if v < 0 or v > 10:
            raise ValueError("Field `bonus_points` must be in range [0;10]")
        return v
