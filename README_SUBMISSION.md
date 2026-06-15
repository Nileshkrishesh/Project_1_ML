# 📤 Submission Guide

Quick guide for submitting to Summer Analytics 2026 - Week 2 Hackathon.

## 🎯 Required Submissions

You need to upload **2 files** to the HackerEarth portal:

### 1️⃣ submission.csv (Predictions)
- Contains predictions for private_test.csv
- Format: `User_ID, Converted`
- Location: `outputs/submission.csv`

### 2️⃣ submission.zip (Code + Report)
- Contains `notebook.ipynb` and `report.pdf`
- Generated using the automated script

---

## ⚡ Quick Submission (3 Steps)

### Step 1: Generate Predictions

```bash
python train.py
```

This creates `outputs/submission.csv` with your predictions.

### Step 2: Convert Report to PDF

Choose one method:

**Option A: Using Pandoc** (if installed)
```bash
pandoc report.md -o report.pdf
```

**Option B: VS Code**
1. Install "Markdown PDF" extension
2. Open `report.md`
3. Right-click → "Markdown PDF: Export (pdf)"

**Option C: Online Converter**
- Visit: https://www.markdowntopdf.com/
- Upload `report.md`
- Download `report.pdf`

**Option D: Copy-Paste**
- Copy content from `report.md`
- Paste into Google Docs/Word
- Export as PDF

### Step 3: Create Submission ZIP

```bash
python create_submission_package.py
```

This automatically creates `submission.zip` with:
- ✅ notebook.ipynb
- ✅ report.pdf

---

## 📋 Submission Checklist

Before uploading, verify:

### submission.csv
- [ ] File exists at `outputs/submission.csv`
- [ ] Has columns: `User_ID`, `Converted`
- [ ] No missing values
- [ ] `Converted` contains only 0 and 1
- [ ] Number of rows matches private_test.csv
- [ ] No duplicate User_IDs

### submission.zip
- [ ] File exists at project root
- [ ] Contains `notebook.ipynb`
- [ ] Contains `report.pdf`
- [ ] ZIP size < 10 MB
- [ ] Can be extracted successfully

### notebook.ipynb
- [ ] All cells execute without errors
- [ ] Generates same results as train.py
- [ ] Well-commented and clear
- [ ] Includes visualizations
- [ ] Reproducible

### report.pdf
- [ ] Converted from report.md
- [ ] 1-2 pages maximum
- [ ] Tables formatted correctly
- [ ] Readable and professional

---

## 🔍 Manual Verification

### Check submission.csv

```python
import pandas as pd

# Load and inspect
df = pd.read_csv('outputs/submission.csv')

print(f"Shape: {df.shape}")
print(f"Columns: {df.columns.tolist()}")
print(f"Missing: {df.isnull().sum().sum()}")
print(f"\nFirst 5 rows:")
print(df.head())
print(f"\nPrediction distribution:")
print(df['Converted'].value_counts())
```

Expected output:
```
Shape: (N, 2)  # N = number of test samples
Columns: ['User_ID', 'Converted']
Missing: 0

Prediction distribution:
0    XXXX
1    YYYY
```

### Check submission.zip

**Windows:**
```bash
tar -tf submission.zip
```

**Linux/Mac:**
```bash
unzip -l submission.zip
```

Expected output:
```
notebook.ipynb
report.pdf
```

---

## 🌐 Upload to HackerEarth

### Portal URL
https://www.hackerearth.com/challenges/competitive/summer-analytics-2026/

### Upload Process

**File 1: Predictions**
1. Navigate to "Submit" tab
2. Click "Upload Submission"
3. Select `outputs/submission.csv`
4. Click "Submit"
5. Wait for evaluation (F1 Score will be displayed)

**File 2: Code & Report**
1. Navigate to "Code Submission" section
2. Click "Upload Code"
3. Select `submission.zip`
4. Add description (optional): "XGBoost + LightGBM ensemble with feature engineering"
5. Click "Submit"

### After Submission

- [ ] Submission shows "Success" status
- [ ] F1 Score displayed (if public leaderboard)
- [ ] Both files uploaded correctly
- [ ] Screenshot taken as proof

---

## 🛠️ Troubleshooting

### Issue: "Invalid file format" for submission.csv

**Fix:**
```python
import pandas as pd

# Reload and resave
df = pd.read_csv('outputs/submission.csv')
df.to_csv('outputs/submission.csv', index=False)
```

### Issue: report.pdf not created

**Fix:**
- Use online converter: https://www.markdowntopdf.com/
- Or copy report.md content to Google Docs and export as PDF

### Issue: submission.zip too large (>10 MB)

**Fix:**
- Remove output cells from notebook before zipping
- In Jupyter: Cell → All Output → Clear

### Issue: Notebook doesn't run

**Fix:**
1. Open notebook in Jupyter
2. Kernel → Restart & Clear Output
3. Cell → Run All
4. Fix any errors
5. Save notebook
6. Recreate submission.zip

---

## 📊 Expected Results

Your submission should achieve:

```
F1 Score:     0.54 (±0.02)
Rank:         Top 30% (approximate)
Threshold:    0.39
Method:       XGBoost + LightGBM Ensemble
```

---

## ✅ Final Checklist

Before clicking submit:

- [ ] `python setup_check.py` passes all checks
- [ ] `python train.py` completes successfully
- [ ] `outputs/submission.csv` created and verified
- [ ] `report.pdf` created and readable
- [ ] `python create_submission_package.py` successful
- [ ] `submission.zip` contains correct files
- [ ] Notebook tested and runs completely
- [ ] All files backed up

---

## 🎉 After Submission

1. **Take screenshot** of submission confirmation
2. **Note your score** and rank
3. **Save submission files** separately
4. **Check leaderboard** periodically
5. **Join Discord** to discuss with others

---

## 📞 Help & Support

**Technical Issues:**
- Check [FINAL_CHECKLIST.md](FINAL_CHECKLIST.md)
- Run `python setup_check.py`
- Read error messages carefully

**Portal Issues:**
- Contact HackerEarth support
- Check hackathon discussion forum
- Ask in Discord community

**Code Questions:**
- Review [USAGE.md](USAGE.md)
- Check [README.md](README.md)
- Examine code comments in `src/`

---

## 🏆 Good Luck!

You've built a strong solution with:
- ✅ Professional code
- ✅ Feature engineering
- ✅ Ensemble model
- ✅ Threshold optimization
- ✅ Complete documentation

**Time to submit and compete! 🚀**

---

**Portal:** https://www.hackerearth.com/challenges/competitive/summer-analytics-2026/  
**Deadline:** June 14, 2026, 11:59 PM IST  
**Questions?** Discord community or hackathon forum
