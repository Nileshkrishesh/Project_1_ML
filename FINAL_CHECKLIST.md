# ✅ Final Submission Checklist

## 📋 Pre-Submission Checklist

Use this checklist to ensure everything is ready for submission.

---

## 1️⃣ Environment Setup

- [ ] Python 3.9+ installed
- [ ] All dependencies installed (`pip install -r requirements.txt`)
- [ ] Virtual environment activated (recommended)
- [ ] `python setup_check.py` passes all checks

---

## 2️⃣ Data Files

- [ ] `data/train.csv` exists and is valid
- [ ] `data/public_test.csv` exists and is valid
- [ ] `data/private_test.csv` exists and is valid
- [ ] All CSV files have correct columns
- [ ] No data corruption or formatting issues

---

## 3️⃣ Code Verification

### Core Modules (`src/`)
- [ ] `src/feature_engineering.py` - Creates 12 features
- [ ] `src/preprocessing.py` - Handles missing values & encoding
- [ ] `src/model.py` - Implements XGBoost + LightGBM ensemble
- [ ] `src/utils.py` - Utility functions working
- [ ] `src/__init__.py` - Package initialization

### Scripts
- [ ] `train.py` - Main pipeline runs without errors
- [ ] `setup_check.py` - Verification script works

### Notebooks
- [ ] `notebooks/notebook.ipynb` - All cells execute successfully
- [ ] Notebook generates same results as train.py
- [ ] All visualizations render correctly

---

## 4️⃣ Pipeline Execution

### Run Complete Pipeline
```bash
python train.py
```

Verify the following outputs:

- [ ] Pipeline completes all 9 steps
- [ ] No error messages during execution
- [ ] F1 Score displayed (should be ~0.54)
- [ ] Optimal threshold displayed (should be ~0.39)
- [ ] Feature importance shown
- [ ] `outputs/submission.csv` created

### Check Console Output

Expected final output:
```
============================================================
PIPELINE COMPLETED SUCCESSFULLY!
============================================================

Final Results:
  - Model: XGBoost + LightGBM Ensemble
  - Public Test F1 Score: 0.5438
  - Optimal Threshold: 0.39
  - Submission file: outputs/submission.csv
  - Total predictions: XXXX

============================================================
```

- [ ] Console output matches expected format
- [ ] No warnings or errors
- [ ] All metrics displayed correctly

---

## 5️⃣ Output Files Verification

### Submission File (`outputs/submission.csv`)

```python
import pandas as pd

# Load and verify
submission = pd.read_csv('outputs/submission.csv')

# Checks:
assert list(submission.columns) == ['User_ID', 'Converted']
assert submission.shape[0] > 0
assert submission['Converted'].isin([0, 1]).all()
assert submission['User_ID'].nunique() == len(submission)
print("✓ Submission file is valid!")
```

- [ ] File exists at `outputs/submission.csv`
- [ ] Has exactly 2 columns: `User_ID`, `Converted`
- [ ] No missing values
- [ ] `Converted` contains only 0 and 1
- [ ] Number of rows matches private_test.csv
- [ ] `User_ID` values match private_test.csv
- [ ] No duplicate User_IDs

### Visualizations (`outputs/`)

- [ ] `feature_importance.png` created
- [ ] `threshold_optimization.png` created
- [ ] `target_distribution.png` created
- [ ] `correlation_matrix.png` created
- [ ] All images render correctly

---

## 6️⃣ Notebook Verification

### Run Notebook End-to-End

```bash
jupyter notebook
# Open notebooks/notebook.ipynb
# Kernel > Restart & Run All
```

- [ ] All cells execute without errors
- [ ] All visualizations render
- [ ] Same F1 Score as train.py
- [ ] Submission file generated
- [ ] Output is reproducible

### Notebook Content Check

- [ ] Has markdown explanations
- [ ] Code is commented
- [ ] Results are displayed
- [ ] Methodology is clear
- [ ] Can be understood by others

---

## 7️⃣ Documentation

### Required Files

- [ ] `README.md` - Complete project overview
- [ ] `report.md` - Methodology summary (1 page)
- [ ] `requirements.txt` - All dependencies listed
- [ ] `.gitignore` - Excludes unnecessary files

### Convert Report to PDF

```bash
# Using pandoc (if installed)
pandoc report.md -o report.pdf

# Or use online converter:
# https://www.markdowntopdf.com/
# https://www.browserling.com/tools/markdown-to-pdf
```

- [ ] `report.pdf` created from `report.md`
- [ ] PDF is readable and well-formatted
- [ ] Tables and formatting preserved
- [ ] Page count is 1-2 pages maximum

---

## 8️⃣ Submission Package

### Create Submission ZIP

**Contents Required:**
1. `notebook.ipynb`
2. `report.pdf`

