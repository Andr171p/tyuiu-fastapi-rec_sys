import pandas as pd


def load_csv(file_path: str) -> pd.DataFrame:
    df = pd.read_csv(file_path)
    df = df.drop(labels='Unnamed: 0', axis=1)
    return df


def encode_labels(df: pd.DataFrame) -> pd.DataFrame:
    df['Пол'] = df['Пол'].apply(
        lambda x: 0 if x != 'М' else 1
    )
    df['Спорт'] = df['Спорт'].apply(
        lambda x: 1 if x != 0 else 0
    )
    df['Иностранное гражданство'] = df['Иностранное гражданство'].apply(
        lambda x: 1 if x != 0 else 0
    )
    return df
