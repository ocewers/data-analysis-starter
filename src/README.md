# Source Code Directory

This directory is for **reusable Python modules and scripts** that support your data analysis.

## 🚨 Gitignore Behavior

- **In this template repository**: Source files are gitignored
- **In your team repository**: You should **commit source code** to share with your team

See [TEAM_SETUP.md](../TEAM_SETUP.md) for instructions on configuring git for team collaboration.

## 📦 What Goes Here

Reusable Python modules and scripts:

```
src/
├── __init__.py              # Makes this a Python package
├── data_processing.py       # Data cleaning and transformation
├── feature_engineering.py   # Feature creation functions
├── visualization.py         # Plotting utilities
├── models.py               # Model training and evaluation
└── utils/
    ├── __init__.py
    ├── file_io.py          # File reading/writing helpers
    └── validation.py       # Data validation functions
```

## 🎯 Purpose

The `src/` directory helps you:

1. **Avoid code duplication** across notebooks
2. **Make code testable** with unit tests
3. **Improve code quality** through modular design
4. **Share functionality** across team members
5. **Maintain consistency** in data processing

## 📝 Best Practices

### Module Organization

1. **Group related functions** in the same module
2. **Use clear, descriptive names** for modules and functions
3. **Add docstrings** to all functions
4. **Keep modules focused** on a single responsibility

### Example Module Structure

```python
# src/data_processing.py
"""
Data processing utilities for customer analysis project.
"""

import pandas as pd
from pathlib import Path
from config import DATA_DIR

def load_customer_data(filename: str) -> pd.DataFrame:
    """
    Load customer data from the data directory.
    
    Args:
        filename: Name of the file in the data directory
        
    Returns:
        DataFrame with customer data
    """
    filepath = DATA_DIR / filename
    return pd.read_csv(filepath)

def clean_customer_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean customer data by removing duplicates and handling nulls.
    
    Args:
        df: Raw customer DataFrame
        
    Returns:
        Cleaned DataFrame
    """
    df = df.drop_duplicates()
    df = df.dropna(subset=['customer_id'])
    return df
```

### Using Modules in Notebooks

Import your modules directly in notebooks:

```python
# In a notebook
from config import DATA_DIR, OUTPUT_DIR
import pandas as pd

# Import your custom modules
from src.data_processing import load_customer_data, clean_customer_data
from src.visualization import plot_distribution

# Use them
df = load_customer_data("customers.csv")
df_clean = clean_customer_data(df)
plot_distribution(df_clean, "age")
```

### Alternative Import Pattern

If direct imports don't work, add src to path:

```python
import sys
from pathlib import Path

# Add src to path
project_root = Path.cwd()
while not (project_root / "pyproject.toml").exists():
    if project_root == project_root.parent:
        raise FileNotFoundError("Could not find pyproject.toml in any parent directory")
    project_root = project_root.parent
sys.path.insert(0, str(project_root / "src"))

# Now import
from data_processing import load_customer_data
```

## 🧪 Testing Your Code

Write tests for your src/ modules in the `tests/` directory:

```python
# tests/test_data_processing.py
import pytest
import pandas as pd
from src.data_processing import clean_customer_data

def test_clean_removes_duplicates():
    df = pd.DataFrame({
        'customer_id': [1, 1, 2],
        'name': ['Alice', 'Alice', 'Bob']
    })
    result = clean_customer_data(df)
    assert len(result) == 2

def test_clean_removes_null_ids():
    df = pd.DataFrame({
        'customer_id': [1, None, 2],
        'name': ['Alice', 'Charlie', 'Bob']
    })
    result = clean_customer_data(df)
    assert len(result) == 2
```

Run tests with:
```bash
uv run pytest
```

## 💡 When to Move Code to src/

Move code from notebooks to `src/` when:

1. **You use it in multiple notebooks**
2. **It's complex** and would benefit from testing
3. **It's stable** and unlikely to change frequently
4. **It represents business logic** that should be reusable
5. **You want to enforce code quality** through reviews

## 🔄 Development Workflow

1. **Start in notebooks** - prototype and explore
2. **Identify reusable code** - functions used multiple times
3. **Move to src/** - create modules for shared functionality
4. **Write tests** - ensure code works correctly
5. **Import in notebooks** - use your modules
6. **Refactor and improve** - iterate on your modules

## 📚 Example Modules to Create

Common modules for data analysis projects:

- **data_processing.py** - Loading, cleaning, transforming data
- **feature_engineering.py** - Creating features for modeling
- **visualization.py** - Standard plots and charts
- **statistical_tests.py** - Hypothesis testing, correlations
- **metrics.py** - Custom metrics and KPIs
- **database.py** - Database connections and queries
- **api_client.py** - API interactions
- **config_loader.py** - Configuration management

## 🔗 Related Documentation

- Main README: [../README.md](../README.md)
- Team Setup Guide: [../TEAM_SETUP.md](../TEAM_SETUP.md)
- Notebooks Directory: [../notebooks/README.md](../notebooks/README.md)
- Tests Directory: [../tests/](../tests/)
