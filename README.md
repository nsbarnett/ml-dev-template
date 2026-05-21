# ML Dev Template

A reusable Python machine learning project template with testing, linting, and CI.  
This repo provides a clean, professional structure for building ML projects that are easy to reproduce, maintain, and share.

---

## 📂 Project Structure

```text
ml-dev-template/
├── .github/workflows/ci.yml     # Continuous Integration workflow
├── .gitignore                   # Files and folders ignored by Git
├── .pre-commit-config.yaml      # Pre-commit hooks for linting/formatting
├── Makefile                     # Automation commands (lint/test/etc.)
├── README.md                    # Project documentation
├── requirements.txt             # Python dependencies
├── src/                         # Main Python source code
├── tests/                       # Unit and integration tests
├── notebooks/                   # Jupyter notebooks for EDA and experiments
├── data/                        # Local datasets (ignored in Git)
└── models/                      # Trained model artifacts (ignored in Git)
```

---

## ⚙️ Setup

### 1. Clone the repository
```bash
git clone https://github.com/nsbarnett/ml-dev-template.git
cd ml-dev-template
```
---

### 2. Create a virtual environment
```bash
python -m venv .venv
```
Activate it:

- Windows:
```bash
.venv\Scripts\activate
```
- Mac/Linux: source
``` bash
.venv/bin/activate
```

---

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

---

## 🧹 Developer Tools
This template includes a modern Python dev setup:
- Ruff → Linting (finds issues, enforces style)
- Black → Code formatting (auto-formats code consistently)
- Mypy → Type checking (ensures variables match expected types)
- Pytest → Testing framework (for unit/integration tests)

Run checks manually:
```bash
ruff check .
black --check .
mypy src/
pytest
```

---

## 🧪 Testing
Place all tests inside the tests/ folder.
Run tests with:
```bash
pytest
```

---

## 🔄 Continuous Integration (CI)
This repo is set up to work with GitHub Actions (add .github/workflows/ci.yml).
Every push and pull request will automatically:
- Lint and format check
- Type check
- Run all tests

---

## 🚀 How to Use This Template
Clone or fork this repo.
- Rename ml-dev-template to your project name.
- Add your data and code inside src/ and notebooks/.
- Train and save models into models/ (ignored by git).
- Update this README with project-specific details.
- Copy `.env.example` to `.env` for local configuration values.
- Choose and add a project-specific `LICENSE` before publishing derived work.

---

## 📌 Notes
- data/ and models/ are gitignored so large files don’t clutter the repo.
- `.env` files are ignored; commit only safe examples such as `.env.example`.
- For reproducibility, update requirements.txt whenever you add a new package:
```bash
pip freeze > requirements.txt
```

---

## 📄 License

This repository is provided as a **template**.  
When you use this template to start your own project, you are free to apply **any license you choose** (MIT, Apache 2.0, GPL, proprietary, etc.).  

⚠️ Note: This template itself does not enforce a license on your derived project.  
Please make sure to add your own `LICENSE` file in your project repository.
