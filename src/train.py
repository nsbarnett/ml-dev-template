from src.config import TrainingConfig


def build_run_name(config: TrainingConfig) -> str:
    return f"seed-{config.seed}-test-size-{config.test_size:g}"
