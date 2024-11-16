from pathlib import Path
from typing import Literal, List
from pydantic_settings import BaseSettings


BASE_DIR: Path = Path(__file__).resolve().parent.parent

LOG_DEFAULT_FORMAT: str = "[%(asctime)s.%(msecs)03d] %(module)10s:%(lineno)-3d %(levelname)-7s - %(message)s"


class DataSettings(BaseSettings):
    inputs_path: Path = BASE_DIR / "data" / "inputs.csv"
    outputs_path: Path = BASE_DIR / "data" / "outputs.csv"


class PreprocessingSettings(BaseSettings):
    columns: List[str] = ['Полученное образование', 'Форма обучения']


class EncodersSettings(BaseSettings):
    dir_path: Path = BASE_DIR / "models"
    ohe_filename: str = "ohe.pkl"
    scaler_filename: str = "scaler.pkl"


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
    preprocessing: PreprocessingSettings = PreprocessingSettings()
    encoders: EncodersSettings = EncodersSettings()
    security: RateLimitSettings = RateLimitSettings()


settings = Settings()
