"""
Utility functions for the E-Commerce Conversion Prediction project
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def load_data(train_path, public_test_path=None, private_test_path=None):
    """
    Load datasets from CSV files
    
    Parameters:
    -----------
    train_path : str
        Path to training data
    public_test_path : str, optional
        Path to public test data
    private_test_path : str, optional
        Path to private test data
        
    Returns:
    --------
    tuple
        (train_df, public_test_df, private_test_df)
    """
    train_df = pd.read_csv(train_path)
    print(f"Training data loaded: {train_df.shape}")
    
    public_test_df = None
    if public_test_path:
        public_test_df = pd.read_csv(public_test_path)
        print(f"Public test data loaded: {public_test_df.shape}")
    
    private_test_df = None
    if private_test_path:
        private_test_df = pd.read_csv(private_test_path)
        print(f"Private test data loaded: {private_test_df.shape}")
    
    return train_df, public_test_df, private_test_df


def explore_data(df, target_col='Converted'):
    """
    Perform basic exploratory data analysis
    
    Parameters:
    -----------
    df : pandas.DataFrame
        Dataframe to explore
    target_col : str
        Name of target column
    """
    print("="*60)
    print("DATASET OVERVIEW")
    print("="*60)
    print(f"\nShape: {df.shape}")
    print(f"\nColumns: {df.columns.tolist()}")
    
    print("\n" + "="*60)
    print("DATA TYPES")
    print("="*60)
    print(df.dtypes)
    
    print("\n" + "="*60)
    print("MISSING VALUES")
    print("="*60)
    missing = df.isnull().sum()
    missing_pct = (missing / len(df)) * 100
    missing_df = pd.DataFrame({
        'Missing_Count': missing,
        'Percentage': missing_pct
    })
    print(missing_df[missing_df['Missing_Count'] > 0].sort_values('Percentage', ascending=False))
    
    print("\n" + "="*60)
    print("BASIC STATISTICS")
    print("="*60)
    print(df.describe())
    
    if target_col in df.columns:
        print("\n" + "="*60)
        print("TARGET DISTRIBUTION")
        print("="*60)
        target_counts = df[target_col].value_counts()
        print(target_counts)
        print(f"\nClass Balance Ratio: {target_counts[0] / target_counts[1]:.2f}:1")


def plot_feature_importance(importance_df, top_n=20, figsize=(10, 8)):
    """
    Plot feature importance
    
    Parameters:
    -----------
    importance_df : pandas.DataFrame
        Feature importance dataframe
    top_n : int
        Number of top features to plot
    figsize : tuple
        Figure size
    """
    plt.figure(figsize=figsize)
    
    top_features = importance_df.head(top_n)
    
    plt.barh(range(len(top_features)), top_features['importance'])
    plt.yticks(range(len(top_features)), top_features['feature'])
    plt.xlabel('Importance')
    plt.title(f'Top {top_n} Feature Importance')
    plt.gca().invert_yaxis()
    plt.tight_layout()
    
    return plt


def plot_threshold_optimization(threshold_df, best_threshold, best_f1, figsize=(10, 6)):
    """
    Plot threshold vs F1 Score
    
    Parameters:
    -----------
    threshold_df : pandas.DataFrame
        Dataframe with threshold and f1_score columns
    best_threshold : float
        Optimal threshold value
    best_f1 : float
        Best F1 score achieved
    figsize : tuple
        Figure size
    """
    plt.figure(figsize=figsize)
    
    plt.plot(threshold_df['threshold'], threshold_df['f1_score'], 
             linewidth=2, label='F1 Score')
    plt.axvline(best_threshold, color='red', linestyle='--', 
                label=f'Best Threshold = {best_threshold:.2f}')
    plt.axhline(best_f1, color='green', linestyle='--', 
                label=f'Best F1 = {best_f1:.4f}')
    
    plt.xlabel('Threshold')
    plt.ylabel('F1 Score')
    plt.title('Threshold Optimization')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    
    return plt


def create_submission(user_ids, predictions, output_path='submission.csv'):
    """
    Create submission file in required format
    
    Parameters:
    -----------
    user_ids : numpy.ndarray or pandas.Series
        User IDs from test set
    predictions : numpy.ndarray
        Predicted labels (0 or 1)
    output_path : str
        Path to save submission file
    """
    submission_df = pd.DataFrame({
        'User_ID': user_ids,
        'Converted': predictions
    })
    
    submission_df.to_csv(output_path, index=False)
    print(f"Submission file created: {output_path}")
    print(f"Shape: {submission_df.shape}")
    print(f"\nPrediction distribution:")
    print(submission_df['Converted'].value_counts())
    
    return submission_df


def plot_correlation_matrix(df, target_col='Converted', figsize=(12, 10)):
    """
    Plot correlation matrix heatmap
    
    Parameters:
    -----------
    df : pandas.DataFrame
        Dataframe with numeric features
    target_col : str
        Name of target column
    figsize : tuple
        Figure size
    """
    # Select only numeric columns
    numeric_df = df.select_dtypes(include=[np.number])
    
    plt.figure(figsize=figsize)
    
    corr_matrix = numeric_df.corr()
    
    # Plot heatmap
    sns.heatmap(corr_matrix, annot=False, cmap='coolwarm', center=0,
                square=True, linewidths=0.5, cbar_kws={"shrink": 0.8})
    
    plt.title('Feature Correlation Matrix')
    plt.tight_layout()
    
    # Print top correlations with target
    if target_col in corr_matrix.columns:
        print("\nTop correlations with target:")
        target_corr = corr_matrix[target_col].sort_values(ascending=False)
        print(target_corr[1:11])  # Top 10 (excluding target itself)
    
    return plt
