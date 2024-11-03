import numpy as np

from sklearn.metrics.pairwise import cosine_similarity

from typing import Any


class RecSysModel:
    def __init__(self, x: Any) -> None:
        self._x = x

    def fit(self) -> np.ndarray:
        similarity = cosine_similarity(
            X=self._x,
            Y=...
        )
        return similarity
