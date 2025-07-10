# bootstrap.py (in project root)
import sys
from pathlib import Path

for parent in [Path.cwd()] + list(Path.cwd().parents):
    if (parent / "pyproject.toml").exists():
        sys.path.insert(0, str(parent))
        break
