# 🧪 Data Analysis Starter Kit

This is a quick-start boilerplate for data analysis using:

- **[VS Code](https://code.visualstudio.com/)**
- **[uv](https://github.com/astral-sh/uv)** for package and environment management
- **Jupyter Notebooks** for exploration
- **[Data Wrangler](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.vscode-jupyter-datawrangler)** for visual data transformation

Everything is configured to work with minimal setup.

---

## ✅ Prerequisites

### 1. Install VS Code

- Download and install from: [https://code.visualstudio.com/](https://code.visualstudio.com/)

### 2. Install the Data Wrangler extension

- Open VS Code.
- Go to Extensions (`Ctrl+Shift+X` or `Cmd+Shift+X`).
- Search for `Data Wrangler` and install it.

### 3. Install `uv`

Detailed instructions: [https://docs.astral.sh/uv/getting-started/installation/](https://docs.astral.sh/uv/getting-started/installation/)

#### On macOS / Linux

```sh
curl -LsSf https://astral.sh/uv/install.sh | sh
```

#### On Windows (PowerShell)

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

---

## 🚀 Clone and Set Up the Project

### 1. Clone this repo

```sh
git clone https://github.com/ocewers/data-analysis-starter.git
cd data-analysis-starter
```

### 2. Sync the environment and install dependencies

```sh
uv sync
```

This will:

- Create a local `.venv`
- Install all dependencies from `pyproject.toml`

---

## 🧭 Open in VS Code

1. Open the folder in VS Code:

```sh
code .
```

2. VS Code should auto-detect the `.venv` and activate it.
3. Open the test notebook: `test/test.ipynb`
4. Run cells to confirm the environment is working.
5. Try right-clicking a `DataFrame` output and select **Open in Data Wrangler**.

---

## 📁 Project Structure

```text
.
├── .vscode/               # VS Code settings for environment + Jupyter
│   └── settings.json
├── data/                  # Local data files (ignored in git)
├── test/                  # Sample notebook and CSV
│   ├── test.ipynb
│   └── testdata.csv
├── .gitignore             # Includes .venv, data/, __pycache__, etc.
├── .python-version        # Optional version pinning (e.g. for pyenv)
├── pyproject.toml         # Project dependencies and metadata
├── uv.lock                # Exact locked versions
└── README.md
```

---

## 🛠 Tips & Troubleshooting

### Interpreter not selected?

- Open Command Palette (`Ctrl+Shift+P` / `Cmd+Shift+P`)
- Type: `Python: Select Interpreter`
- Choose the one pointing to `.venv`

### Jupyter not working?

- Make sure you opened the repo **after** running `uv sync`
- Check the Python extension is installed

### Data Wrangler not appearing?

- Make sure the extension is installed.
- Try restarting VS Code if it doesn't show on right-click.

---

You're now ready to explore and analyze data! 🎉
