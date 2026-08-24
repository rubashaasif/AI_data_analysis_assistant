import pandas as pd
def get_basic_statistics(df):
    statistics = {
        "total_records": len(df),
        "total_columns": len(df.columns),
        "columns": df.columns.tolist(),
        "missing_values": df.isnull().sum().to_dict(),
    }

    return statistics


def average_value(df, column):
    return df[column].mean()


def maximum_value(df, column):
    return df[column].max()


def minimum_value(df, column):
    return df[column].min()


def most_frequent(df, column):
    return df[column].value_counts().idxmax()
def sum_value(df, column):

    return df[column].sum()


def count_values(df, column):

    return df[column].count()


def median_value(df, column):

    return df[column].median()


def unique_count(df, column):

    return df[column].nunique()


def count_by_category(df, column):
    return df[column].value_counts()
def get_column_information(df):

    numerical_columns = df.select_dtypes(
        include="number"
    ).columns.tolist()

    categorical_columns = df.select_dtypes(
        include="object"
    ).columns.tolist()

    return {
        "numerical_columns": numerical_columns,
        "categorical_columns": categorical_columns
    }
def clean_dataset(df):

    # Remove completely empty rows
    df = df.dropna(how="all")

    # Remove completely empty columns
    df = df.dropna(axis=1, how="all")

    # Remove duplicate rows
    df = df.drop_duplicates()

    # Try to convert text columns to numeric
    for column in df.columns:

        if df[column].dtype == "object":

            converted = pd.to_numeric(
                df[column],
                errors="coerce"
            )

            if converted.notna().mean() > 0.8:

                df[column] = converted

    return df