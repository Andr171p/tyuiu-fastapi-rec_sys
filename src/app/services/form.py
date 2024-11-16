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
