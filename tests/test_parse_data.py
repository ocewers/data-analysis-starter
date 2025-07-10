# test_parse_data.py
# This file is used to test parsing data from a CSV and store as Parquet files


import sys
from pathlib import Path

SUBDIRECTORY_LEVEL = 1  # Adjust this if the structure changes
sys.path.append(str(Path(__file__).resolve().parents[SUBDIRECTORY_LEVEL]))

# Import the configuration for directories
from config import TESTS_DIR, OUTPUT_DIR

import pandas as pd


def parse_data():
    """Load CSV test data, save and reload as Parquet."""
    csv_path = TESTS_DIR / "data" / "testdata.csv"
    parquet_path = OUTPUT_DIR / "testdata.parquet"

    # Load the CSV file into a DataFrame
    testdata = pd.read_csv(csv_path, engine="pyarrow")

    # Store testdata as Parquet file
    testdata.to_parquet(parquet_path, engine="pyarrow")

    # Reload from Parquet and return
    return pd.read_parquet(parquet_path, engine="pyarrow")


def test_parse_data():
    df_parquet = parse_data()

    # Parquet file should exist
    parquet_path = OUTPUT_DIR / "testdata.parquet"
    assert parquet_path.is_file()

    # Data loaded from Parquet should match the original CSV
    df_csv = pd.read_csv(TESTS_DIR / "data" / "testdata.csv", engine="pyarrow")
    pd.testing.assert_frame_equal(df_parquet, df_csv)
