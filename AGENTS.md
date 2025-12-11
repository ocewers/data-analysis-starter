# Data Analysis Starter – Agent Guide

## Start Here
- Activate the uv-managed environment: run `uv sync` once, then prefix commands with `uv run`.
- Core path helpers live in `config.py`; import `DATA_DIR`, `OUTPUT_DIR`, `NOTEBOOKS_DIR`, `SRC_DIR`, and `TESTS_DIR` instead of hard-coding filesystem locations.
- `bootstrap.py` is legacy for notebooks using `%run`; new code should import directly from `config`, as illustrated in `example_simple_usage.py`.

## Architecture & Paths
- `config.py` auto-detects `pyproject.toml`, prepends the project root to `sys.path`, and eagerly loads `.env` when `python-dotenv` is installed—leverage environment variables for overrides instead of editing code.
- Library code belongs in `src/`; notebooks under `notebooks/` are treated as clients by the pipeline grapher in `utils/pipeline_graph.py`.
- Tests in `tests/test_config_file.py` and `tests/test_config_env.py` enforce that directory constants exist and remain reloadable after environment changes; preserve that behavior when extending configuration.

## Data I/O Patterns
- Route every read/write through the path constants from `config`; bypassing them breaks environment overrides and the dependency graph.
- Use pandas with the `pyarrow` engine (`pd.read_csv(..., engine="pyarrow")`, `.to_parquet(..., engine="pyarrow")`) to stay compatible with `tests/test_parse_data.py`.
- If you introduce new notebook helpers for file access, extend `READ_PATTERNS` / `WRITE_PATTERNS` and possibly `DependencyVisitor` in `utils/pipeline_graph.py` so generated graphs keep tracking the files.

## Core Workflows
- Run the full test suite with `uv run pytest`; it touches the real `data/`, `output/`, and `tests/` directories, so keep those folders available locally.
- Regenerate the notebook ⇄ data Mermaid graph with `python utils/pipeline_graph.py --root . --out output/pipeline.mmd` and commit the refreshed `output/pipeline.mmd` when notebooks change.
- For quick path sanity checks, run `uv run python example_simple_usage.py` to see resolved directories and a sample CSV → Parquet round trip.

## Gotchas & Housekeeping
- `tests/test_parse_data.py` writes `OUTPUT_DIR/testdata.parquet`; clean or reuse that file if your workflow creates other outputs in the same location.
- Several tests manipulate `sys.path` via `ROOT_LEVELS_UP`; adjust those constants if you relocate test files deeper in the tree.
- Maintain ASCII filenames/paths unless there is a strong reason otherwise; the repository relies on simple path joins across platforms.
- When adding new config surface area, mirror the coverage in `tests/test_config_env.py` to confirm environment overrides continue to work.
