from pandas import DataFrame

from src.app.schemas.user import UserSchema
from src.preprocessing.features import FEATURES


def get_df(data: dict) -> DataFrame:
    return DataFrame(data, index=[0])


def get_user_df(user: UserSchema) -> DataFrame:
    user_dict = {}
    values = user.model_dump().values()
    print(len(FEATURES))
    print(len(values))
    for feature, value in zip(FEATURES, values):
        user_dict[feature] = value
    print(user_dict)
    user_df = get_df(user_dict)
    return user_df
