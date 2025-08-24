# ML Dev Template

A reusable Python machine learning project template with testing, linting, and CI.  
This repo provides a clean, professional structure for building ML projects that are easy to reproduce, maintain, and share.

---

## 📂 Project Structure
ml-dev-template/
├─ src/ # Main Python source code
├─ tests/ # Unit and integration tests
├─ notebooks/ # Jupyter notebooks for EDA and experiments
├─ data/ # Local datasets (ignored in git)
├─ models/ # Trained model artifacts (ignored in git)
└─ README.md # Project documentation

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

- Windows: .venv\Scripts\activate
- Mac/Linux: source .venv/bin/activate

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

---

## 📌 Notes
- data/ and models/ are gitignored so large files don’t clutter the repo.
- For reproducibility, update requirements.txt whenever you add a new package:
```bash
pip freeze > requirements.txt
```

---

## 📄 License
This project is licensed under the MIT License (or whichever you prefer).
