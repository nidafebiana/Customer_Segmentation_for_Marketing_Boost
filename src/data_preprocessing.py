# data_preprocessing.py

# Example helper functions for data cleaning and feature engineering

import pandas as pd

def clean_data(df):
    """Handle missing values and duplicates"""
    df = df.drop_duplicates()
    df['Income'].fillna(df['Income'].median(), inplace=True)
    return df

def create_features(df):
    """Feature engineering for customer spend and purchase metrics"""
    df['Total_Spend'] = df[['MntCoke', 'MntFruits', 'MntMeatProducts',
                            'MntFishProducts', 'MntSweetProducts', 'MntGoldProds']].sum(axis=1)
    df['Total_Purchases'] = df[['NumDealsPurchases', 'NumWebPurchases',
                                'NumCatalogPurchases', 'NumStorePurchases']].sum(axis=1)
    df['Online_Purchase_Ratio'] = df['NumWebPurchases'] / (df['Total_Purchases'] + 1)
    df['Avg_Spend_per_Purchase'] = df['Total_Spend'] / (df['Total_Purchases'] + 1)
    return df
