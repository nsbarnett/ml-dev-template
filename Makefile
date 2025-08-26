.PHONY: install lint format type-check test

# Install dependencies
install:
	pip install -r requirements.txt

# Run Ruff (linting)
lint:
	ruff check .

# Auto-format code with Black
format:
	black src tests

# Run type checks with mypy
type-check:
	mypy src

# Run tests with pytest
test:
	pytest -q
