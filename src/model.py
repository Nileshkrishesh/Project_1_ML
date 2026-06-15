"""
Model Training Module for E-Commerce Conversion Prediction
Implements XGBoost + LightGBM ensemble
"""

import numpy as np
import pandas as pd
from xgboost import XGBClassifier
from lightgbm import LGBMClassifier
from sklearn.metrics import f1_score, classification_report, confusion_matrix


class EnsembleModel:
    """
    Ensemble of XGBoost and LightGBM with equal weight averaging
    """
    
    def __init__(self, random_state=42):
        """
        Initialize the ensemble model
        
        Parameters:
        -----------
        random_state : int
            Random seed for reproducibility
        """
        self.random_state = random_state
        self.xgb_model = None
        self.lgbm_model = None
        self.models = []
        
    def _create_xgboost(self, scale_pos_weight=2.27):
        """Create XGBoost classifier with optimized hyperparameters"""
        return XGBClassifier(
            n_estimators=500,
            max_depth=5,
            learning_rate=0.03,
            subsample=0.8,
            colsample_bytree=0.7,
            reg_alpha=0.1,
            scale_pos_weight=scale_pos_weight,
            random_state=self.random_state,
            eval_metric='logloss',
            use_label_encoder=False
        )
    
    def _create_lightgbm(self):
        """Create LightGBM classifier with optimized hyperparameters"""
        return LGBMClassifier(
            n_estimators=500,
            max_depth=5,
            learning_rate=0.03,
            subsample=0.8,
            colsample_bytree=0.7,
            reg_alpha=0.1,
            is_unbalance=True,
            random_state=self.random_state,
            verbose=-1
        )
    
    def fit(self, X_train, y_train, scale_pos_weight=None):
        """
        Train both XGBoost and LightGBM models
        
        Parameters:
        -----------
        X_train : pandas.DataFrame or numpy.ndarray
            Training features
        y_train : pandas.Series or numpy.ndarray
            Training labels
        scale_pos_weight : float, optional
            Weight for positive class (auto-calculated if None)
        """
        # Calculate scale_pos_weight if not provided
        if scale_pos_weight is None:
            neg_count = (y_train == 0).sum()
            pos_count = (y_train == 1).sum()
            scale_pos_weight = neg_count / pos_count
            print(f"Auto-calculated scale_pos_weight: {scale_pos_weight:.2f}")
        
        # Train XGBoost
        print("Training XGBoost...")
        self.xgb_model = self._create_xgboost(scale_pos_weight)
        self.xgb_model.fit(X_train, y_train)
        
        # Train LightGBM
        print("Training LightGBM...")
        self.lgbm_model = self._create_lightgbm()
        self.lgbm_model.fit(X_train, y_train)
        
        self.models = [self.xgb_model, self.lgbm_model]
        
        print("Training complete!")
        return self
    
    def predict_proba(self, X):
        """
        Predict probabilities using ensemble (average of both models)
        
        Parameters:
        -----------
        X : pandas.DataFrame or numpy.ndarray
            Features to predict
            
        Returns:
        --------
        numpy.ndarray
            Predicted probabilities (average of both models)
        """
        xgb_proba = self.xgb_model.predict_proba(X)
        lgbm_proba = self.lgbm_model.predict_proba(X)
        
        # Equal weight averaging
        ensemble_proba = (xgb_proba + lgbm_proba) / 2
        return ensemble_proba
    
    def predict(self, X, threshold=0.5):
        """
        Predict binary labels using ensemble
        
        Parameters:
        -----------
        X : pandas.DataFrame or numpy.ndarray
            Features to predict
        threshold : float
            Decision threshold (default 0.5)
            
        Returns:
        --------
        numpy.ndarray
            Predicted binary labels
        """
        proba = self.predict_proba(X)[:, 1]
        return (proba >= threshold).astype(int)
    
    def get_feature_importance(self, feature_names=None, top_n=20):
        """
        Get average feature importance from both models
        
        Parameters:
        -----------
        feature_names : list, optional
            List of feature names
        top_n : int
            Number of top features to return
            
        Returns:
        --------
        pandas.DataFrame
            Feature importance dataframe
        """
        xgb_importance = self.xgb_model.feature_importances_
        lgbm_importance = self.lgbm_model.feature_importances_
        
        # Average importance
        avg_importance = (xgb_importance + lgbm_importance) / 2
        
        if feature_names is None:
            feature_names = [f'feature_{i}' for i in range(len(avg_importance))]
        
        importance_df = pd.DataFrame({
            'feature': feature_names,
            'importance': avg_importance,
            'xgb_importance': xgb_importance,
            'lgbm_importance': lgbm_importance
        })
        
        importance_df = importance_df.sort_values('importance', ascending=False).head(top_n)
        return importance_df


def optimize_threshold(y_true, y_proba, start=0.2, end=0.8, step=0.01):
    """
    Find optimal classification threshold to maximize F1 Score
    
    Parameters:
    -----------
    y_true : numpy.ndarray
        True labels
    y_proba : numpy.ndarray
        Predicted probabilities
    start : float
        Start of threshold range
    end : float
        End of threshold range
    step : float
        Step size for threshold search
        
    Returns:
    --------
    tuple
        (optimal_threshold, best_f1_score, threshold_results)
    """
    thresholds = np.arange(start, end, step)
    f1_scores = []
    
    for threshold in thresholds:
        y_pred = (y_proba >= threshold).astype(int)
        f1 = f1_score(y_true, y_pred)
        f1_scores.append(f1)
    
    best_idx = np.argmax(f1_scores)
    best_threshold = thresholds[best_idx]
    best_f1 = f1_scores[best_idx]
    
    results_df = pd.DataFrame({
        'threshold': thresholds,
        'f1_score': f1_scores
    })
    
    return best_threshold, best_f1, results_df


def evaluate_model(y_true, y_pred, y_proba=None):
    """
    Comprehensive model evaluation
    
    Parameters:
    -----------
    y_true : numpy.ndarray
        True labels
    y_pred : numpy.ndarray
        Predicted labels
    y_proba : numpy.ndarray, optional
        Predicted probabilities
        
    Returns:
    --------
    dict
        Dictionary containing evaluation metrics
    """
    f1 = f1_score(y_true, y_pred)
    
    print(f"\nF1 Score: {f1:.4f}")
    print("\nClassification Report:")
    print(classification_report(y_true, y_pred))
    print("\nConfusion Matrix:")
    print(confusion_matrix(y_true, y_pred))
    
    return {
        'f1_score': f1,
        'classification_report': classification_report(y_true, y_pred, output_dict=True),
        'confusion_matrix': confusion_matrix(y_true, y_pred)
    }
