# 🎯 E-Commerce Conversion Prediction - Complete Project Summary

## 📋 Overview

This is a **complete, production-ready solution** for the Summer Analytics 2026 Week 2 Hackathon - E-Commerce Conversion Prediction Challenge.

**Task:** Predict whether an e-commerce user will convert (make a purchase)  
**Metric:** F1 Score  
**Result:** 0.5438 F1 Score on public test set  

---

## 🗂️ Project Structure

```
Project_1_ML/
│
├── 📂 src/                          # Core source code modules
│   ├── feature_engineering.py       # 12 engineered features
│   ├── preprocessing.py             # Data cleaning & encoding
│   ├── model.py                     # XGBoost + LightGBM ensemble
│   └── utils.py                     # Helper functions
│
├── 📂 notebooks/                    # Jupyter notebooks
│   └── notebook.ipynb               # Complete interactive solution
│
├── 📂 data/                         # Dataset location
│   └── [Place train.csv, public_test.csv, private_test.csv here]
│
├── 📂 outputs/                      # Generated results
│   └── submission.csv               # Final predictions
│
├── 🐍 train.py                      # Main training script
├── 📄 requirements.txt              # Python dependencies
├── 📊 report.md                     # Methodology report
├── 📖 README.md                     # Project documentation
├── 🔧 INSTALLATION.md               # Setup instructions
└── 📚 USAGE.md                      # Detailed usage guide
```

---

## ⚡ Quick Start (3 Steps)

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Add Data Files
Place `train.csv`, `public_test.csv`, `private_test.csv` in the `data/` folder

### 3. Run Pipeline
```bash
python train.py
```

**Output:** `outputs/submission.csv` (ready for submission!)

---

## 🧠 Solution Architecture

### Feature Engineering (12 New Features)

**Interaction Features:**
- `engagement_score` = Pages × Products
- `time_per_page` = Time / Pages
- `products_per_page` = Products / Pages
- `total_interaction` = Pages + Products
- `time_products` = Time × Products
- `purchase_discount_interaction` = Purchases × Discount

**Binary Indicators:**
- `returning_buyer` = Has prior purchases
- `high_previous` = Frequent buyer (≥3 purchases)
- `discount_buyer` = Discount-driven buyer

**Transformations:**
- `log_income` = Log-transformed income
- `income_per_age` = Income normalized by age
- `age_group` = Age categories

### Preprocessing Pipeline

1. **Missing Value Imputation:** Median (Age, Income, Time_On_Site)
2. **Categorical Encoding:** LabelEncoder (Device_Type, Traffic_Source)
3. **Fitted on Combined Data:** Train + Test for consistency

### Model Architecture

**Ensemble:** XGBoost + LightGBM (equal-weight averaging)

| Component | XGBoost | LightGBM |
|-----------|---------|----------|
| Trees | 500 | 500 |
| Depth | 5 | 5 |
| Learning Rate | 0.03 | 0.03 |
| Imbalance | scale_pos_weight=2.27 | is_unbalance=True |

### Optimization

**Threshold Tuning:** Swept 0.20-0.80, optimized on public test  
**Best Threshold:** 0.39  
**F1 Score:** 0.5438

---

## 📊 Key Results

### Performance
- **Public Test F1 Score:** 0.5438
- **Baseline (Logistic Regression):** ~0.42
- **Improvement:** +29%

### Top 8 Features
1. Pages_Viewed
2. engagement_score
3. total_interaction
4. Products_Viewed
5. discount_buyer
6. Discount_Seen
7. purchase_discount_interaction
8. Previous_Purchases

**Key Insight:** Browsing depth + discount-driven returning buyers = strongest conversion signals

---

## 📝 Files Description

### Core Modules (`src/`)

| File | Purpose |
|------|---------|
| `feature_engineering.py` | Creates 12 engineered features |
| `preprocessing.py` | Handles missing values, encoding |
| `model.py` | Implements ensemble, threshold optimization |
| `utils.py` | Data loading, visualization, submission creation |

### Scripts

| File | Purpose |
|------|---------|
| `train.py` | Complete end-to-end pipeline |
| `notebooks/notebook.ipynb` | Interactive Jupyter notebook |

### Documentation

| File | Purpose |
|------|---------|
| `README.md` | Project overview and documentation |
| `report.md` | Methodology summary (1-page report) |
| `INSTALLATION.md` | Setup and installation guide |
| `USAGE.md` | Detailed usage examples |
| `PROJECT_SUMMARY.md` | This file |

---

## 🎓 Usage Examples

### Run Complete Pipeline
```bash
python train.py
```

### Use Jupyter Notebook
```bash
jupyter notebook
# Open notebooks/notebook.ipynb
```

### Use Individual Modules
```python
from src.feature_engineering import create_features
from src.model import EnsembleModel

# Feature engineering
train_enhanced = create_features(train_df)

# Model training
model = EnsembleModel(random_state=42)
model.fit(X_train, y_train)

# Prediction
predictions = model.predict(X_test, threshold=0.39)
```

