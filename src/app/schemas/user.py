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

    @field_validator('gender')
    @classmethod
    def validate_gender(cls, v: int) -> int:
        if v not in (0, 1):
            raise ValueError('field gender must be binary')
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
