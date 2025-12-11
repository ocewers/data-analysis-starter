# test_config_env.py
# Test environment variable configuration for config.py

import os
import sys
from pathlib import Path
import pytest


@pytest.fixture
def reload_config(monkeypatch):
    """Helper fixture to reload config module with clean state."""
    def _reload(project_root: Path):
        """Reload config module ensuring it picks up new environment variables."""
        import importlib
        
        # Use monkeypatch for safer sys.path manipulation
        root_str = str(project_root.resolve())
        monkeypatch.syspath_prepend(root_str)
        
        # Reload the config module to pick up environment changes
        if 'config' in sys.modules:
            importlib.reload(sys.modules['config'])
        else:
            import config
            importlib.reload(config)
        
        return sys.modules['config']
    
    return _reload


def test_env_variable_overrides_data_dir(tmp_path, monkeypatch, reload_config):
    """Test that DATA_DIR can be overridden by environment variable."""
    # Create a fake project structure
    project_root = tmp_path / "myproject"
    project_root.mkdir()
    (project_root / "pyproject.toml").write_text("[tool.poetry]\nname = 'test'")
    
    # Create custom data directory
    custom_data = tmp_path / "custom_data"
    custom_data.mkdir()
    
    # Set environment variable
    monkeypatch.setenv("DATA_DIR", str(custom_data))
    monkeypatch.chdir(project_root)
    
    config = reload_config(project_root)
    assert config.DATA_DIR == custom_data.resolve()


def test_env_variable_relative_path(tmp_path, monkeypatch, reload_config):
    """Test that relative paths in env variables are resolved relative to project root."""
    # Create a fake project structure
    project_root = tmp_path / "myproject"
    project_root.mkdir()
    (project_root / "pyproject.toml").write_text("[tool.poetry]\nname = 'test'")
    
    # Create custom subdirectory
    custom_dir = project_root / "my_custom_output"
    custom_dir.mkdir()
    
    # Set environment variable with relative path
    monkeypatch.setenv("OUTPUT_DIR", "my_custom_output")
    monkeypatch.chdir(project_root)
    
    config = reload_config(project_root)
    assert config.OUTPUT_DIR == custom_dir.resolve()


def test_project_root_env_variable(tmp_path, monkeypatch, reload_config):
    """Test that PROJECT_ROOT can be set via environment variable."""
    # Create a fake project structure
    project_root = tmp_path / "myproject"
    project_root.mkdir()
    (project_root / "pyproject.toml").write_text("[tool.poetry]\nname = 'test'")
    
    # Set PROJECT_ROOT environment variable
    monkeypatch.setenv("PROJECT_ROOT", str(project_root))
    
    # Change to a different directory
    other_dir = tmp_path / "other"
    other_dir.mkdir()
    monkeypatch.chdir(other_dir)
    
    config = reload_config(project_root)
    assert config.PROJECT_ROOT == project_root.resolve()


def test_default_paths_without_env(tmp_path, monkeypatch, reload_config):
    """Test that default paths work when no environment variables are set."""
    # Create a fake project structure
    project_root = tmp_path / "myproject"
    project_root.mkdir()
    (project_root / "pyproject.toml").write_text("[tool.poetry]\nname = 'test'")
    
    # Create default directories
    for dirname in ["data", "output", "notebooks", "src", "tests"]:
        (project_root / dirname).mkdir()
    
    monkeypatch.chdir(project_root)
    
    # Clear any environment variables
    for var in ["PROJECT_ROOT", "DATA_DIR", "OUTPUT_DIR", "NOTEBOOKS_DIR", "SRC_DIR", "TESTS_DIR"]:
        monkeypatch.delenv(var, raising=False)
    
    config = reload_config(project_root)
    assert config.PROJECT_ROOT == project_root
    assert config.DATA_DIR == project_root / "data"
    assert config.OUTPUT_DIR == project_root / "output"
    assert config.NOTEBOOKS_DIR == project_root / "notebooks"
    assert config.SRC_DIR == project_root / "src"
    assert config.TESTS_DIR == project_root / "tests"
