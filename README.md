# ML Dev Template

A reusable Python machine learning project template with testing, linting, formatting, type checking, and CI.

This repo is designed to give new ML/AI projects a clean starting point: source code, tests, local configuration examples, ignored data/model artifacts, and automated quality checks.

## Project Structure

```text
ml-dev-template/
|-- .github/workflows/ci.yml  # Continuous Integration workflow
|-- .gitignore                # Files and folders ignored by Git
|-- .pre-commit-config.yaml   # Local pre-commit hooks
|-- configs/                  # Experiment and training configuration examples
|-- data/                     # Local datasets, ignored except .gitkeep
|-- models/                   # Trained model artifacts, ignored except .gitkeep
|-- notebooks/                # Jupyter notebooks for EDA and experiments
|-- src/                      # Main Python source code
|-- tests/                    # Unit and integration tests
|-- Makefile                  # Automation commands
|-- pyproject.toml            # Tool configuration
|-- README.md                 # Project documentation
|-- requirements.txt          # Runtime dependencies
`-- requirements-dev.txt      # Development dependencies
```

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/nsbarnett/ml-dev-template.git
cd ml-dev-template
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it:

```bash
# Windows
.venv\Scripts\activate

# Mac/Linux
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

This template intentionally leaves versions unpinned so new projects install the latest compatible package releases when they start.

## Developer Tools

- Ruff: linting for common Python issues
- Black: consistent code formatting
- Mypy: static type checking
- Pytest: unit and integration testing
- Pre-commit: local checks before commits

Run checks manually:

```bash
ruff check .
black --check src tests
mypy src
pytest
```

Install pre-commit hooks:

```bash
pre-commit install
```

## Configuration

Use `configs/example.yaml` as a starting point for project-level settings such as random seeds, data paths, model output paths, and train/test split values.

Use `.env.example` for local machine settings. Copy it to `.env` and fill in project-specific values.

## Key Starter Files

`src/config.py` defines a small `TrainingConfig` object for common ML settings such as the random seed, data directory, model directory, test split size, and target column. Keeping these values in one place makes experiments easier to repeat and avoids scattering important settings across notebooks and scripts.

`src/train.py` is the starter home for training logic. It currently includes a small helper that builds a run name from the config, but future projects can expand it with functions for loading data, splitting datasets, training models, evaluating metrics, and saving artifacts.

`pyproject.toml` centralizes tool configuration for Black, Ruff, Mypy, and Pytest. This keeps the repository cleaner than having separate config files for each tool and gives new projects one obvious place to adjust formatting, linting, typing, and test settings.

`tests/test_smoke.py` contains lightweight smoke tests that confirm the starter code imports correctly and behaves as expected. These tests are intentionally small; replace or expand them with real project tests as the ML code grows.

## Continuous Integration

GitHub Actions runs on every push and pull request. It checks:

- Ruff linting
- Black formatting
- Pytest tests
- Mypy type checking

## How to Use This Template

- Rename `ml-dev-template` to your project name.
- Add project code under `src/`.
- Add tests under `tests/`.
- Add notebooks under `notebooks/` when useful.
- Keep local datasets in `data/`.
- Save trained model artifacts in `models/`.
- Update this README with project-specific details.
- Choose and add a project-specific `LICENSE` before publishing derived work.

## Reproducibility Notes

This template gives you a good starting structure, but ML reproducibility also depends on project-specific habits:

- Set and document random seeds.
- Keep data preparation steps scripted.
- Store experiment settings in config files.
- Track dataset and model artifact versions when projects become larger.
- Record metrics and training parameters for each experiment.

## License

This repository is provided as a template. When you use it to start your own project, choose the license that fits that project and add a `LICENSE` file before publishing.
