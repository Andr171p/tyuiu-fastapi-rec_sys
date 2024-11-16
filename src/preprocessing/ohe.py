import pickle
import pandas as pd
from sklearn.preprocessing import OneHotEncoder

from src.config import settings


class OHE:
    _ohe: OneHotEncoder | None = None

    @classmethod
    def fit(
            cls,
            data: pd.DataFrame,
            columns: list[str] = settings.preprocessing.columns
    ) -> None:
        cls._ohe = OneHotEncoder(sparse_output=False)
        cls._ohe.fit(data[columns])

    @classmethod
    def transform(
            cls, data: pd.DataFrame,
            columns: list[str] = settings.preprocessing.columns
    ) -> pd.DataFrame:
        encoded = cls._ohe.transform(data[columns])
        data_ohe = pd.DataFrame(encoded)
        data_ohe.columns = cls._ohe.get_feature_names_out()
        data = data.drop(
            labels=columns,
            axis=1
        )
        df = pd.concat(
            [data, data_ohe],
            sort=False,
            axis=1
        )
        df = df.drop(
            labels=settings.preprocessing.drop,
            axis=1
        )
        return df

    @classmethod
    def save(
            cls,
            file_name: str = settings.encoders.ohe_filename
    ) -> None:
        with open(
            file=settings.encoders.dir_path / file_name,
            mode='wb'
        ) as file:
            pickle.dump(cls._ohe, file)

    @classmethod
    def load(
            cls,
            file_name: str = settings.encoders.ohe_filename
    ) -> OneHotEncoder | None:
        if cls._ohe is None:
            with open(
                file=settings.encoders.dir_path / file_name,
                mode='rb'
            ) as file:
                cls._ohe = pickle.load(file)
            return cls._ohe
        return
