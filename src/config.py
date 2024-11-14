from pathlib import Path
from pydantic_settings import BaseSettings


BASE_DIR: Path = Path(__file__).resolve().parent.parent


class DataSettings(BaseSettings):
    x_train_path: Path = BASE_DIR / "data" / "x_train.csv"
    x_test_path: Path = BASE_DIR / "data" / "x_test.csv"
    y_train_path: Path = BASE_DIR / "data" / "y_train.csv"
    y_test_path: Path = BASE_DIR / "data" / "y_test.csv"


class StandardScalerSettings(BaseSettings):
    dir_path: Path = BASE_DIR / "models"
    file_name: str = "standard_scaler.pkl"


class AppSettings(BaseSettings):
    app_name: str = "Rec-sys API"
    app_v: str = "0.0.1"


class Settings(BaseSettings):
    app: AppSettings = AppSettings()
    data: DataSettings = DataSettings()
    standard: StandardScalerSettings = StandardScalerSettings()


settings = Settings()
