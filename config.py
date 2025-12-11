# config.py (in project root)
import os
import sys
from pathlib import Path


def _find_project_root(marker: str = "pyproject.toml") -> Path:
    """
    Locate the project root by walking upward from the current working directory.
    Returns the project root path.
    """
    # First check if PROJECT_ROOT is set via environment variable
    env_root = os.getenv("PROJECT_ROOT")
    if env_root:
        root_path = Path(env_root).resolve()
        if root_path.exists():
            return root_path
    
    # Otherwise, search for the marker file
    cwd = Path.cwd().resolve()
    for parent in [cwd] + list(cwd.parents):
        if (parent / marker).exists():
            return parent
    
    raise FileNotFoundError(
        f"Could not find project root by looking for '{marker}'. "
        f"Set PROJECT_ROOT environment variable to specify the project root."
    )


def _ensure_project_root(marker: str = "pyproject.toml") -> Path:
    """
    Locate the project root and add it to sys.path.
    Maintains backward compatibility with the old function.
    """
    root = _find_project_root(marker)
    root_str = str(root)
    if root_str not in sys.path:
        sys.path.insert(0, root_str)
    return root


# ✅ Find and set up project root first (before anything else)
PROJECT_ROOT = _ensure_project_root()

# Try to load .env file if python-dotenv is available
try:
    from dotenv import load_dotenv
    # Look for .env file in project root
    dotenv_path = PROJECT_ROOT / ".env"
    if dotenv_path.exists():
        load_dotenv(dotenv_path)
except ImportError:
    # python-dotenv not installed, skip .env file loading
    pass


def _get_path_from_env(env_var: str, default_relative: str) -> Path:
    """
    Get a directory path from environment variable or use default relative to project root.
    
    Args:
        env_var: Environment variable name (e.g., 'DATA_DIR')
        default_relative: Default path relative to project root (e.g., 'data')
    
    Returns:
        Absolute Path object
    """
    env_value = os.getenv(env_var)
    if env_value:
        path = Path(env_value)
        # If path is relative, make it relative to project root
        if not path.is_absolute():
            return (PROJECT_ROOT / path).resolve()
        return path.resolve()
    
    # Use default relative to project root
    return PROJECT_ROOT / default_relative


# Base folders - can be overridden by environment variables
DATA_DIR = _get_path_from_env("DATA_DIR", "data")
OUTPUT_DIR = _get_path_from_env("OUTPUT_DIR", "output")
NOTEBOOKS_DIR = _get_path_from_env("NOTEBOOKS_DIR", "notebooks")
SRC_DIR = _get_path_from_env("SRC_DIR", "src")
TESTS_DIR = _get_path_from_env("TESTS_DIR", "tests")
