# Outputs Directory

This directory contains all generated outputs from the model pipeline.

## Files Generated

### Submission File
- **submission.csv** - Final predictions for private test set
  - Format: User_ID, Converted
  - Ready for hackathon submission

### Visualizations
- **feature_importance.png** - Top 20 most important features
- **threshold_optimization.png** - F1 Score vs threshold curve
- **target_distribution.png** - Class distribution in training data
- **correlation_matrix.png** - Feature correlation heatmap

### Model Artifacts (if saved)
- Model checkpoints
- Preprocessor objects
- Feature importance tables

## Submission File Format

```csv
User_ID,Converted
1,0
2,1
3,1
...
```

## Notes

- All outputs are generated automatically by running train.py or notebook.ipynb
- Visualizations are saved at 150 DPI for high quality
- This directory is included in .gitignore to avoid versioning large files
