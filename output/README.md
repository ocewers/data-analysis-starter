# Output Directory

This directory is for **generated outputs and results** from your analysis.

## ⚠️ Important: Output Files Are Gitignored

By default, all output files in this directory are **excluded from git** to prevent committing large generated files.

The `.gitignore` file excludes:
- All files in the output directory
- Images (PNG, JPG, etc.)
- PDFs and other report formats
- Processed data files

## 📁 What Goes Here

Store generated outputs from your analysis:

```
output/
├── figures/                # Generated charts and visualizations
│   ├── customer_distribution.png
│   ├── sales_trends.png
│   └── correlation_matrix.png
├── reports/               # Generated reports
│   ├── weekly_summary.pdf
│   └── monthly_analysis.html
├── processed_data/        # Intermediate processed datasets
│   ├── features.parquet
│   └── aggregated_results.csv
└── models/                # Saved ML models
    ├── model_v1.pkl
    └── model_v2.joblib
```

## 💾 Saving Outputs

Use the `OUTPUT_DIR` from config:

```python
from config import OUTPUT_DIR
import pandas as pd
import matplotlib.pyplot as plt

# Save a figure
plt.figure()
plt.plot(data)
plt.savefig(OUTPUT_DIR / "my_plot.png")

# Save processed data
df.to_csv(OUTPUT_DIR / "processed_data.csv", index=False)
df.to_parquet(OUTPUT_DIR / "processed_data.parquet")

# Save a report
with open(OUTPUT_DIR / "report.txt", "w") as f:
    f.write("Analysis Results\n")
    f.write(f"Mean: {df['value'].mean()}\n")
```

## 🔒 For Team Projects

Output files are typically **not committed** to git because:

1. **They're regenerated** - can be recreated by running notebooks
2. **They're large** - images and data files increase repo size
3. **They change frequently** - creates unnecessary git history
4. **They may contain sensitive info** - processed data might be sensitive

### When to Share Outputs

If you need to share outputs with your team:

1. **Share final reports manually**:
   - Email, Slack, or shared drive
   - Consider using a separate reports repository

2. **Document how to regenerate**:
   - Include instructions in notebooks
   - Make sure notebooks are reproducible

3. **Use external storage**:
   - Cloud storage (S3, GCS, Azure)
   - Shared network drives
   - Artifact repositories

4. **Exception: Documentation images**:
   - Keep key figures for documentation in a `docs/` folder
   - Commit documentation images (these are usually small and static)

## 🧹 Managing Output Files

### Cleaning Up

Periodically clean old output files:

```bash
# Delete all files but keep directory structure
find output -type f ! -name 'README.md' ! -name '.gitkeep' -delete

# Or delete everything except markers
rm -rf output/*
```

### Organizing by Date

Consider organizing outputs by date for long-running projects:

```python
from config import OUTPUT_DIR
from datetime import datetime

# Create date-based subdirectory
today = datetime.now().strftime("%Y-%m-%d")
output_dir = OUTPUT_DIR / today
output_dir.mkdir(exist_ok=True)

# Save outputs
df.to_csv(output_dir / "results.csv")
```

## 💡 Best Practices

1. **Use descriptive names** - `customer_churn_analysis_2025.png` not `output1.png`
2. **Include dates** - `sales_report_2025-01-15.pdf` for time-sensitive outputs
3. **Organize by type** - separate figures, reports, and data
4. **Document in notebooks** - explain what outputs are generated
5. **Make reproducible** - ensure notebooks can regenerate outputs
6. **Clean regularly** - remove old/unnecessary outputs

## 🔗 Configuration

The `OUTPUT_DIR` path can be customized using environment variables. See the main README for details on using `.env` files to set custom output locations.

## 📊 Alternative: Separate Output Locations

For team projects, you might want separate output locations:

```bash
# .env file
OUTPUT_DIR=/mnt/shared/project-outputs
```

This allows:
- Shared access to outputs
- Separate storage from code repository
- Better organization for large outputs
- Easier cleanup and archiving

## 🔗 Related Documentation

- Main README: [../README.md](../README.md)
- Team Setup Guide: [../TEAM_SETUP.md](../TEAM_SETUP.md)
- Configuration: [../config.py](../config.py)
