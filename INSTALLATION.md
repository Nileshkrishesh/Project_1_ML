# Installation Guide

## Prerequisites

- Python 3.9 or higher
- pip (Python package manager)
- Git (for version control)

## Step-by-Step Installation

### 1. Clone or Download the Repository

```bash
# If using Git
git clone <repository-url>
cd Project_1_ML

# Or download and extract the ZIP file
```

### 2. Create Virtual Environment (Recommended)

#### Windows:
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
venv\Scripts\activate
```

#### Linux/Mac:
```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate
```

### 3. Install Dependencies

```bash
# Upgrade pip
pip install --upgrade pip

# Install required packages
pip install -r requirements.txt
```

This will install:
- numpy (1.24.3)
- pandas (2.0.3)
- scikit-learn (1.3.0)
- xgboost (1.7.6)
- lightgbm (4.0.0)
- matplotlib (3.7.2)
- seaborn (0.12.2)
- jupyter (1.0.0)
- notebook (7.0.0)

### 4. Verify Installation

```bash
# Test imports
python -c "import numpy, pandas, sklearn, xgboost, lightgbm; print('All packages installed successfully!')"
```

### 5. Download Dataset

1. Go to the hackathon page: https://www.hackerearth.com/challenges/competitive/summer-analytics-2026/
2. Download the following files:
   - train.csv
   - public_test.csv
   - private_test.csv
   - sample_submission.csv (optional)

3. Place all files in the `data/` directory

### 6. Verify Project Structure

Your project should look like this:

```
Project_1_ML/
├── data/
│   ├── train.csv
│   ├── public_test.csv
│   ├── private_test.csv
│   └── sample_submission.csv
├── src/
│   ├── __init__.py
│   ├── feature_engineering.py
│   ├── preprocessing.py
│   ├── model.py
│   └── utils.py
├── notebooks/
│   └── notebook.ipynb
├── outputs/
├── train.py
└── requirements.txt
```

## Running the Project

### Option 1: Python Script

```bash
# Run the complete pipeline
python train.py
```

Expected output location: `outputs/submission.csv`

### Option 2: Jupyter Notebook

```bash
# Start Jupyter server
jupyter notebook

# In browser, navigate to notebooks/notebook.ipynb
# Run all cells: Kernel > Restart & Run All
```

## Troubleshooting

### Issue: Module not found
**Solution:** Make sure virtual environment is activated and all packages are installed

```bash
pip install -r requirements.txt
```

### Issue: XGBoost or LightGBM installation fails
**Solution:** Install Microsoft Visual C++ Build Tools (Windows) or build essentials (Linux)

**Windows:**
- Download from: https://visualstudio.microsoft.com/visual-cpp-build-tools/
- Or try: `pip install --upgrade xgboost lightgbm`

**Linux:**
```bash
sudo apt-get install build-essential
```

### Issue: Jupyter kernel not found
**Solution:** Install IPython kernel

```bash
pip install ipykernel
python -m ipykernel install --user --name=venv
```

### Issue: Data files not found
**Solution:** Check data files are in correct location

```bash
# Windows
dir data

# Linux/Mac
ls -la data/
```

### Issue: Out of memory error
**Solution:** Reduce n_estimators in model.py or use a machine with more RAM

## System Requirements

### Minimum:
- CPU: 2 cores
- RAM: 4 GB
- Disk: 500 MB free space

### Recommended:
- CPU: 4+ cores
- RAM: 8 GB+
- Disk: 2 GB free space

## Getting Help

If you encounter issues:

1. Check the error message carefully
2. Verify all dependencies are installed: `pip list`
3. Ensure data files are in the correct location
4. Check Python version: `python --version` (should be 3.9+)
5. Try reinstalling dependencies: `pip install -r requirements.txt --force-reinstall`

## Next Steps

Once installation is complete:

1. Read the [README.md](README.md) for project overview
2. Check [report.md](report.md) for methodology details
3. Run `train.py` or open `notebook.ipynb`
4. Review outputs in `outputs/` directory

---

Happy coding! 🚀
