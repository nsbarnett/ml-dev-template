from src.config import default_config
from src.train import build_run_name


def test_default_training_config_has_reproducible_seed() -> None:
    config = default_config()

    assert config.seed == 42


def test_build_run_name_includes_key_settings() -> None:
    config = default_config()

    assert build_run_name(config) == "seed-42-test-size-0.2"