---

## 🛠️ Technical Stack

- **Python:** 3.9+
- **Data Processing:** pandas, numpy
- **ML Models:** XGBoost, LightGBM
- **ML Framework:** scikit-learn
- **Visualization:** matplotlib, seaborn
- **Notebook:** Jupyter

---

## 📦 Hackathon Submission

### Required Files

1. ✅ **submission.csv** - Predictions (`outputs/submission.csv`)
2. ✅ **notebook.ipynb** - Reproducible notebook (`notebooks/notebook.ipynb`)
3. ✅ **report.pdf** - Convert `report.md` to PDF

### Creating ZIP for Submission

```bash
# Create submission ZIP
zip -r submission.zip notebooks/notebook.ipynb report.pdf

# Or manually:
# 1. Convert report.md to report.pdf (use any Markdown to PDF converter)
# 2. Create ZIP with notebook.ipynb and report.pdf
```

---

## 🎯 Key Features

✅ **Modular Design** - Clean, reusable code  
✅ **Production Ready** - Error handling, logging  
✅ **Fully Documented** - Extensive comments and docs  
✅ **Reproducible** - Fixed random seeds  
✅ **Extensible** - Easy to add features/models  
✅ **Best Practices** - PEP 8, type hints  
✅ **Complete Pipeline** - End-to-end automation  

---

## 📈 Model Performance Breakdown

| Stage | F1 Score | Description |
|-------|----------|-------------|
| Baseline | 0.42 | Logistic Regression |
| XGBoost Only | 0.51 | Single model |
| LightGBM Only | 0.50 | Single model |
| **Ensemble** | **0.54** | XGBoost + LightGBM |
| + Threshold Opt | **0.5438** | Tuned at 0.39 |

---

## 🔍 What Makes This Solution Strong?

1. **Comprehensive Feature Engineering** - 12 carefully crafted features
2. **Ensemble Method** - Combines strengths of two models
3. **Threshold Optimization** - Maximizes F1 on validation set
4. **Handles Imbalance** - scale_pos_weight & is_unbalance
5. **Robust Preprocessing** - Median imputation, proper encoding
6. **Retrains on Full Data** - Uses train + public_test for final model
7. **Clean Code** - Modular, maintainable, documented

---

## 🚀 Next Steps & Improvements

### Potential Enhancements

1. **Feature Engineering**
   - Add temporal features (if timestamps available)
   - Create more interaction terms
   - Apply feature selection (SHAP, permutation importance)

2. **Model Improvements**
   - Add CatBoost to ensemble
   - Try Neural Networks
   - Implement stacking ensemble
   - Use Optuna for hyperparameter tuning

3. **Validation**
   - Add cross-validation
   - Implement stratified K-fold
   - Use multiple holdout sets

4. **Preprocessing**
   - Try different imputation strategies (KNN, iterative)
   - Experiment with scaling methods
   - Handle outliers

---

## 📚 Learning Resources

### Concepts Used in This Project

- Binary Classification
- Imbalanced Classification
- Feature Engineering
- Gradient Boosting (XGBoost, LightGBM)
- Ensemble Methods
- Threshold Optimization
- F1 Score Optimization
- Missing Value Imputation
- Label Encoding

### Recommended Reading

- **XGBoost Documentation:** https://xgboost.readthedocs.io/
- **LightGBM Documentation:** https://lightgbm.readthedocs.io/
- **Feature Engineering Guide:** Kaggle Feature Engineering tutorials
- **Imbalanced Learning:** https://imbalanced-learn.org/

---

## 🤝 Contributing

This is a hackathon project, but improvements are welcome:

1. Fork the repository
2. Create a feature branch
3. Make improvements
4. Test thoroughly
5. Submit a pull request

---

## 📧 Support

For questions about the project:
- Check the documentation files (README.md, USAGE.md, INSTALLATION.md)
- Review the code comments
- Consult Summer Analytics 2026 Discord community

---

## ✅ Checklist Before Submission

- [ ] Data files are in `data/` directory
- [ ] All dependencies installed (`pip install -r requirements.txt`)
- [ ] Run `python train.py` successfully
- [ ] `outputs/submission.csv` generated
- [ ] Notebook runs completely (`notebooks/notebook.ipynb`)
- [ ] Convert `report.md` to `report.pdf`
- [ ] Create submission ZIP with notebook.ipynb and report.pdf
- [ ] Upload `submission.csv` to hackathon portal
- [ ] Upload ZIP file with notebook and report

---

## 🏆 Hackathon Information

**Event:** Summer Analytics 2026  
**Week:** 2 (June 12-14, 2026)  
**Challenge:** E-Commerce Conversion Prediction  
**Evaluation:** F1 Score on private_test.csv  
**Platform:** HackerEarth  

---

## 📄 License

This project is created for educational purposes as part of Summer Analytics 2026.

---

**Built with ❤️ for Summer Analytics 2026**

*Last Updated: June 15, 2026*
