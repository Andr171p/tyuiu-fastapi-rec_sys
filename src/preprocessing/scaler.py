import pickle
import pandas as pd
from sklearn.preprocessing import StandardScaler

from src.config import settings


class Scaler:
    _scaler: StandardScaler | None = None

    @classmethod
    def fit(cls, data: pd.DataFrame) -> None:
        cls._scaler = StandardScaler()
        cls._scaler.fit(data)

    @classmethod
    def transform(cls, data: pd.DataFrame) -> pd.DataFrame:
        return cls._scaler.transform(data)

    @classmethod
    def save(
            cls,
            file_name: str = settings.encoders.scaler_filename
    ) -> None:
        with open(
                file=settings.encoders.dir_path / file_name,
                mode='wb'
        ) as file:
            pickle.dump(cls._scaler, file)

    @classmethod
    def load(
            cls,
            file_name: str = settings.encoders.scaler_filename
    ) -> StandardScaler | None:
        if cls._scaler is None:
            with open(
                    file=settings.encoders.dir_path / file_name,
                    mode='rb'
            ) as file:
                cls._scaler = pickle.load(file)
            return cls._scaler
        return
