"""
Data Preprocessing Module for E-Commerce Conversion Prediction
Handles missing values, encoding, and data preparation
"""

import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.impute import SimpleImputer


class DataPreprocessor:
    """
    Handles all preprocessing steps including imputation and encoding
    """
    
    def __init__(self):
        self.imputer = None
        self.label_encoders = {}
        self.numeric_features = []
        self.categorical_features = []
        
    def fit(self, df, categorical_cols=['Device_Type', 'Traffic_Source', 'age_group']):
        """
        Fit the preprocessor on the data
        
        Parameters:
        -----------
        df : pandas.DataFrame
            Training dataframe
        categorical_cols : list
            List of categorical column names
        """
        self.categorical_features = categorical_cols
        self.numeric_features = [col for col in df.columns 
                                if col not in categorical_cols and col != 'Converted']
        
        # Fit imputer on numeric features (use median - robust to outliers)
        self.imputer = SimpleImputer(strategy='median')
        self.imputer.fit(df[self.numeric_features])
        
        # Fit label encoders on categorical features
        for col in self.categorical_features:
            if col in df.columns:
                le = LabelEncoder()
                # Fit on all unique values including NaN as string
                values = df[col].fillna('Missing').astype(str)
                le.fit(values)
                self.label_encoders[col] = le
        
        return self
    
    def transform(self, df):
        """
        Transform the data using fitted preprocessor
        
        Parameters:
        -----------
        df : pandas.DataFrame
            Dataframe to transform
            
        Returns:
        --------
        pandas.DataFrame
            Transformed dataframe
        """
        df = df.copy()
        
        # Impute numeric features
        df[self.numeric_features] = self.imputer.transform(df[self.numeric_features])
        
        # Encode categorical features
        for col in self.categorical_features:
            if col in df.columns:
                # Handle unseen categories by replacing with 'Missing'
                values = df[col].fillna('Missing').astype(str)
                # Transform, handling unseen labels
                le = self.label_encoders[col]
                df[col] = values.apply(lambda x: le.transform([x])[0] 
                                      if x in le.classes_ 
                                      else le.transform(['Missing'])[0])
        
        return df
    
    def fit_transform(self, df, categorical_cols=['Device_Type', 'Traffic_Source', 'age_group']):
        """
        Fit and transform in one step
        
        Parameters:
        -----------
        df : pandas.DataFrame
            Training dataframe
        categorical_cols : list
            List of categorical column names
            
        Returns:
        --------
        pandas.DataFrame
            Transformed dataframe
        """
        self.fit(df, categorical_cols)
        return self.transform(df)


def prepare_data(train_df, test_df, feature_engineer_fn=None):
    """
    Prepare train and test data with preprocessing
    
    Parameters:
    -----------
    train_df : pandas.DataFrame
        Training dataframe
    test_df : pandas.DataFrame
        Test dataframe
    feature_engineer_fn : callable, optional
        Function to create engineered features
        
    Returns:
    --------
    tuple
        (X_train, y_train, X_test, preprocessor)
    """
    # Apply feature engineering if provided
    if feature_engineer_fn is not None:
        train_df = feature_engineer_fn(train_df)
        test_df = feature_engineer_fn(test_df)
    
    # Separate features and target
    X_train = train_df.drop('Converted', axis=1) if 'Converted' in train_df.columns else train_df
    y_train = train_df['Converted'] if 'Converted' in train_df.columns else None
    X_test = test_df.drop('Converted', axis=1) if 'Converted' in test_df.columns else test_df
    
    # Initialize and fit preprocessor on combined data for better coverage
    preprocessor = DataPreprocessor()
    combined_df = pd.concat([X_train, X_test], axis=0, ignore_index=True)
    preprocessor.fit(combined_df)
    
    # Transform both datasets
    X_train = preprocessor.transform(X_train)
    X_test = preprocessor.transform(X_test)
    
    return X_train, y_train, X_test, preprocessor
