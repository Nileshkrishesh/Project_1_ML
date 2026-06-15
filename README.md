# E-Commerce Conversion Prediction

**Summer Analytics 2026 - Week 2 Hackathon**

A machine learning solution to predict e-commerce user conversion using XGBoost + LightGBM ensemble with comprehensive feature engineering.

## 🎯 Objective

Predict whether a user converts (makes a purchase) based on:
- User demographics (Age, Income, City Tier)
- Device and browser information
- Traffic acquisition sources
- User engagement metrics (Pages Viewed, Products Viewed, Time on Site)
- Historical purchase behavior
- Marketing campaign and discount information

**Evaluation Metric:** F1 Score

## 📊 Results

- **Public Test F1 Score:** 0.5438
- **Optimal Threshold:** 0.39
- **Model:** XGBoost + LightGBM Ensemble
- **Baseline Improvement:** ~29% over Logistic Regression

## 🏗️ Project Structure

```
Project_1_ML/
│
├── data/                          # Dataset directory
│   ├── train.csv                  # Training data (10,000 samples)
│   ├── public_test.csv            # Labeled validation set
│   ├── private_test.csv           # Unlabeled test set for submission
│   └── sample_submission.csv      # Submission format template
│
├── src/                           # Source code modules
│   ├── __init__.py
│   ├── feature_engineering.py     # Feature creation functions
│   ├── preprocessing.py           # Data preprocessing pipeline
│   ├── model.py                   # Ensemble model implementation
│   └── utils.py                   # Utility functions
│
├── notebooks/                     # Jupyter notebooks
│   └── notebook.ipynb             # Complete solution notebook
│
├── outputs/                       # Generated outputs
│   ├── submission.csv             # Final predictions
│   ├── feature_importance.png     # Feature importance plot
│   ├── threshold_optimization.png # Threshold tuning plot
│   └── target_distribution.png    # EDA visualizations
│
├── train.py                       # Main training script
├── requirements.txt               # Python dependencies
├── report.md                      # Methodology report
├── .gitignore
└── README.md                      # This file
```

## 🚀 Quick Start

### 1. Installation

```bash
# Clone the repository
git clone <repository-url>
cd Project_1_ML

# Install dependencies
pip install -r requirements.txt
```

### 2. Prepare Data

Place the following files in the `data/` directory:
- `train.csv`
- `public_test.csv`
- `private_test.csv`

### 3. Run Training Pipeline

```bash
# Run the complete pipeline
python train.py
```

This will:
- Load and explore the data
- Engineer features
- Train the ensemble model
- Optimize the decision threshold
- Generate predictions
- Create `outputs/submission.csv`

### 4. Run Jupyter Notebook

```bash
# Launch Jupyter
jupyter notebook

# Open notebooks/notebook.ipynb
```

## 🔧 Key Components

### Feature Engineering

**12 new features** created from base features:

- **Interaction Features:**
  - `engagement_score` = Pages_Viewed × Products_Viewed
  - `time_per_page` = Time_On_Site / (Pages_Viewed + 1)
  - `products_per_page` = Products_Viewed / (Pages_Viewed + 1)
  - `total_interaction` = Pages_Viewed + Products_Viewed
  - `time_products` = Time_On_Site × Products_Viewed
  - `purchase_discount_interaction` = Previous_Purchases × Discount_Seen

- **Binary Features:**
  - `returning_buyer` = Previous_Purchases > 0
  - `high_previous` = Previous_Purchases >= 3
  - `discount_buyer` = Discount_Seen=1 AND Previous_Purchases > 0

- **Transformations:**
  - `log_income` = log(1 + Income)
  - `income_per_age` = Income / (Age + 1)
  - `age_group` = Age binned into categories

### Preprocessing

- **Missing Value Imputation:** Median imputation (robust to outliers)
- **Categorical Encoding:** LabelEncoder for Device_Type and Traffic_Source
- **Fitted on Combined Data:** Train + Public_Test for better coverage

### Model Architecture

**Ensemble of Two Gradient Boosting Models:**

1. **XGBoost** (with `scale_pos_weight=2.27`)
2. **LightGBM** (with `is_unbalance=True`)

**Prediction:** Equal-weight averaging of probabilities

**Hyperparameters:**
- n_estimators: 500
- max_depth: 5
- learning_rate: 0.03
- subsample: 0.8
- colsample_bytree: 0.7
- reg_alpha: 0.1

### Threshold Optimization

- Swept thresholds from 0.20 to 0.80
- Optimized on public test set
- **Best threshold: 0.39** (maximizes F1 Score)

## 📈 Top Predictive Features

1. Pages_Viewed
2. engagement_score (pages × products)
3. total_interaction
4. Products_Viewed
5. discount_buyer (discount + prior purchase)
6. Discount_Seen
7. purchase_discount_interaction
8. Previous_Purchases

**Key Insight:** Browsing depth and discount-driven returning buyers are the strongest conversion signals.

## 📝 Methodology

See [report.md](report.md) for a detailed methodology summary.

## 📦 Dependencies

- Python 3.9+
- numpy
- pandas
- scikit-learn
- xgboost
- lightgbm
- matplotlib
- seaborn
- jupyter

## 🎓 Hackathon Details

**Event:** Summer Analytics 2026 - Week 2 Hackathon  
**Organizer:** Analytics Club  
**Format:** Binary Classification Challenge  
**Metric:** F1 Score  
**Timeline:** June 12-14, 2026

## 📄 Submission Files

Required for hackathon submission:

1. **submission.csv** - Predictions for private_test.csv (`outputs/submission.csv`)
2. **submission.zip** - Contains:
   - `notebook.ipynb` - Reproducible solution notebook
   - `report.pdf` - One-page methodology summary

### 📤 Creating Submission Package

```bash
# 1. Generate predictions
python train.py

# 2. Convert report to PDF (choose one)
pandoc report.md -o report.pdf
# Or use: https://www.markdowntopdf.com/

# 3. Create submission ZIP automatically
python create_submission_package.py
```

See [README_SUBMISSION.md](README_SUBMISSION.md) for detailed submission instructions.

## 🔍 Usage Examples

### Using Individual Modules

```python
from src.feature_engineering import create_features
from src.preprocessing import DataPreprocessor
from src.model import EnsembleModel

# Feature engineering
train_enhanced = create_features(train_df)

# Preprocessing
preprocessor = DataPreprocessor()
X_train = preprocessor.fit_transform(train_enhanced)

# Model training
model = EnsembleModel(random_state=42)
model.fit(X_train, y_train)

# Prediction with custom threshold
predictions = model.predict(X_test, threshold=0.39)
```

## 🤝 Contributing

This is a hackathon submission project. For improvements or suggestions:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📧 Contact

For questions or feedback, reach out via the Summer Analytics 2026 Discord community.

---

**Built with ❤️ for Summer Analytics 2026**