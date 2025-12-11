# Notebooks Directory

This directory is for **Jupyter notebooks** used in your data analysis.

## 🚨 Gitignore Behavior

- **In this template repository**: Notebooks are gitignored (except test notebooks)
- **In your team repository**: You should **commit notebooks** to share analysis with your team

See [TEAM_SETUP.md](../TEAM_SETUP.md) for instructions on configuring git for team collaboration.

## 📓 What Goes Here

Your analysis notebooks:

```
notebooks/
├── 01-exploration/
│   ├── initial-data-exploration.ipynb
│   └── data-quality-check.ipynb
├── 02-cleaning/
│   ├── data-cleaning.ipynb
│   └── outlier-detection.ipynb
├── 03-analysis/
│   ├── customer-segmentation.ipynb
│   ├── sales-analysis.ipynb
│   └── trend-analysis.ipynb
└── 04-reporting/
    └── final-report.ipynb
```

## 📝 Best Practices

### Notebook Organization

1. **Use numbered prefixes** to indicate order of execution
2. **One purpose per notebook** - keep notebooks focused
3. **Use descriptive names** that explain what the notebook does
4. **Group related notebooks** in subdirectories

### Notebook Content

1. **Add markdown documentation**:
   - Explain the purpose at the top
   - Document key findings
   - Add comments for complex code

2. **Keep notebooks clean**:
   - Remove debugging cells before committing
   - Clear output for large dataframes (optional)
   - Restart kernel and run all cells before sharing

3. **Import from src/ modules**:
   ```python
   from config import DATA_DIR, OUTPUT_DIR
   import pandas as pd
   
   # Import custom functions from src/
   import sys
   sys.path.append(str(DATA_DIR.parent / "src"))
   from data_processing import clean_data
   ```

4. **Use the config system**:
   ```python
   from config import DATA_DIR, OUTPUT_DIR
   
   # Read data
   df = pd.read_csv(DATA_DIR / "input.csv")
   
   # Save results
   df.to_csv(OUTPUT_DIR / "results.csv")
   ```

## 🔄 Version Control Tips

### Reducing Merge Conflicts

1. **Communicate with team** about who's working on which notebooks
2. **Use separate notebooks** for individual exploration
3. **Merge insights** into shared notebooks after discussion
4. **Use branches** for experimental analysis

### Handling Notebook Outputs

You can optionally strip outputs before committing to reduce file size and conflicts:

```bash
# Clear outputs manually
jupyter nbconvert --clear-output --inplace notebooks/**/*.ipynb

# Or use nbstripout for automatic clearing
pip install nbstripout
nbstripout --install
```

### Collaboration Workflow

1. **Pull before starting**:
   ```bash
   git pull
   ```

2. **Work on your notebook**

3. **Commit with clear message**:
   ```bash
   git add notebooks/my-analysis.ipynb
   git commit -m "Add customer churn analysis"
   git push
   ```

## 🔗 Related Documentation

- Main README: [../README.md](../README.md)
- Team Setup Guide: [../TEAM_SETUP.md](../TEAM_SETUP.md)
- Source Code Directory: [../src/README.md](../src/README.md)
