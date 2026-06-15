# Notebooks Directory

## notebook.ipynb

Complete end-to-end solution notebook for the E-Commerce Conversion Prediction challenge.

### Contents

1. **Import Libraries** - Load all necessary packages
2. **Load Data** - Import train, public_test, and private_test datasets
3. **Exploratory Data Analysis** - Understand the data structure and patterns
4. **Feature Engineering** - Create 12 new engineered features
5. **Data Preprocessing** - Handle missing values and encode categorical features
6. **Model Training** - Train XGBoost + LightGBM ensemble
7. **Threshold Optimization** - Find optimal decision threshold
8. **Evaluation** - Assess performance on public test set
9. **Feature Importance** - Analyze top predictive features
10. **Retrain on Full Data** - Use all labeled data for final model
11. **Generate Predictions** - Create predictions for private test set
12. **Create Submission** - Generate submission.csv file
13. **Summary** - View final results and insights

### Usage

```bash
# Start Jupyter
jupyter notebook

# Open notebook.ipynb in the browser
# Run all cells: Cell > Run All
```

### Key Outputs

- Feature importance visualization
- Threshold optimization curve
- Correlation matrix heatmap
- Target distribution plots
- Classification report
- Submission file (submission.csv)

### Requirements

All packages must be installed from requirements.txt before running the notebook.

### Notes

- Notebook is fully reproducible with fixed random seeds
- All visualizations are saved to outputs/ directory
- Execution time: ~5-10 minutes depending on hardware
