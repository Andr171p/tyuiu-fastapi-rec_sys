import pickle
from pandas import DataFrame
from sklearn.preprocessing import StandardScaler

from src.config import settings


class StandardScalerService:
    _scaler: StandardScaler | None = None

    @classmethod
    def fit(cls, data: DataFrame) -> None:
        cls._scaler = StandardScaler()
        cls._scaler.fit(data)

    @classmethod
    def standard(cls, data: DataFrame) -> DataFrame:
        return cls._scaler.transform(data)

    @classmethod
    def save(
            cls,
            file_name: str = settings.standard.file_name
    ) -> None:
        with open(
                file=settings.standard.dir_path / file_name,
                mode='wb'
        ) as file:
            pickle.dump(cls._scaler, file)

    @classmethod
    def load(
            cls,
            file_name: str = settings.standard.file_name
    ) -> StandardScaler | None:
        if cls._scaler is None:
            with open(
                    file=settings.standard.dir_path / file_name,
                    mode='rb'
            ) as file:
                cls._scaler = pickle.load(file)
            return cls._scaler
        return
