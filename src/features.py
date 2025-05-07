import os
import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Base path = project root
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def load_data(file_name: str) -> pd.DataFrame:
    full_path = os.path.join(BASE_DIR, "data", "raw", file_name)
    return pd.read_csv(full_path)


def fill_missing_values_by_type(df: pd.DataFrame):
    """Fill numerics and categoricals missing values."""
    # numerics columns
    num_cols = df.select_dtypes(include=["float64", "int64"]).columns

    df[num_cols] = df[num_cols].fillna(-999)

    # texts columns
    cat_cols = df.select_dtypes(include=["object", "string"]).columns
    df[cat_cols] = df[cat_cols].fillna("missing")


def label_encode_text_columns(df: pd.DataFrame) -> pd.DataFrame:
    """Encode all categorical text columns in the dataframe."""
    cat_cols = df.select_dtypes(include=["object", "string"]).columns

    for col in cat_cols:
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col])

    return df


def save_processed_data(df: pd.DataFrame, file_name: str) -> pd.DataFrame:
    """save processed data to csv file"""
    full_path = os.path.join(BASE_DIR, "data", "processed", file_name)
    df.to_csv(full_path, index=False)


def prepare_features_dataset() -> pd.DataFrame:
    """Return a DataFrame with the features.
    The features are the columns of the merged transaction and identity
    dataframes.
    """
    # Read the transaction and identity dataframes
    df_transactions = load_data("train_transaction.csv")
    df_identity = load_data("train_identity.csv")

    # Merge the two dataframes on the TransactionID
    df = df_transactions.merge(df_identity, on="TransactionID", how="left")
    print(f"[INFO] Merged data shape: {df.shape}")

    fill_missing_values_by_type(df)
    print("[INFO] Missing values filled.")

    # Encode categorical columns in the df
    label_encode_text_columns(df)
    print("[INFO] Categorical columns encoded.")

    # save processed data
    save_processed_data(df, "train_processed.csv")
    print("[INFO] Processed data saved.")


if __name__ == "__main__":
    prepare_features_dataset()
