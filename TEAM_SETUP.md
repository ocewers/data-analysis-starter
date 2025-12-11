# 👥 Team Collaboration Setup Guide

This guide explains how to set up a **private repository** for your team based on this starter template. This is the recommended approach when working with sensitive data or sharing analysis notebooks and Python scripts within your team.

---

## 🎯 Why Create a Private Team Repository?

When working on data analysis projects with a team, you'll likely need to:

- **Share Jupyter notebooks** containing analysis code
- **Share Python scripts** and data processing pipelines  
- **Collaborate on source code** in the `src/` directory
- **Version control your work** while keeping sensitive data secure
- **Work with potentially sensitive data** that shouldn't be public

This starter template is designed to be **forked into a private repository** where your team can safely collaborate.

---

## 🚀 Quick Start: Create Your Team Repository

### Option 1: Use This Repository as a Template (Recommended)

1. **Navigate to this repository on GitHub**
   - Go to: https://github.com/ocewers/data-analysis-starter

2. **Click "Use this template"**
   - Click the green "Use this template" button at the top right
   - Select "Create a new repository"

3. **Configure your new repository**
   - **Owner**: Select your organization or personal account
   - **Repository name**: Choose a descriptive name (e.g., `customer-analysis-2025`)
   - **Description**: Add a description of your project
   - **Visibility**: Select **Private** ⚠️ (Important!)
   - Click "Create repository"

4. **Clone your new private repository**
   ```sh
   git clone https://github.com/YOUR-ORG/your-project-name.git
   cd your-project-name
   ```

5. **Set up the environment**
   ```sh
   uv sync
   ```

### Option 2: Fork and Make Private

1. **Fork this repository**
   - Click "Fork" at the top right of this repository
   - Select your account/organization

2. **Make the fork private**
   - Go to your forked repository
   - Click "Settings" → "General"
   - Scroll to "Danger Zone"
   - Click "Change visibility" → Select "Private"
   - Confirm the change

3. **Clone and set up** (same as above)

---

## 📁 What to Commit vs. What to Ignore

### ✅ What SHOULD Be Committed (Shared with Team)

The following should be committed to your team's private repository:

- **Notebooks** (`notebooks/`)
  - Analysis notebooks
  - Exploration notebooks
  - Documentation notebooks
  
- **Source code** (`src/`)
  - Reusable Python modules
  - Data processing functions
  - Analysis utilities

- **Configuration files**
  - `pyproject.toml` (dependencies)
  - `.python-version` (Python version)
  - Custom `.env.example` files (with example values)
  
- **Documentation**
  - README updates
  - Project-specific documentation

### ❌ What Should NOT Be Committed (Even in Private Repos)

The following should remain ignored (already in `.gitignore`):

- **Raw data files** (`data/`)
  - CSV, Excel, Parquet files
  - Database files
  - Any files with actual data

- **Output files** (`output/`)
  - Generated charts
  - Processed datasets
  - Exported reports

- **Environment files**
  - `.env` files (may contain secrets)
  - Credential files

- **Virtual environments**
  - `.venv/` directory
  - Python cache files

---

## 🔧 Configuring Your Team Repository

### Step 1: Update the `.gitignore`

The starter template comes with a conservative `.gitignore` that excludes notebooks, src, and other directories by default. **For your team repository, you'll want to track these files.**

1. **Copy the team-specific template**
   ```sh
   cp .gitignore.team-template .gitignore
   ```

2. **Review and customize** the `.gitignore` based on your needs

The team template includes:
- ✅ Tracks `notebooks/`, `src/` (for collaboration)
- ❌ Ignores `data/`, `output/` (sensitive/generated content)
- ❌ Ignores `.env` files (secrets)

### Step 2: Update the README

Update your repository's README to reflect your specific project:

```sh
# Edit README.md to include:
# - Project name and description
# - Team members
# - Data sources information (without exposing sensitive details)
# - Project-specific setup instructions
# - Links to key notebooks
```

### Step 3: Add Team Members

1. Go to your repository on GitHub
2. Click "Settings" → "Collaborators and teams"
3. Click "Add people" or "Add teams"
4. Add your team members with appropriate permissions:
   - **Write**: For contributors who will make changes
   - **Admin**: For team leads who will manage settings

---

## 🔒 Security Best Practices

### 1. Never Commit Sensitive Data

Even in a private repository, follow these rules:

- ❌ **No API keys** in code
- ❌ **No passwords** in notebooks
- ❌ **No actual data** files (use `.gitignore`)
- ❌ **No credentials** in `.env` or elsewhere

### 2. Use Environment Variables

Store sensitive configuration in `.env` files (which are gitignored):

```sh
# Copy the example
cp .env.example .env

# Edit .env with your actual values (NEVER commit this file)
# Example:
API_KEY=your_secret_key_here
DATABASE_URL=your_database_connection_string
```

### 3. Share Data Separately

Options for sharing data with your team:

- **Cloud storage**: AWS S3, Google Cloud Storage, Azure Blob Storage
- **Shared network drives**: Mount as `DATA_DIR` using `.env`
- **Data versioning tools**: DVC (Data Version Control)
- **Database connections**: Share connection strings via secure channels

Example `.env` for shared data location:
```sh
# .env (not committed)
DATA_DIR=/mnt/shared-drive/project-data
OUTPUT_DIR=/mnt/shared-drive/project-output
```

### 4. Use `.env.example` for Documentation

Document what environment variables your project needs:

