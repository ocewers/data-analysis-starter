import os
import sys
import tempfile
from pathlib import Path
import pytest

SUBDIRECTORY_LEVEL = 1  # Adjust this if the structure changes
sys.path.append(str(Path(__file__).resolve().parents[SUBDIRECTORY_LEVEL]))
from config import _ensure_project_root


def test_ensure_project_root_finds_marker(tmp_path, monkeypatch):
    # Create a fake project structure
    project_root = tmp_path / "myproject"
    project_root.mkdir()
    marker = project_root / "pyproject.toml"
    marker.write_text("[tool.poetry]\nname = 'test'")
    subdir = project_root / "subdir"
    subdir.mkdir()
    monkeypatch.chdir(subdir)

    # Remove project_root from sys.path if present
    root_str = str(project_root.resolve())
    if root_str in sys.path:
        sys.path.remove(root_str)

    found_root = _ensure_project_root("pyproject.toml")
    assert found_root == project_root
    assert root_str in sys.path


def test_ensure_project_root_raises(tmp_path, monkeypatch):
    # No marker file in this temp dir
    monkeypatch.chdir(tmp_path)
    with pytest.raises(FileNotFoundError):
        _ensure_project_root("pyproject.toml")
