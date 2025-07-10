# config.py (in project root)
import sys
from pathlib import Path


def _ensure_project_root(marker: str = "pyproject.toml") -> Path:
    """
    Locate the project root by walking upward from the current working directory.
    Adds it to sys.path so modules like `config` can be imported globally.
    """
    cwd = Path.cwd().resolve()
    for parent in [cwd] + list(cwd.parents):
        if (parent / marker).exists():
            root_str = str(parent)
            if root_str not in sys.path:
                sys.path.insert(0, root_str)
            return parent
    raise FileNotFoundError(f"Could not find project root by looking for '{marker}'")


# ✅ Automatically inject root into sys.path every time config.py is imported
PROJECT_ROOT = _ensure_project_root()

# Base folders
DATA_DIR = PROJECT_ROOT / "data"
OUTPUT_DIR = PROJECT_ROOT / "output"
NOTEBOOKS_DIR = PROJECT_ROOT / "notebooks"
SRC_DIR = PROJECT_ROOT / "src"
TESTS_DIR = PROJECT_ROOT / "tests"
