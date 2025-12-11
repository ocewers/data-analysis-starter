#!/usr/bin/env python3
"""
Example: Simple usage of the new configuration system

This script demonstrates how easy it is to use the config module
without any manual sys.path manipulation or bootstrap scripts.
"""

# No need for sys.path manipulation!
# Just import config directly
from config import DATA_DIR, OUTPUT_DIR, TESTS_DIR

import pandas as pd


def main():
    """Demonstrate simple config usage."""
    print("📁 Project Paths:")
    print(f"  DATA_DIR: {DATA_DIR}")
    print(f"  OUTPUT_DIR: {OUTPUT_DIR}")
    print(f"  TESTS_DIR: {TESTS_DIR}")
    print()
    
    # Example: Read test data
    test_csv = TESTS_DIR / "data" / "testdata.csv"
    if test_csv.exists():
        print(f"✅ Reading: {test_csv}")
        df = pd.read_csv(test_csv)
        print(f"   Shape: {df.shape}")
        print(f"   Columns: {list(df.columns)}")
        print()
        
        # Example: Write to output
        output_file = OUTPUT_DIR / "example_output.parquet"
        df.to_parquet(output_file)
        print(f"✅ Written: {output_file}")
    else:
        print(f"⚠️  Test file not found: {test_csv}")


if __name__ == "__main__":
    main()
