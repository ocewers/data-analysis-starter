# bootstrap.py (in project root)
# 
# NOTE: This file is now OPTIONAL and maintained for backward compatibility.
# 
# The new approach (recommended):
#   from config import DATA_DIR, OUTPUT_DIR
# 
# The old approach (still works):
#   %run ../../bootstrap.py
#   from config import DATA_DIR, OUTPUT_DIR
#
# Both approaches work because config.py now automatically handles
# project root detection and sys.path setup.

import sys
from pathlib import Path

for parent in [Path.cwd()] + list(Path.cwd().parents):
    if (parent / "pyproject.toml").exists():
        sys.path.insert(0, str(parent))
        break
