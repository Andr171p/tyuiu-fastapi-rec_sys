import numpy as np
import pandas as pd
from typing import Any

from src.app.schemas.user import UserSchema
from src.preprocessing.features import USER_FEATURES


class UserForm:

    def __init__(
            self,
            user: UserSchema,
            features: list[str] = USER_FEATURES
    ) -> None:
        self._user = user
        self._features = features
        self._data: dict[str, Any] = {feature: np.nan for feature in self._features}

    def get(self) -> pd.DataFrame:
        return pd.DataFrame(
            data=self._data,
            index=[0]
        )

    def fill(self) -> None:
        dumped = self._user.model_dump()
        self._data['Пол'] = dumped['gender']
        self._data['Дата рождения'] = dumped['age']
        self._data['Спорт'] = dumped['sport']
        self._data['Иностранное гражданство'] = dumped['foreign']
        self._data['Ср. балл док-та об образовании'] = dumped['gpa']
        self._data['Сумма баллов'] = dumped['total_points']
        self._data['Сумма баллов за индивидуальные достижения'] = dumped['bonus_points']
        for exam in dumped['exams']:
            self._data[exam] = True
        self._data['Полученное образование'] = dumped['education']
        self._data['Форма обучения'] = dumped['study_form']



u = UserSchema(
    gender='М',
    age=18,
    sport='КМС БОКС',
    foreign='Таджикистан',
    gpa=4.7,
    total_points=200,
    bonus_points=0,
    exams=['Математика', 'Русский язык', 'Обществознание'],
    education='Среднее общее образование',
    study_form='Очная'
)
uf = UserForm(u)
uf.fill()
df = uf.get()
print(df)

from src.preprocessing.ohe import OHE

ohe = OHE()
ohe.load()
e = ohe.encode(
    data=df,
    columns=['Полученное образование', 'Форма обучения']
)
e = e.drop('Полученное образование_Высшее образование специалитет', axis=1)
print(e.columns)
print(e.shape)

from src.preprocessing.scaler import Scaler

scaler = Scaler()
scaler.load()
e = e.fillna(0)
e['Пол'] = e['Пол'].apply(lambda x: 0 if x != 'М' else 1)
e['Спорт'] = e['Спорт'].apply(lambda x: 1 if x != 0 else 0)
e['Иностранное гражданство'] = e['Иностранное гражданство'].apply(lambda x: 1 if x != 0 else 0)
print(e.values)
df = scaler.standard(e)
print(df)

from src.ml.model import RecSysModel

model = RecSysModel()
model.predict(df)
rec = model.recommend(top_n=5)
print(rec)