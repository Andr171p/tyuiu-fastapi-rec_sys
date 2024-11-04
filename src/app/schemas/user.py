from pydantic import BaseModel, ValidationError, ValidationInfo, field_validator


class _UserInfo:
    gender: int
    age: int
    sport: int
    is_foreign: int
    gpa: float
    total_points: int
    bonus_points: int
    is_enrolled: int

    @field_validator('age')
    @classmethod
    def validate_age(cls, v: int) -> int:
        if v <= 0:
            raise ValueError('field age must be >0')
        return v

    @field_validator('gpa')
    @classmethod
    def validate_gpa(cls, v: float) -> float:
        if v < 1 or v > 5:
            raise ValueError('field gpa must be in 1 <= gpa <= 5')
        return v


class _UserExam:
    drawing_exam: int
    math_exam: int
    russian_exam: int
    social_exam: int
    physic_exam: int
    history_exam: int
    composition_architecture_exam: int
    composition_design_exam: int
    informatics_exam: int
    chemistry_exam: int
    composition_exam: int


class _UserEducation:
    education_bac_degree: int
    education_school: int
    education_collage: int


class _UserStudyForm:
    study_form_full: int
    study_form_ext: int
    study_form_full_ext: int


class UserSchema(BaseModel, _UserStudyForm, _UserEducation, _UserExam, _UserInfo):
    pass
