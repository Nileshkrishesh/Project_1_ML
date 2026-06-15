# 🚀 Getting Started with E-Commerce Conversion Prediction

Welcome! This guide will help you get up and running in **5 minutes**.

## ⚡ Quick Setup (5 Minutes)

### Step 1: Verify Setup (1 min)

```bash
# Run the setup checker
python setup_check.py
```

This will verify:
- ✓ Python version (3.9+)
- ✓ All dependencies installed
- ✓ Project structure
- ✓ Source code files
- ✓ Data files present

### Step 2: Install Dependencies (2 min)

If setup_check.py shows missing packages:

```bash
pip install -r requirements.txt
```

### Step 3: Add Data Files (1 min)

Download from: https://www.hackerearth.com/challenges/competitive/summer-analytics-2026/

Place these files in the `data/` folder:
- train.csv
- public_test.csv
- private_test.csv

### Step 4: Run Pipeline (1 min)

```bash
python train.py
```

**Done!** Your submission file is ready at `outputs/submission.csv`

---

## 📂 What You Get

After running the pipeline, you'll have:

```
outputs/
├── submission.csv              # Final predictions (upload this!)
├── feature_importance.png      # Top features visualization
├── threshold_optimization.png  # Threshold tuning curve
├── target_distribution.png     # Class distribution
└── correlation_matrix.png      # Feature correlations
```

---

## 🎯 Two Ways to Run

### Option 1: Python Script (Fastest)

```bash
python train.py
```

**Pros:**
- Fast execution
- Complete automation
- Best for final submission

**Output:** Submission file at `outputs/submission.csv`

### Option 2: Jupyter Notebook (Interactive)

```bash
jupyter notebook
```

Open `notebooks/notebook.ipynb` and run all cells.

**Pros:**
- Step-by-step exploration
- Interactive visualizations
- Great for learning
- Easy to experiment

---

## 📊 Understanding the Output

### Console Output

```
[1/9] Loading data...
[2/9] Performing EDA...
[3/9] Creating engineered features...
[4/9] Preparing data...
[5/9] Training ensemble model...
[6/9] Optimizing classification threshold...
[7/9] Evaluating model on public test set...
[8/9] Analyzing feature importance...
[9/9] Retraining on full labeled data...

✓ F1 Score: 0.5438
✓ Optimal Threshold: 0.39
✓ Submission: outputs/submission.csv
```

### Submission File Format

```csv
User_ID,Converted
1,0
2,1
3,1
4,0
...
```

This file is ready to upload directly to the hackathon portal!

---

## 🔍 Quick Validation

After running, verify your submission:

```python
import pandas as pd

# Load submission
submission = pd.read_csv('outputs/submission.csv')

# Check format
print(f"Shape: {submission.shape}")
print(f"Columns: {submission.columns.tolist()}")
print(f"\nPredictions distribution:")
print(submission['Converted'].value_counts())

# Should output:
# Shape: (N, 2)  # N = number of test samples
# Columns: ['User_ID', 'Converted']
# Predictions distribution:
# 0    XXXX
# 1    YYYY
```

---

## 🎓 Understanding the Solution

### What the Pipeline Does

1. **Loads data** (10,000 training samples)
2. **Engineers 12 features** (engagement_score, time_per_page, etc.)
3. **Preprocesses** (imputes missing values, encodes categories)
4. **Trains ensemble** (XGBoost + LightGBM)
5. **Optimizes threshold** (finds best decision boundary)
6. **Evaluates performance** (F1 Score on public test)
7. **Analyzes features** (identifies top predictors)
8. **Retrains on full data** (train + public_test)
9. **Generates predictions** (for private_test)

### Key Features Created

| Feature | Impact | Description |
|---------|--------|-------------|
| `engagement_score` | ⭐⭐⭐ | Pages × Products |
| `discount_buyer` | ⭐⭐⭐ | Discount + Prior Purchase |
| `total_interaction` | ⭐⭐⭐ | Pages + Products |
| `time_per_page` | ⭐⭐ | Avg time per page |
| `returning_buyer` | ⭐⭐ | Has bought before |

### Model Performance

```
Baseline (Logistic Regression): 0.42 F1
Our Ensemble Model:             0.54 F1
Improvement:                    +29%
```

---

## 🛠️ Customization

### Change Model Parameters

Edit `src/model.py`:

```python
# Line 31-42: XGBoost parameters
n_estimators=500,      # Try 1000
max_depth=5,           # Try 7
learning_rate=0.03,    # Try 0.01

# Line 50-60: LightGBM parameters
n_estimators=500,      # Try 1000
max_depth=5,           # Try 7
learning_rate=0.03,    # Try 0.01
```

