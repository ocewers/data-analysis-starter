# Data Directory

This directory is for **source data files** used in your analysis.

## ⚠️ Important: Data Files Are Gitignored

By default, all data files in this directory are **excluded from git** to prevent accidentally committing sensitive or large data files.

The `.gitignore` file excludes:
- CSV, Excel, Parquet files
- Database files  
- All other common data formats

## 📁 What Goes Here

Place your raw data files in this directory:

```
data/
├── raw/                    # Original, immutable data
│   ├── customers.csv
│   ├── transactions.xlsx
│   └── products.parquet
├── processed/              # Cleaned, transformed data
│   ├── clean_customers.csv
│   └── aggregated_sales.parquet
└── external/               # Data from external sources
    └── market_data.csv
```

## 🔒 For Team Projects

When working in a team:

1. **Never commit actual data files** - they're gitignored for good reason
2. **Share data separately** via:
   - Shared network drives
   - Cloud storage (S3, GCS, Azure)
   - Database connections
   - Data versioning tools (DVC)

3. **Document your data sources** in your project README:
   - Where the data comes from
   - How to access it
   - Any preprocessing steps needed

4. **Use environment variables** for data paths:
   ```python
   from config import DATA_DIR
   df = pd.read_csv(DATA_DIR / "customers.csv")
   ```

## 💡 Tips

- Keep raw data immutable - don't modify original files
- Create subdirectories to organize different data sources
- Consider adding a `data_dictionary.md` to document your datasets
- For large datasets, consider using Parquet format for better performance

## 🔗 Configuration

The `DATA_DIR` path can be customized using environment variables. See the main README for details on using `.env` files to point to shared data locations.