```bash
# Windows PowerShell
Compress-Archive -Path notebooks\notebook.ipynb,report.pdf -DestinationPath submission.zip

# Linux/Mac
zip submission.zip notebooks/notebook.ipynb report.pdf

# Or manually:
# 1. Create new folder called "submission"
# 2. Copy notebook.ipynb and report.pdf into it
# 3. Right-click folder > "Compress" or "Send to > Compressed folder"
```

- [ ] `submission.zip` created
- [ ] ZIP contains `notebook.ipynb`
- [ ] ZIP contains `report.pdf`
- [ ] ZIP is less than 10MB
- [ ] ZIP can be extracted successfully

### Verify ZIP Contents

```bash
# Windows
tar -tf submission.zip

# Linux/Mac
unzip -l submission.zip
```

Expected output:
```
notebook.ipynb
report.pdf
```

- [ ] Only required files in ZIP
- [ ] No extra files or folders
- [ ] File paths are correct

---

## 9️⃣ Final Submission

### Upload to HackerEarth

Portal: https://www.hackerearth.com/challenges/competitive/summer-analytics-2026/

**File 1: Predictions CSV**
- [ ] Navigate to submission page
- [ ] Click "Upload submission"
- [ ] Upload `outputs/submission.csv`
- [ ] Verify upload successful
- [ ] Check leaderboard updates (if public)

**File 2: Code & Report ZIP**
- [ ] Navigate to code submission section
- [ ] Upload `submission.zip`
- [ ] Verify upload successful
- [ ] Download and verify uploaded file

### Post-Submission Verification

- [ ] Submission shows "Successful" status
- [ ] Score is displayed (if public leaderboard)
- [ ] Both files uploaded correctly
- [ ] Confirmation email received (if applicable)

---

## 🔟 Backup & Version Control

### Git Commit

```bash
git add .
git commit -m "Final submission for Week 2 Hackathon"
git tag v1.0-submission
```

- [ ] Code committed to Git
- [ ] Tagged with version
- [ ] Pushed to remote (GitHub/GitLab)

### Backup Files

- [ ] Copy entire project folder to backup location
- [ ] Save submission files separately
- [ ] Keep copy of submission confirmation

---

## ⚠️ Common Issues & Solutions

### Issue: Low F1 Score (< 0.50)

**Checks:**
- [ ] All 12 engineered features created?
- [ ] Preprocessing applied correctly?
- [ ] Models trained on correct data?
- [ ] Threshold optimized?

### Issue: Submission File Wrong Format

**Checks:**
- [ ] Has exactly 2 columns?
- [ ] Column names are 'User_ID' and 'Converted'?
- [ ] No index column?
- [ ] Values are 0 or 1 only?

### Issue: Notebook Doesn't Run

**Checks:**
- [ ] All cells have correct paths (`../data/` not `data/`)?
- [ ] Kernel restarted before running?
- [ ] All dependencies installed in notebook environment?
- [ ] No hardcoded paths?

---

## 📊 Expected Metrics

Your results should be approximately:

```
Training Set Size:     10,000 samples
Public Test Set Size:  ~2,500 samples
Private Test Set Size: ~2,500 samples

Class Distribution:
  - Not Converted (0): ~69%
  - Converted (1):     ~31%

Model Performance:
  - Public Test F1 Score:  0.54 (±0.02)
  - Optimal Threshold:     0.39 (±0.02)
  - Training Time:         2-5 minutes
  
Top 5 Features:
  1. Pages_Viewed
  2. engagement_score
  3. total_interaction
  4. Products_Viewed
  5. discount_buyer
```

---

## 🎯 Final Confidence Check

Answer these questions before submitting:

1. **Can you run `python train.py` without errors?**
   - [ ] Yes ✅
   
2. **Does it generate `outputs/submission.csv`?**
   - [ ] Yes ✅
   
3. **Is your F1 Score around 0.54?**
   - [ ] Yes ✅
   
4. **Can someone else run your notebook and get same results?**
   - [ ] Yes ✅
   
5. **Is your report.pdf clear and well-written?**
   - [ ] Yes ✅

**If you answered YES to all 5, you're ready to submit! 🚀**

---

## 📝 Submission Summary

Fill this out before submitting:

```
Submission Details:
===================
Date: _______________
Time: _______________

Files Submitted:
✓ submission.csv (predictions)
✓ submission.zip (notebook + report)

Results:
✓ F1 Score: _____________
✓ Threshold: ____________
✓ Training Time: ________

Confirmation:
✓ Submission ID: _______________
✓ Leaderboard Rank: ____________ (if public)

Notes:
_______________________________________
_______________________________________
_______________________________________
```

---

## 🎉 Congratulations!

If you've completed all items in this checklist, you're ready for submission!

**Good luck! 🏆**

---

**Need help?** Check:
- `README.md` - Project overview
- `GETTING_STARTED.md` - Quick start guide
- `INSTALLATION.md` - Setup help
- `USAGE.md` - Detailed usage
- Discord community - Ask questions

**Last updated:** June 15, 2026
