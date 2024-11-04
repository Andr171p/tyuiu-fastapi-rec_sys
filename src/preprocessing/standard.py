import pickle

from sklearn.preprocessing import StandardScaler

from pandas import DataFrame

from src.config import STANDARD_SCALER_PATH


class StandardScalerService:
    _scaler: StandardScaler = None

    @classmethod
    def fit(cls, data: DataFrame) -> None:
        cls._scaler = StandardScaler()
        cls._scaler.fit(data)

    @classmethod
    def standard(cls, data: DataFrame) -> DataFrame:
        return cls._scaler.transform(data)

    @classmethod
    def save(cls, file_name: str = 'standard_scaler.pkl') -> None:
        with open(file=fr'{STANDARD_SCALER_PATH}/{file_name}', mode='wb') as file:
            pickle.dump(cls._scaler, file)

    @classmethod
    def load(cls, file_name: str = 'standard_scaler.pkl') -> StandardScaler | None:
        if cls._scaler is None:
            with open(file=fr'{STANDARD_SCALER_PATH}/{file_name}', mode='rb') as file:
                cls._scaler = pickle.load(file)
            return cls._scaler
        return
