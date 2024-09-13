from pydantic import BaseModel
from omegaconf import OmegaConf


class ClassifierSettings(BaseModel):
    weights_path: str
    detection_threshold: float
    cls_critical_det: dict[int, int]


class AppSettings(BaseModel):
    host: str
    port: int


class LoggerSettings(BaseModel):
    log_level: str
    log_dir: str


class Settings(BaseModel):
    classifier_settings: ClassifierSettings
    app_settings: AppSettings
    logger_settings: LoggerSettings

    @classmethod
    def from_yaml(cls, path: str) -> 'Settings':
        cfg = OmegaConf.to_container(OmegaConf.load(path), resolve=True)
        return cls(**cfg)
