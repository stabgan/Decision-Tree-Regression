# 🌳 Decision Tree Regression

A clean implementation of **Decision Tree Regression** in both Python and R, applied to a position salary dataset to predict compensation based on job level.

---

## 📖 Description

This project demonstrates how a Decision Tree Regressor can model non-linear relationships between job position levels and salaries. The dataset contains 10 job positions (from Business Analyst to CEO) with corresponding salary figures. The model learns the step-wise salary structure and can predict salaries for intermediate levels.

## 🔬 Methodology

1. **Data Loading** — Import the `Position_Salaries.csv` dataset containing position levels (1–10) and corresponding salaries.
2. **Feature Selection** — Use `Level` as the independent variable and `Salary` as the dependent variable.
3. **Model Training** — Fit a `DecisionTreeRegressor` (Python) / `rpart` (R) on the full dataset.
4. **Prediction** — Predict the salary for an unseen level (6.5) to evaluate interpolation behavior.
5. **Visualization** — Plot the decision tree's step-function predictions against the actual data points using a high-resolution grid.

> **Note:** Train/test splitting and feature scaling are intentionally skipped due to the small dataset size (10 samples) and because decision trees are invariant to feature scaling.

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| 🐍 Python 3 | Primary implementation |
| 📊 R | Alternative implementation |
| 📦 scikit-learn | `DecisionTreeRegressor` model |
| 🔢 NumPy | Numerical operations |
| 🐼 pandas | Data loading and manipulation |
| 📈 matplotlib | Python visualization |
| 🎨 ggplot2 | R visualization |
| 🌲 rpart | R decision tree model |

## 📋 Dependencies

### Python

```
numpy
pandas
matplotlib
scikit-learn
```

### R

```
rpart
ggplot2
```

## 🚀 How to Run

### Python

```bash
# Install dependencies
pip install numpy pandas matplotlib scikit-learn

# Run the script
python decision_tree_regression.py
```

### R

```r
# Install packages (first time only)
install.packages("rpart")
install.packages("ggplot2")

# Run the script
source("decision_tree_regression.R")
```

Or from the terminal:

```bash
Rscript decision_tree_regression.R
```

## 📊 Dataset

`Position_Salaries.csv` — 10 rows mapping job titles to levels and salaries:

| Position | Level | Salary |
|----------|-------|--------|
| Business Analyst | 1 | 45,000 |
| Junior Consultant | 2 | 50,000 |
| ... | ... | ... |
| CEO | 10 | 1,000,000 |

## ⚠️ Known Issues

- **Small dataset** — Only 10 data points; the model memorizes rather than generalizes. Not suitable for production use without more data.
- **No train/test split** — The model is evaluated on training data, so reported accuracy is artificially high.
- **Overfitting** — With `minsplit=1` (R) and default settings (Python), the tree perfectly fits every data point, which limits generalization.
- **Non-interactive plot** — The Python `matplotlib` plot blocks execution until the window is closed.

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.
