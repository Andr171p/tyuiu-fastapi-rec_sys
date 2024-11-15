import numpy as np
from pandas import DataFrame
from sklearn.metrics.pairwise import cosine_similarity

from src.config import settings
from src.preprocessing.utils import load_csv


class RecSysModel:
    _similarity: np.ndarray | None = None

    def __init__(self) -> None:
        self._inputs = load_csv(settings.data.inputs_path)
        self._outputs = load_csv(settings.data.outputs_path)

    def predict(self, x: DataFrame | np.ndarray) -> np.ndarray | None:
        if x.shape != (1, 24):
            x = x.to_numpy().reshape(1, -1)
        self._similarity = cosine_similarity(
            X=x,
            Y=self._inputs
        )
        return self._similarity

    def recommend(self, top_n: int) -> list[str]:
        if self._similarity is not None:
            indices = np.argsort(self._similarity[0])[-top_n-1:-1][::-1]
            recommended = self._outputs.iloc[indices].sum(axis=0)
            return recommended.nlargest(top_n).index.to_list()
