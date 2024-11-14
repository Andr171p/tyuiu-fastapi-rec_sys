from pathlib import Path
from typing import Literal
from pydantic_settings import BaseSettings


BASE_DIR: Path = Path(__file__).resolve().parent.parent

LOG_DEFAULT_FORMAT: str = "[%(asctime)s.%(msecs)03d] %(module)10s:%(lineno)-3d %(levelname)-7s - %(message)s"


class DataSettings(BaseSettings):
    x_train_path: Path = BASE_DIR / "data" / "x_train.csv"
    x_test_path: Path = BASE_DIR / "data" / "x_test.csv"
    y_train_path: Path = BASE_DIR / "data" / "y_train.csv"
    y_test_path: Path = BASE_DIR / "data" / "y_test.csv"


class StandardScalerSettings(BaseSettings):
    dir_path: Path = BASE_DIR / "models"
    file_name: str = "standard_scaler.pkl"


class AppSettings(BaseSettings):
    host: str = "0.0.0.0"
    port: int = 8000
    workers: int = 3
    timeout: int = 900


class LoggingSettings(BaseSettings):
    log_level: Literal[
        'debug',
        'info',
        'warning',
        'error',
        'critical',
    ] = 'info'
    log_format: str = LOG_DEFAULT_FORMAT


class RateLimitSettings(BaseSettings):
    rate_limit: int = 5
    period: int = 1


class Settings(BaseSettings):
    app: AppSettings = AppSettings()
    logging: LoggingSettings = LoggingSettings()
    data: DataSettings = DataSettings()
    standard: StandardScalerSettings = StandardScalerSettings()
    security: RateLimitSettings = RateLimitSettings()


settings = Settings()
