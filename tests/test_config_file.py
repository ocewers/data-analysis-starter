# test_config_file.py
# This file is used to ensure that the config.py file can be imported correctly
# and that the project root is set up properly.

import sys
from pathlib import Path

SUBDIRECTORY_LEVEL = 1  # Adjust this if the structure changes
sys.path.append(str(Path(__file__).resolve().parents[SUBDIRECTORY_LEVEL]))
import config


# print all variables in config.py
def test_config_variables():
    assert hasattr(config, "PROJECT_ROOT"), "PROJECT_ROOT is not defined in config.py"
    assert hasattr(config, "DATA_DIR"), "DATA_DIR is not defined in config.py"
    assert hasattr(config, "OUTPUT_DIR"), "OUTPUT_DIR is not defined in config.py"
    assert hasattr(config, "NOTEBOOKS_DIR"), "NOTEBOOKS_DIR is not defined in config.py"
    assert hasattr(config, "SRC_DIR"), "SRC_DIR is not defined in config.py"
    assert hasattr(config, "TESTS_DIR"), "TESTS_DIR is not defined in config.py"

    # Check that the paths are correct
    assert config.PROJECT_ROOT.is_dir(), (
        f"PROJECT_ROOT {config.PROJECT_ROOT} does not exist"
    )
    assert config.DATA_DIR.is_dir(), f"DATA_DIR {config.DATA_DIR} does not exist"
    assert config.OUTPUT_DIR.is_dir(), f"OUTPUT_DIR {config.OUTPUT_DIR} does not exist"
    assert config.NOTEBOOKS_DIR.is_dir(), (
        f"NOTEBOOKS_DIR {config.NOTEBOOKS_DIR} does not exist"
    )
    assert config.SRC_DIR.is_dir(), f"SRC_DIR {config.SRC_DIR} does not exist"
    assert config.TESTS_DIR.is_dir(), f"TESTS_DIR {config.TESTS_DIR} does not exist"

    # Print the variables for debugging
    print("PROJECT_ROOT:", config.PROJECT_ROOT)
    print("DATA_DIR:", config.DATA_DIR)
    print("OUTPUT_DIR:", config.OUTPUT_DIR)
    print("NOTEBOOKS_DIR:", config.NOTEBOOKS_DIR)
    print("SRC_DIR:", config.SRC_DIR)
    print("TESTS_DIR:", config.TESTS_DIR)
