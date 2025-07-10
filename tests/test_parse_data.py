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
    # Load the CSV file into a DataFrame
    testdata = pd.read_csv(TESTS_DIR / "data" / "testdata.csv", engine="pyarrow")

    # Store testdata as Parquet file
    testdata.to_parquet(OUTPUT_DIR / "testdata.parquet", engine="pyarrow")

    # Drop current testdata and reload from Parquet, dtype_backend = 'pyarrow' can be used instead of Numpy
    testdata = pd.read_parquet(OUTPUT_DIR / "testdata.parquet", engine="pyarrow")


def test_parse_data():
    assert parse_data() is None