### Add Custom Features

Edit `src/feature_engineering.py`:

```python
def create_features(df):
    df = df.copy()
    
    # Existing features...
    
    # Add your custom feature here
    df['my_feature'] = df['Pages_Viewed'] / (df['Age'] + 1)
    
    return df
```

### Change Threshold

In `train.py` line 66:

```python
best_threshold, best_f1, _ = optimize_threshold(
    y_public_test, 
    public_proba, 
    start=0.20,  # Change range
    end=0.80,    # Change range
    step=0.01    # Change granularity
)
```

---

## 📚 Learning Path

### Beginner Track

1. ✅ Run `python train.py` to see it work
2. ✅ Open `notebook.ipynb` to understand each step
3. ✅ Read `report.md` for methodology
4. ✅ Check `src/feature_engineering.py` to see features

### Intermediate Track

5. ✅ Modify feature engineering
6. ✅ Try different model parameters
7. ✅ Add cross-validation
8. ✅ Experiment with threshold values

### Advanced Track

9. ✅ Implement new models (CatBoost, Neural Networks)
10. ✅ Create advanced ensemble (stacking)
11. ✅ Use SHAP for feature importance
12. ✅ Implement hyperparameter tuning (Optuna)

---

## 🐛 Troubleshooting

### Issue: "Module not found"

```bash
# Solution: Install dependencies
pip install -r requirements.txt
```

### Issue: "Data file not found"

```bash
# Solution: Check data files are in correct location
dir data               # Windows
ls data/               # Linux/Mac

# Should show: train.csv, public_test.csv, private_test.csv
```

### Issue: "Low F1 Score"

- Check if all features are created correctly
- Verify preprocessing is applied
- Ensure threshold is optimized
- Check for data leakage

### Issue: "Out of Memory"

- Reduce `n_estimators` to 200
- Close other applications
- Use a machine with more RAM

### Issue: "Training takes too long"

- Reduce `n_estimators` to 200
- Increase `learning_rate` to 0.05
- Use fewer features

---

## 📝 Submission Checklist

Before submitting to the hackathon:

- [ ] Run `python setup_check.py` (all checks pass)
- [ ] Run `python train.py` (completes successfully)
- [ ] Check `outputs/submission.csv` exists
- [ ] Verify submission format (User_ID, Converted columns)
- [ ] Test notebook runs completely (all cells execute)
- [ ] Convert `report.md` to PDF
- [ ] Create ZIP with notebook.ipynb and report.pdf

### Creating Submission ZIP

```bash
# Linux/Mac
zip -r submission.zip notebooks/notebook.ipynb report.pdf

# Windows PowerShell
Compress-Archive -Path notebooks\notebook.ipynb,report.pdf -DestinationPath submission.zip
```

### Upload to Portal

1. Go to: https://www.hackerearth.com/challenges/competitive/summer-analytics-2026/
2. Upload `outputs/submission.csv` for predictions
3. Upload `submission.zip` for notebook and report

---

## 🎯 Expected Results

After running the complete pipeline:

```
✓ Training complete
✓ Public Test F1 Score: 0.5438
✓ Optimal Threshold: 0.39
✓ Submission file created
✓ Total predictions: 2500 (example)
```

---

## 💡 Pro Tips

1. **Always run setup_check.py first** - Saves debugging time
2. **Use the notebook for exploration** - Then switch to train.py for speed
3. **Keep a backup of data/** - Don't accidentally modify original files
4. **Version control your experiments** - Use git to track changes
5. **Document your changes** - Add comments when modifying code

---

## 🤝 Getting Help

If stuck:

1. Run `python setup_check.py` to identify issues
2. Check documentation:
   - `README.md` - Project overview
   - `INSTALLATION.md` - Setup guide
   - `USAGE.md` - Detailed usage
   - `report.md` - Methodology
3. Review code comments in `src/` files
4. Ask on Summer Analytics 2026 Discord

---

## 🎉 Success!

Once you see this output, you're done:

```
============================================================
PIPELINE COMPLETED SUCCESSFULLY!
============================================================

Final Results:
  - Model: XGBoost + LightGBM Ensemble
  - Public Test F1 Score: 0.5438
  - Optimal Threshold: 0.39
  - Submission file: outputs/submission.csv
  - Total predictions: 2500

============================================================
```

**Next step:** Upload `outputs/submission.csv` to the hackathon portal! 🚀

---

**Good luck with your submission! 🏆**

*Questions? Check the other documentation files or reach out on Discord.*
