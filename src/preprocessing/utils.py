import pandas as pd


def load_csv(file_path: str) -> pd.DataFrame:
    df = pd.read_csv(file_path)
    df = df.drop(labels='Unnamed: 0', axis=1)
    return df
