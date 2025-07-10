import sys
import runpy
from pathlib import Path


def test_bootstrap_adds_project_root_to_syspath(tmp_path, monkeypatch):
    # Create a fake project root with pyproject.toml
    project_root = tmp_path / "myproject"
    project_root.mkdir()
    (project_root / "pyproject.toml").write_text("[tool.poetry]\nname = 'test'")
    subdir = project_root / "notebooks"
    subdir.mkdir()
    script_path = project_root / "bootstrap.py"
    script_path.write_text(
        "import sys\n"
        "from pathlib import Path\n"
        "for parent in [Path.cwd()] + list(Path.cwd().parents):\n"
        "    if (parent / 'pyproject.toml').exists():\n"
        "        sys.path.insert(0, str(parent))\n"
        "        break\n"
    )

    # Change working directory to subdir and clear sys.path
    monkeypatch.chdir(subdir)
    root_str = str(project_root.resolve())
    if root_str in sys.path:
        sys.path.remove(root_str)

    # Run bootstrap.py as if with %run
    runpy.run_path(str(script_path))

    assert root_str in sys.path
