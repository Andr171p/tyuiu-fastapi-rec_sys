import pandas as pd
from pandas import DataFrame


def load_csv(file_path: str) -> DataFrame:
    df = pd.read_csv(file_path)
    df = df.drop(labels='Unnamed: 0', axis=1)
    return df

from src.app.schemas.user import UserSchema
from src.app.services.user_df import get_user_df


user = UserSchema(
    gender=1,
    age=18,
    sport=1,
    is_foreign=0,
    gpa=4.3,
    total_points=230,
    bonus_points=10,
    is_enrolled=1,
    drawing_exam=0,
    math_exam=1,
    russian_exam=1,
    social_exam=0,
    physic_exam=1,
    history_exam=0,
    composition_architecture_exam=0,
    composition_design_exam=0,
    informatics_exam=1,
    chemistry_exam=0,
    composition_exam=0,
    education_bac_degree=0,
    education_school=1,
    education_collage=0,
    study_form_full=1,
    study_form_ext=0,
    study_form_full_ext=0
)
df = get_user_df(user)
print(df.columns)
from src.preprocessing.standard import StandardScalerService

scaler = StandardScalerService()
scaler.load()
scaled = scaler.standard(df)
print(scaled)
from src.ml.model import RecommendSystemModel

model = RecommendSystemModel()
model.predict(x=scaled)
res = model.recommend(top_n=7)
print(res)
print(type(res))

from src.app.schemas.request import UserRequestSchema

rec_user = UserRequestSchema(top_n=5, user=user)
print(rec_user.user)