```sh
# .env.example (committed to repo)
# Copy this to .env and fill in actual values

# Data Locations
DATA_DIR=/path/to/data
OUTPUT_DIR=/path/to/output

# API Keys (get from team lead)
API_KEY=your_api_key_here
DATABASE_URL=postgresql://user:password@host:port/database
```

---

## 👥 Team Workflow

### Initial Setup (Each Team Member)

1. **Clone the team repository**
   ```sh
   git clone https://github.com/YOUR-ORG/your-project-name.git
   cd your-project-name
   ```

2. **Install dependencies**
   ```sh
   uv sync
   ```

3. **Configure local environment**
   ```sh
   cp .env.example .env
   # Edit .env with your local paths and credentials
   ```

4. **Set up data access**
   - Ask team lead for data location
   - Configure `DATA_DIR` in your `.env` file
   - Verify access to shared data storage

### Daily Workflow

1. **Pull latest changes**
   ```sh
   git pull
   ```

2. **Work on your analysis**
   - Create/edit notebooks in `notebooks/`
   - Create/edit Python modules in `src/`

3. **Commit and push your work**
   ```sh
   git add notebooks/my_analysis.ipynb
   git add src/my_module.py
   git commit -m "Add customer segmentation analysis"
   git push
   ```

### Collaboration Best Practices

- **Use branches** for major changes or experiments
  ```sh
  git checkout -b analysis/customer-churn
  # Work on your branch
  git push -u origin analysis/customer-churn
  # Create a Pull Request on GitHub
  ```

- **Clear commit messages**: Describe what the analysis does
- **Document your notebooks**: Add markdown cells explaining your approach
- **Code reviews**: Review each other's Pull Requests
- **Regular syncs**: Pull changes frequently to avoid conflicts

---

## 📊 Working with Notebooks

### Notebook Organization

Recommended structure for `notebooks/`:

```
notebooks/
├── 01-data-exploration/
│   ├── explore-customer-data.ipynb
│   └── data-quality-check.ipynb
├── 02-feature-engineering/
│   ├── create-features.ipynb
│   └── feature-selection.ipynb
├── 03-modeling/
│   ├── baseline-model.ipynb
│   └── model-comparison.ipynb
└── 04-reporting/
    └── final-report.ipynb
```

### Notebook Tips

1. **Clear outputs before committing** (optional, reduces repo size):
   ```sh
   jupyter nbconvert --clear-output --inplace notebooks/**/*.ipynb
   ```

2. **Use version control friendly formats**:
   - Keep notebooks small and focused
   - Avoid very large outputs in cells
   - Consider using `nbstripout` for automatic output clearing

3. **Link notebooks to scripts**:
   - Move reusable code to `src/` modules
   - Import from `src/` in notebooks
   - Keep notebooks focused on analysis, not utilities

---

## 🔄 Keeping Up with Upstream Updates

If you want to incorporate updates from the original starter template:

1. **Add the upstream remote** (one-time setup)
   ```sh
   git remote add upstream https://github.com/ocewers/data-analysis-starter.git
   ```

2. **Fetch upstream changes**
   ```sh
   git fetch upstream
   ```

3. **Merge updates carefully**
   ```sh
   git merge upstream/main
   # Review changes and resolve conflicts
   ```

⚠️ **Note**: Only merge upstream changes if they're relevant to your project. Your team repository will diverge from the template, and that's expected!

---

## 🛠 Troubleshooting

### "I accidentally committed sensitive data"

If you committed actual data or secrets:

1. **Don't panic**, but act quickly
2. **Remove the sensitive file**:
   ```sh
   git rm --cached path/to/sensitive-file
   git commit -m "Remove sensitive file"
   ```

3. **For files in history**: Use `git filter-branch` or BFG Repo-Cleaner
4. **Rotate any exposed credentials** immediately
5. **Update `.gitignore`** to prevent it from happening again

### "Git says there are conflicts in notebooks"

Notebook conflicts can be tricky:

1. **Avoid conflicts**: Communicate with team about who's working on what
2. **If conflicts occur**: 
   - Use a tool like `nbdime` for notebook-aware diffing
   - Or manually resolve: pick one version, re-run cells

3. **Consider**: Using one notebook per team member for exploration, then merging insights into shared notebooks

### "The repository is getting too large"

If your repository grows too large:

1. **Check for accidentally committed data**:
   ```sh
   git rev-list --objects --all | \
     git cat-file --batch-check='%(objecttype) %(objectname) %(objectsize) %(rest)' | \
     awk '/^blob/ {print substr($0,6)}' | sort -n -k 2 | tail -20
   ```

2. **Remove large files from history** using BFG Repo-Cleaner
3. **Review `.gitignore`**: Make sure data and output files are excluded
4. **Consider Git LFS** for large but necessary files

---

## 📚 Additional Resources

- [GitHub Docs: Creating a Private Repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-new-repository)
- [GitHub Docs: Managing Access](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/managing-repository-settings/managing-teams-and-people-with-access-to-your-repository)
- [Git Best Practices](https://git-scm.com/book/en/v2/Distributed-Git-Contributing-to-a-Project)
- [Jupyter Notebook Best Practices](https://jupyter-notebook.readthedocs.io/en/stable/)

---

## ❓ Questions?

If you have questions about setting up your team repository:

1. Check the [main README](README.md) for general setup instructions
2. Review this guide thoroughly
3. Open an issue in your team repository for team-specific questions
4. Consult with your team lead or project manager

---

**Happy collaborating!** 🎉
