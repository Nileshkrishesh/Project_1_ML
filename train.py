"""
Main training script for E-Commerce Conversion Prediction
Runs the complete pipeline from data loading to submission generation
"""

import sys
import os
import warnings
warnings.filterwarnings('ignore')

import numpy as np
import pandas as pd

from src.utils import load_data, explore_data, create_submission
from src.feature_engineering import create_features
from src.preprocessing import prepare_data
from src.model import EnsembleModel, optimize_threshold, evaluate_model

def main():
    print("="*80)
    print("E-COMMERCE CONVERSION PREDICTION")
    print("Summer Analytics 2026 - Week 2 Hackathon")
    print("="*80)
    
    # 1. Load Data
    print("\n[1/9] Loading data...")
    train_df, public_test_df, private_test_df = load_data(
        train_path='data/train.csv',
        public_test_path='data/public_test.csv',
        private_test_path='data/private_test.csv'
    )
    
    # 2. Exploratory Data Analysis
    print("\n[2/9] Performing EDA...")
    explore_data(train_df, target_col='Converted')
    
    # 3. Feature Engineering
    print("\n[3/9] Creating engineered features...")
    train_enhanced = create_features(train_df.copy())
    public_test_enhanced = create_features(public_test_df.copy())
    private_test_enhanced = create_features(private_test_df.copy())
    print(f"Features created: {train_enhanced.shape[1] - train_df.shape[1]} new features")
    
    # 4. Store User IDs
    print("\n[4/9] Preparing data...")
    private_user_ids = private_test_enhanced['User_ID']
    
    # Drop User_ID
    train_enhanced = train_enhanced.drop('User_ID', axis=1)
    public_test_enhanced = public_test_enhanced.drop('User_ID', axis=1)
    private_test_enhanced = private_test_enhanced.drop('User_ID', axis=1)
    
    # 5. Preprocessing
    X_train, y_train, X_public_test, preprocessor = prepare_data(
        train_enhanced, 
        public_test_enhanced
    )
    
    private_test_processed = private_test_enhanced.drop('Converted', axis=1, errors='ignore')
    X_private_test = preprocessor.transform(private_test_processed)
    y_public_test = public_test_enhanced['Converted']
    
    print(f"Training set: {X_train.shape}")
    print(f"Public test set: {X_public_test.shape}")
    print(f"Private test set: {X_private_test.shape}")
    
    # 6. Model Training
    print("\n[5/9] Training ensemble model...")
    scale_pos_weight = (y_train == 0).sum() / (y_train == 1).sum()
    
    model = EnsembleModel(random_state=42)
    model.fit(X_train, y_train, scale_pos_weight=scale_pos_weight)
    
    # 7. Threshold Optimization
    print("\n[6/9] Optimizing classification threshold...")
    public_proba = model.predict_proba(X_public_test)[:, 1]
    
    best_threshold, best_f1, _ = optimize_threshold(
        y_public_test, 
        public_proba, 
        start=0.20, 
        end=0.80, 
        step=0.01
    )
    
    print(f"Optimal threshold: {best_threshold:.2f}")
    print(f"Best F1 Score on public test: {best_f1:.4f}")
    
    # 8. Evaluation
    print("\n[7/9] Evaluating model on public test set...")
    public_predictions = model.predict(X_public_test, threshold=best_threshold)
    evaluate_model(y_public_test, public_predictions, public_proba)
    
    # 9. Feature Importance
    print("\n[8/9] Analyzing feature importance...")
    feature_names = X_train.columns.tolist()
    importance_df = model.get_feature_importance(feature_names, top_n=10)
    print("\nTop 10 Features:")
    print(importance_df[['feature', 'importance']].to_string(index=False))
    
    # 10. Retrain on Full Data
    print("\n[9/9] Retraining on full labeled data...")
    X_full = pd.concat([X_train, X_public_test], axis=0, ignore_index=True)
    y_full = pd.concat([y_train, y_public_test], axis=0, ignore_index=True)
    
    final_model = EnsembleModel(random_state=42)
    final_model.fit(X_full, y_full, scale_pos_weight=scale_pos_weight)
    
    # 11. Generate Final Predictions
    print("\nGenerating final predictions...")
    private_predictions = final_model.predict(X_private_test, threshold=best_threshold)
    
    # 12. Create Submission
    submission_df = create_submission(
        user_ids=private_user_ids,
        predictions=private_predictions,
        output_path='outputs/submission.csv'
    )
    
    # Summary
    print("\n" + "="*80)
    print("PIPELINE COMPLETED SUCCESSFULLY!")
    print("="*80)
    print(f"\nFinal Results:")
    print(f"  - Model: XGBoost + LightGBM Ensemble")
    print(f"  - Public Test F1 Score: {best_f1:.4f}")
    print(f"  - Optimal Threshold: {best_threshold:.2f}")
    print(f"  - Submission file: outputs/submission.csv")
    print(f"  - Total predictions: {len(private_predictions)}")
    print("\n" + "="*80)

if __name__ == "__main__":
    main()
