# Usage Guide

Complete guide for using the E-Commerce Conversion Prediction project.

## Quick Start

### 1. Run the Complete Pipeline

```bash
python train.py
```

This executes the entire workflow:
- Data loading and EDA
- Feature engineering
- Preprocessing
- Model training
- Threshold optimization
- Evaluation
- Submission generation

**Output:** `outputs/submission.csv`

### 2. Run Jupyter Notebook

```bash
jupyter notebook
```

Open `notebooks/notebook.ipynb` and run all cells for an interactive experience.

## Using Individual Components

### Feature Engineering

```python
from src.feature_engineering import create_features
import pandas as pd

# Load data
train_df = pd.read_csv('data/train.csv')

# Create engineered features
train_enhanced = create_features(train_df)

# View new features
new_features = [col for col in train_enhanced.columns if col not in train_df.columns]
print(f"Created features: {new_features}")
```

### Preprocessing

```python
from src.preprocessing import DataPreprocessor, prepare_data
from src.feature_engineering import create_features

# Load and enhance data
train_df = pd.read_csv('data/train.csv')
test_df = pd.read_csv('data/public_test.csv')

train_enhanced = create_features(train_df)
test_enhanced = create_features(test_df)

# Prepare data
X_train, y_train, X_test, preprocessor = prepare_data(
    train_enhanced, 
    test_enhanced
)

print(f"X_train shape: {X_train.shape}")
print(f"X_test shape: {X_test.shape}")
```

### Model Training

```python
from src.model import EnsembleModel

# Initialize model
model = EnsembleModel(random_state=42)

# Calculate class weight
scale_pos_weight = (y_train == 0).sum() / (y_train == 1).sum()

# Train model
model.fit(X_train, y_train, scale_pos_weight=scale_pos_weight)

# Predict probabilities
probabilities = model.predict_proba(X_test)

# Predict with default threshold (0.5)
predictions = model.predict(X_test, threshold=0.5)

# Predict with custom threshold
predictions_custom = model.predict(X_test, threshold=0.39)
```

### Threshold Optimization

```python
from src.model import optimize_threshold

# Get predicted probabilities
y_proba = model.predict_proba(X_test)[:, 1]

# Optimize threshold
best_threshold, best_f1, results_df = optimize_threshold(
    y_true=y_test,
    y_proba=y_proba,
    start=0.2,
    end=0.8,
    step=0.01
)

print(f"Best threshold: {best_threshold:.2f}")
print(f"Best F1 Score: {best_f1:.4f}")

# View all results
print(results_df.head(10))
```

### Model Evaluation

```python
from src.model import evaluate_model

# Get predictions
predictions = model.predict(X_test, threshold=0.39)

# Evaluate
metrics = evaluate_model(
    y_true=y_test,
    y_pred=predictions,
    y_proba=y_proba
)

print(f"F1 Score: {metrics['f1_score']:.4f}")
```

### Feature Importance

```python
# Get feature importance
feature_names = X_train.columns.tolist()
importance_df = model.get_feature_importance(feature_names, top_n=20)

# Display
print(importance_df[['feature', 'importance']])

# Plot
from src.utils import plot_feature_importance
plot_feature_importance(importance_df, top_n=15)
plt.show()
```

### Creating Submission

```python
from src.utils import create_submission

# Load private test set
private_test_df = pd.read_csv('data/private_test.csv')
private_test_enhanced = create_features(private_test_df)

# Store User IDs
user_ids = private_test_enhanced['User_ID']

# Preprocess
private_test_processed = private_test_enhanced.drop(['User_ID', 'Converted'], axis=1, errors='ignore')
X_private = preprocessor.transform(private_test_processed)

# Predict
predictions = model.predict(X_private, threshold=0.39)

# Create submission file
submission_df = create_submission(
    user_ids=user_ids,
    predictions=predictions,
    output_path='outputs/submission.csv'
)
```

## Advanced Usage

### Custom Feature Engineering

Add your own features:

```python
from src.feature_engineering import create_features

def custom_features(df):
    # Start with base features
    df = create_features(df)
    
    # Add custom features
    df['my_custom_feature'] = df['Pages_Viewed'] / (df['Time_On_Site'] + 1)
    df['another_feature'] = df['Income'] * df['Previous_Purchases']
    
    return df

# Use custom function
train_custom = custom_features(train_df)
```

### Hyperparameter Tuning

Modify model parameters in `src/model.py`:

```python
# In EnsembleModel class, modify _create_xgboost:
def _create_xgboost(self, scale_pos_weight=2.27):
    return XGBClassifier(
        n_estimators=1000,        # Increased
        max_depth=7,              # Deeper trees
        learning_rate=0.01,       # Lower learning rate
        subsample=0.8,
        colsample_bytree=0.7,
        reg_alpha=0.1,
        reg_lambda=1.0,           # Added L2 regularization
        scale_pos_weight=scale_pos_weight,
        random_state=self.random_state
    )
```

### Cross-Validation

Add cross-validation for more robust evaluation:

```python
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import f1_score

kfold = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
f1_scores = []

for fold, (train_idx, val_idx) in enumerate(kfold.split(X_train, y_train)):
    X_tr, X_val = X_train.iloc[train_idx], X_train.iloc[val_idx]
    y_tr, y_val = y_train.iloc[train_idx], y_train.iloc[val_idx]
    
    model = EnsembleModel(random_state=42)
    model.fit(X_tr, y_tr)
    
    y_pred = model.predict(X_val, threshold=0.39)
    f1 = f1_score(y_val, y_pred)
    f1_scores.append(f1)
    
    print(f"Fold {fold+1} F1 Score: {f1:.4f}")

print(f"\nMean F1 Score: {np.mean(f1_scores):.4f} (+/- {np.std(f1_scores):.4f})")
```

## Command Line Arguments

Extend `train.py` to accept arguments:

```python
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--threshold', type=float, default=0.39)
parser.add_argument('--n_estimators', type=int, default=500)
parser.add_argument('--max_depth', type=int, default=5)
args = parser.parse_args()

# Use in model
model = EnsembleModel(random_state=42)
# Configure with args...
```

Run with:
```bash
python train.py --threshold 0.40 --n_estimators 1000
```

## Tips & Best Practices

### 1. Data Validation
Always check data shapes after each step:
```python
print(f"Before: {df.shape}")
df = create_features(df)
print(f"After: {df.shape}")
```

### 2. Reproducibility
Set random seeds everywhere:
```python
import random
import numpy as np

random.seed(42)
np.random.seed(42)
```

### 3. Save Models
Save trained models for reuse:
```python
import joblib

# Save
joblib.dump(model, 'outputs/model.pkl')
joblib.dump(preprocessor, 'outputs/preprocessor.pkl')

# Load
model = joblib.load('outputs/model.pkl')
preprocessor = joblib.load('outputs/preprocessor.pkl')
```

### 4. Logging
Add logging for better debugging:
```python
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

logger.info("Starting training...")
logger.info(f"Training set size: {X_train.shape}")
```

## Troubleshooting

### Low F1 Score
- Check threshold optimization range
- Verify feature engineering is applied
- Check for data leakage
- Try different model parameters

### Memory Issues
- Reduce n_estimators
- Process data in chunks
- Use subsample parameter

### Long Training Time
- Reduce n_estimators
- Increase learning_rate
- Use fewer features

## Next Steps

- Experiment with new features
- Try different models (CatBoost, Neural Networks)
- Implement stacking ensemble
- Add cross-validation
- Tune hyperparameters with Optuna or GridSearch

---

For more details, see [README.md](README.md) and [report.md](report.md).
