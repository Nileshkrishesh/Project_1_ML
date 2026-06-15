"""
Feature Engineering Module for E-Commerce Conversion Prediction
Creates interaction features, aggregations, and transformations
"""

import numpy as np
import pandas as pd


def create_features(df):
    """
    Create engineered features from the base dataset
    
    Parameters:
    -----------
    df : pandas.DataFrame
        Input dataframe with base features
        
    Returns:
    --------
    pandas.DataFrame
        Dataframe with additional engineered features
    """
    df = df.copy()
    
    # Interaction Features
    # Engagement score: pages × products (measures browsing depth)
    df['engagement_score'] = df['Pages_Viewed'] * df['Products_Viewed']
    
    # Time per page (how long user spends per page on average)
    df['time_per_page'] = df['Time_On_Site'] / (df['Pages_Viewed'] + 1)
    
    # Products per page (how focused is the user on products)
    df['products_per_page'] = df['Products_Viewed'] / (df['Pages_Viewed'] + 1)
    
    # Total interaction metric
    df['total_interaction'] = df['Pages_Viewed'] + df['Products_Viewed']
    
    # Time × Products interaction
    df['time_products'] = df['Time_On_Site'] * df['Products_Viewed']
    
    # Purchase × Discount interaction
    df['purchase_discount_interaction'] = df['Previous_Purchases'] * df['Discount_Seen']
    
    # Binary Features
    # Returning buyer (has made at least one purchase)
    df['returning_buyer'] = (df['Previous_Purchases'] > 0).astype(int)
    
    # High previous purchases (power user indicator)
    df['high_previous'] = (df['Previous_Purchases'] >= 3).astype(int)
    
    # Discount-driven buyer (saw discount AND has bought before)
    df['discount_buyer'] = ((df['Discount_Seen'] == 1) & 
                            (df['Previous_Purchases'] > 0)).astype(int)
    
    # Income Transformations
    # Log transform to reduce skewness
    df['log_income'] = np.log1p(df['Income'].fillna(0))
    
    # Income per age (purchasing power relative to age)
    df['income_per_age'] = df['Income'] / (df['Age'] + 1)
    
    # Age Groups (categorical binning)
    df['age_group'] = pd.cut(df['Age'], 
                             bins=[0, 25, 35, 50, 100],
                             labels=['<25', '25-35', '35-50', '50+'])
    df['age_group'] = df['age_group'].astype(str)
    
    return df


def get_feature_names():
    """
    Returns list of all feature names (base + engineered)
    
    Returns:
    --------
    list
        List of feature column names
    """
    base_features = [
        'Age', 'Income', 'Pages_Viewed', 'Products_Viewed', 
        'Time_On_Site', 'Previous_Purchases', 'Device_Type', 
        'Traffic_Source', 'City_Tier', 'Campaign_Clicked', 
        'Discount_Seen', 'User_Rating', 'Cart_Abandonment'
    ]
    
    engineered_features = [
        'engagement_score', 'time_per_page', 'products_per_page',
        'total_interaction', 'time_products', 'purchase_discount_interaction',
        'returning_buyer', 'high_previous', 'discount_buyer',
        'log_income', 'income_per_age', 'age_group'
    ]
    
    return base_features + engineered_features


def get_categorical_features():
    """
    Returns list of categorical feature names
    
    Returns:
    --------
    list
        List of categorical column names
    """
    return ['Device_Type', 'Traffic_Source', 'age_group']
