from dataclasses import dataclass


@dataclass(frozen=True)
class TrainingConfig:
    seed: int = 42
    data_dir: str = "data"
    model_dir: str = "models"
    test_size: float = 0.2
    target_column: str = "target"


def default_config() -> TrainingConfig:
    return TrainingConfig()
