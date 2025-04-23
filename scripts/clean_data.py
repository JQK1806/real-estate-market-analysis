import pandas as pd
import numpy as np
from pathlib import Path

def load_data(file_path):
    """
    Load data from a CSV file into a pandas DataFrame.
    
    Args:
        file_path (str): Path to the CSV file to be loaded.
        
    Returns:
        pd.DataFrame: Loaded data as a pandas DataFrame.
    """
    return pd.read_csv(file_path)

def clean_data(df):
    """
    Clean and preprocess the house prices dataset.
    
    This function performs the following cleaning steps:
    1. Handles missing values in numerical and categorical columns
    2. Converts ordinal categorical variables to numeric using predefined mappings
    3. Converts binary categorical variables to numeric (0/1)
    4. Creates dummy variables for remaining categorical variables
    5. Adds derived features (age and price per square foot)
    
    Args:
        df (pd.DataFrame): Raw input DataFrame containing house prices data.
        
    Returns:
        pd.DataFrame: Cleaned and preprocessed DataFrame ready for modeling.
        
    Note:
        The function assumes the input DataFrame contains columns from the House Prices
        dataset from Kaggle. It handles specific column names and data types accordingly.
    """
    print('Cleaning started.')
    df_clean = df.copy()
    
    # Handle missing values in numerical columns
    numeric_columns = df_clean.select_dtypes(include=[np.number]).columns
    for col in numeric_columns:
        if df_clean[col].isnull().any():
            df_clean[col] = df_clean[col].fillna(df_clean[col].median())

    # Handle missing values in categorical columns
    cat_columns = df_clean.select_dtypes(include=['object']).columns
    for col in cat_columns:
        if df_clean[col].isnull().any():
            df_clean[col] = df_clean[col].fillna(df_clean[col].mode()[0])

    df_clean['MSSubClass'] = df_clean['MSSubClass'].astype('object')

    # Convert ordinal categorical variables to numeric
    ordinal_mappings = {
        'ExterQual': {'Ex': 5, 'Gd': 4, 'TA': 3, 'Fa': 2, 'Po': 1},
        'ExterCond': {'Ex': 5, 'Gd': 4, 'TA': 3, 'Fa': 2, 'Po': 1},
        'BsmtQual': {'Ex': 5, 'Gd': 4, 'TA': 3, 'Fa': 2, 'Po': 1, 'NA': 0},
        'BsmtCond': {'Ex': 5, 'Gd': 4, 'TA': 3, 'Fa': 2, 'Po': 1, 'NA': 0},
        'HeatingQC': {'Ex': 5, 'Gd': 4, 'TA': 3, 'Fa': 2, 'Po': 1},
        'KitchenQual': {'Ex': 5, 'Gd': 4, 'TA': 3, 'Fa': 2, 'Po': 1},
        'FireplaceQu': {'Ex': 5, 'Gd': 4, 'TA': 3, 'Fa': 2, 'Po': 1, 'NA': 0},
        'GarageQual': {'Ex': 5, 'Gd': 4, 'TA': 3, 'Fa': 2, 'Po': 1, 'NA': 0},
        'GarageCond': {'Ex': 5, 'Gd': 4, 'TA': 3, 'Fa': 2, 'Po': 1, 'NA': 0},
        'PoolQC': {'Ex': 5, 'Gd': 4, 'TA': 3, 'Fa': 2, 'Po': 1, 'NA': 0},
        'BsmtExposure': {'Gd': 4, 'Av': 3, 'Mn': 2, 'No': 1, 'NA': 0},
        'BsmtFinType1': {'GLQ': 6, 'ALQ': 5, 'BLQ': 4, 'Rec': 3, 'LwQ': 2, 'Unf': 1, 'NA': 0},
        'BsmtFinType2': {'GLQ': 6, 'ALQ': 5, 'BLQ': 4, 'Rec': 3, 'LwQ': 2, 'Unf': 1, 'NA': 0},
        'Functional': {'Typ': 7, 'Min1': 6, 'Min2': 5, 'Mod': 4, 'Maj1': 3, 'Maj2': 2, 'Sev': 1, 'Sal': 0},
        'GarageFinish': {'Fin': 3, 'RFn': 2, 'Unf': 1, 'NA': 0},
        'PavedDrive': {'Y': 3, 'P': 2, 'N': 1},
        'LandSlope': {'Gtl': 3, 'Mod': 2, 'Sev': 1},
        'LotShape': {'Reg': 4, 'IR1': 3, 'IR2': 2, 'IR3': 1},
        'LandContour': {'Lvl': 4, 'Bnk': 3, 'HLS': 2, 'Low': 1}
    }

    for col, mapping in ordinal_mappings.items():
        if col in df_clean.columns:
            df_clean[col] = df_clean[col].map(mapping)
    
    # Convert binary categorical variables to numeric
    binary_mappings = {
        'CentralAir': {'Y': 1, 'N': 0},
        'Street': {'Pave': 1, 'Grvl': 0},
        'Alley': {'Pave': 1, 'Grvl': 0, 'NA': 0}
    }
    
    for col, mapping in binary_mappings.items():
        if col in df_clean.columns:
            df_clean[col] = df_clean[col].map(mapping)
    
    # Create dummy variables for remaining categorical variables
    categorical_columns = df_clean.select_dtypes(include=['object']).columns
    df_clean = pd.get_dummies(df_clean, columns=categorical_columns, dummy_na=False)
    
    # Add age and price per sqft cols
    current_year = pd.Timestamp.now().year
    df_clean['age'] = current_year - df_clean['YearBuilt']
    df_clean['price_per_sqft'] = df_clean['SalePrice'] / df_clean['GrLivArea']
    
    return df_clean
    


def main():
    """
    Main function to execute the data cleaning pipeline.
    
    This function:
    1. Creates the output directory if it doesn't exist
    2. Loads the raw training data
    3. Applies cleaning transformations
    4. Saves the cleaned data to the output directory
    
    The cleaned data is saved to 'data/cleaned/data_cleaned.csv'.
    """
    cleaned_dir = Path('data/cleaned')
    cleaned_dir.mkdir(parents=True, exist_ok=True)

    data = load_data('data/raw/train.csv')
    data_cleaned = clean_data(data)
    data_cleaned.to_csv('data/cleaned/data_cleaned.csv', index=False)

    print('Data cleaning completed. Cleaned Files saved in data/cleaned/')

if __name__ == '__main__':
    main()