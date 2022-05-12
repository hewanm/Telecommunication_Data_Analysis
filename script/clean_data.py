import numpy as np
import pandas as pd

def drop_duplicates(df):
    df.drop_duplicates(inplace=True)

def drop_columns(df, columns):
    df.drop(columns, axis=1, inplace=True)

def convert_to_string(df, columns):
    for col in columns:
        df[col] = df[col].astype("string")

def convert_to_numbers(df, columns):
    for col in columns:
        df[col] = pd.to_numeric(df[col])

def convert_to_int(df, columns):
    for col in columns:
        df[col] = df[col].astype("int64")

def convert_to_datetime(df, columns):
    for col in columns:
        df[col] = pd.to_datetime(df[col])

def multiply_by_factor(df, columns, factor):
    for col in columns:
        df[col] = df[col] * factor
        
        
# how many missing values exist or better still what is the % of missing values in the dataset?
def percent_missing(df):

    # Calculate total number of cells in dataframe
    totalCells = np.product(df.shape)

    # Count number of missing values per column
    missingCount = df.isnull().sum()

    # Calculate total number of missing values
    totalMissing = missingCount.sum()

    # Calculate percentage of missing values
    print("The dataset contains", round(((totalMissing/totalCells) * 100), 2), "%", "missing values.")

percent_missing(db)



def percent_missing_rows(df):

    # Calculate total number rows with missing values
    missing_rows = sum([True for idx,row in df.iterrows() if any(row.isna())])

    # Calculate total number of rows
    total_rows = df.shape[0]

    # Calculate the percentage of missing rows
    print(round(((missing_rows/total_rows) * 100), 2), "%",
    "of the rows in the dataset contain atleast one missing value.")

# Function to calculate missing values by column
def missing_values_table(df):
    # Total missing values
    mis_val = df.isnull().sum()

    # Percentage of missing values
    mis_val_percent = 100 * mis_val / len(df)

    # dtype of missing values
    mis_val_dtype = df.dtypes

    # Make a table with the results
    mis_val_table = pd.concat([mis_val, mis_val_percent, mis_val_dtype], axis=1)

    # Rename the columns
    mis_val_table_ren_columns = mis_val_table.rename(
    columns = {0 : 'Missing Values', 1 : '% of Total Values', 2: 'Dtype'})

    # Sort the table by percentage of missing descending and remove columns with no missing values
    mis_val_table_ren_columns = mis_val_table_ren_columns[
        mis_val_table_ren_columns.iloc[:,0] != 0].sort_values(
    '% of Total Values', ascending=False).round(2)

    # Print some summary information
    print ("Your selected dataframe has " + str(df.shape[1]) + " columns.\n"
        "There are " + str(mis_val_table_ren_columns.shape[0]) +
          " columns that have missing values.")

    if mis_val_table_ren_columns.shape[0] == 0:
        return

    # Return the dataframe with missing information
    return mis_val_table_ren_columns



# fill missing with ffill method

def fix_missing_ffill(df, col):
    df[col] = df[col].fillna(method='ffill')
    return df[col]


def fix_missing_bfill(df, col):
    df[col] = df[col].fillna(method='bfill')
    return df[col]

def fix_missing_median(df, col):
    median = df[col].median()
    df[col] = df[col].fillna(median)
    return df[col]

def fix_missing_value(df, col, value):
    df[col] = df[col].fillna(value)
    return df[col]

def drop_rows_with_missing_values(df):
    df.dropna(inplace=True)
