# Decision Tree Regression

Predicting salaries based on position level using a Decision Tree Regressor — implemented in both Python and R.

## What It Does

Trains a decision tree on a small position-salary dataset (10 rows) and visualises the step-function predictions that decision trees produce for continuous targets. Includes a single-point prediction for level 6.5.

## Dataset

`Position_Salaries.csv` — 10 job titles mapped to a numeric level (1–10) and corresponding salary (45 000 – 1 000 000).

## 🛠 Tech Stack

| Tool | Purpose |
|------|---------|
| 🐍 Python 3 | Main implementation |
| 📊 scikit-learn | `DecisionTreeRegressor` |
| 🔢 NumPy | Array operations |
| 📈 Matplotlib | Visualisation |
| 🐼 pandas | Data loading |
| 📗 R | Alternative implementation (`rpart`, `ggplot2`) |

## Getting Started

```bash
# Install dependencies
pip install numpy pandas matplotlib scikit-learn

# Run the Python version
python decision_tree_regression.py

# Run the R version (requires R + rpart + ggplot2)
Rscript decision_tree_regression.R
```

## ⚠️ Known Issues

- The dataset is very small (10 samples), so the model memorises every point — this is intentional for demonstration purposes.
- The R script assumes the CSV is in the working directory; run `Rscript` from the repo root.
