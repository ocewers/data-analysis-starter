# test_config_env.py
# Test environment variable configuration for config.py

import os
import sys
from pathlib import Path
import pytest


def test_env_variable_overrides_data_dir(tmp_path, monkeypatch):
    """Test that DATA_DIR can be overridden by environment variable."""
    # Create a fake project structure
    project_root = tmp_path / "myproject"
    project_root.mkdir()
    marker = project_root / "pyproject.toml"
    marker.write_text("[tool.poetry]\nname = 'test'")
    
    # Create custom data directory
    custom_data = tmp_path / "custom_data"
    custom_data.mkdir()
    
    # Set environment variable
    monkeypatch.setenv("DATA_DIR", str(custom_data))
    monkeypatch.chdir(project_root)
    
    # Remove project_root from sys.path if present
    root_str = str(project_root.resolve())
    if root_str in sys.path:
        sys.path.remove(root_str)
    
    # Need to reload the config module to pick up env changes
    import importlib
    if 'config' in sys.modules:
        importlib.reload(sys.modules['config'])
    else:
        sys.path.append(str(project_root.resolve()))
        import config
        importlib.reload(config)
    
    import config
    assert config.DATA_DIR == custom_data.resolve()


def test_env_variable_relative_path(tmp_path, monkeypatch):
    """Test that relative paths in env variables are resolved relative to project root."""
    # Create a fake project structure
    project_root = tmp_path / "myproject"
    project_root.mkdir()
    marker = project_root / "pyproject.toml"
    marker.write_text("[tool.poetry]\nname = 'test'")
    
    # Create custom subdirectory
    custom_dir = project_root / "my_custom_output"
    custom_dir.mkdir()
    
    # Set environment variable with relative path
    monkeypatch.setenv("OUTPUT_DIR", "my_custom_output")
    monkeypatch.chdir(project_root)
    
    # Remove project_root from sys.path if present
    root_str = str(project_root.resolve())
    if root_str in sys.path:
        sys.path.remove(root_str)
    
    # Reload config
    import importlib
    if 'config' in sys.modules:
        importlib.reload(sys.modules['config'])
    else:
        sys.path.append(str(project_root.resolve()))
        import config
        importlib.reload(config)
    
    import config
    assert config.OUTPUT_DIR == custom_dir.resolve()


def test_project_root_env_variable(tmp_path, monkeypatch):
    """Test that PROJECT_ROOT can be set via environment variable."""
    # Create a fake project structure
    project_root = tmp_path / "myproject"
    project_root.mkdir()
    marker = project_root / "pyproject.toml"
    marker.write_text("[tool.poetry]\nname = 'test'")
    
    # Set PROJECT_ROOT environment variable
    monkeypatch.setenv("PROJECT_ROOT", str(project_root))
    
    # Change to a different directory
    other_dir = tmp_path / "other"
    other_dir.mkdir()
    monkeypatch.chdir(other_dir)
    
    # Remove project_root from sys.path if present
    root_str = str(project_root.resolve())
    if root_str in sys.path:
        sys.path.remove(root_str)
    
    # Reload config
    import importlib
    if 'config' in sys.modules:
        importlib.reload(sys.modules['config'])
    else:
        sys.path.append(str(project_root.resolve()))
        import config
        importlib.reload(config)
    
    import config
    assert config.PROJECT_ROOT == project_root.resolve()


def test_default_paths_without_env(tmp_path, monkeypatch):
    """Test that default paths work when no environment variables are set."""
    # Create a fake project structure
    project_root = tmp_path / "myproject"
    project_root.mkdir()
    marker = project_root / "pyproject.toml"
    marker.write_text("[tool.poetry]\nname = 'test'")
    
    # Create default directories
    for dirname in ["data", "output", "notebooks", "src", "tests"]:
        (project_root / dirname).mkdir()
    
    monkeypatch.chdir(project_root)
    
    # Clear any environment variables
    for var in ["PROJECT_ROOT", "DATA_DIR", "OUTPUT_DIR", "NOTEBOOKS_DIR", "SRC_DIR", "TESTS_DIR"]:
        monkeypatch.delenv(var, raising=False)
    
    # Remove project_root from sys.path if present
    root_str = str(project_root.resolve())
    if root_str in sys.path:
        sys.path.remove(root_str)
    
    # Reload config
    import importlib
    if 'config' in sys.modules:
        importlib.reload(sys.modules['config'])
    else:
        sys.path.append(str(project_root.resolve()))
        import config
        importlib.reload(config)
    
    import config
    assert config.PROJECT_ROOT == project_root
    assert config.DATA_DIR == project_root / "data"
    assert config.OUTPUT_DIR == project_root / "output"
    assert config.NOTEBOOKS_DIR == project_root / "notebooks"
    assert config.SRC_DIR == project_root / "src"
    assert config.TESTS_DIR == project_root / "tests"
