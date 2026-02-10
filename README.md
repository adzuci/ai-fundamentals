# AI Fundamentals Code Repository

This repository contains the code, notes, and projects for the Unique System Skills AI Fundamentals course.

## Overview

This course is designed for beginners to understand the foundation of Artificial
Intelligence, including Machine Learning (ML), Deep Learning (DL), Natural Language Processing
(NLP), and Computer Vision (CV), with hands-on coding using Python and real-world applications.

## Eligibility

Students should have basic knowledge of a computer programming language and be familiar with
computer fundamentals. Basic understanding of any programming language is mandatory (Python
knowledge required).

## Schedule

The course is typically taught over ten four hour Zoom seeions over two weeks and covers the following core topics:
1. Introduction to Artificial Intelligence
1. Core Concepts in AI
1. Machine Learning Basics
1. Deep Learning Basics
1. Natural Language Processing (NLP)
1. Computer Vision Basics
1. Tools & Platforms for Al
1. Ethics & Responsible Al
1. Capstone Mini Projects
1. Review & Assessment

## Development Environment Setup

The course uses **Python 3.10** for hands-on coding. Notebooks in this repo can be run **locally** (with Jupyter) or **in Google Colab** (browser-based, no local setup).

### Recommended editors / IDEs

Choose one of these (you can switch later):

- **[Geany](https://www.geany.org/)** — Lightweight, fast editor that’s beginner-friendly.
- **[Cursor](https://cursor.sh/)** — Modern editor with AI assistance, great for notebooks and code navigation.
- **[PyCharm](https://www.jetbrains.com/pycharm/)** — Full-featured Python IDE with excellent Jupyter support. Free Community Edition available.

### Installing Python

**Option 1: Direct download (recommended for beginners)**
- Download Python [3.10.11](https://www.python.org/ftp/python/3.10.11/python-3.10.11-amd64.exe) or 3.10.14 from [python.org/downloads](https://www.python.org/downloads/)
- Run the installer and check "Add Python to PATH" during installation

### Windows dev setup (PowerShell, using winget)

On Windows 10/11, **winget** (the Windows Package Manager) is available if you have the **App Installer** from the Microsoft Store.

Open **PowerShell** and run:

```powershell
# Windows dev setup (PowerShell)
# Prereq: winget is available on most Windows 10/11 installs (App Installer from Microsoft Store)

# Install Google Chrome (optional but handy for Colab)
winget install --id Google.Chrome --exact

# Install Git
winget install --id Git.Git --exact

# Install PyCharm
# Community (free)
winget install --id JetBrains.PyCharm.Community --exact

# OR PyCharm Professional (paid)
# If you have a student license / JetBrains Student Pack, install Pro and sign in to activate
# Student Pack: https://www.jetbrains.com/academy/student-pack/
winget install --id JetBrains.PyCharm --exact

# Verify Git
git --version
```

For **Geany** and **Cursor**, use their installers:

- Geany: download from `https://www.geany.org/download/releases/`
- Cursor: download from `https://cursor.sh/`

### Setting up a Virtual Environment

**Option 1: Using pyenv (recommended for managing multiple Python versions)**
- Install [pyenv](https://github.com/pyenv/pyenv) (macOS/Linux) or [pyenv-win](https://github.com/pyenv-win/pyenv-win) (Windows)
- Create a virtual environment:
  ```bash
  pyenv virtualenv 3.10.14 ai-fundamentals
  pyenv local ai-fundamentals
  ```

**Option 2: Using Python's built-in venv**
```bash
python -m venv .venv
# On Windows:
.venv\Scripts\activate
# On macOS/Linux:
source .venv/bin/activate
```

Then install dependencies:
```bash
pip install -r requirements.txt
```

## Installation Guide (Windows VM on macOS via Parallels)

- **Virtualization**: Parallels Desktop is used to run Windows 11 (ARM).
- **Windows Setup**: Ensure Windows 11 is fully updated.
- **Sharing**: Enable Parallels Options > Sharing to share a local code directory  
  (e.g., `/Users/<username>/code`) with the Windows VM (shared at `\\Mac\Home\code\`).
- **Editors on both sides**:  
  - On macOS you can open the shared folder in **Geany**, **Cursor**, or **PyCharm**.  
  - In the Windows VM you can open the **same folder** in **Geany**, **Cursor**, or **PyCharm** (installed via winget or their installers).  
  - This lets you work on the **same project from both macOS and Windows** without copying files.
- **winget in the VM**: In the Windows VM, use the same `winget` commands as above for Git/Chrome/PyCharm. Python itself can still be installed from `python.org` as in the section above; the recommended path for this course is the direct Python installer plus `winget` for tools like Git and IDEs.

## Running Notebooks

Notebooks in this repo (e.g., in `class-2-machine-learning-basics/`) can be run in two ways:

1. **Locally** — Install Jupyter (`pip install jupyter`) and run `jupyter notebook` or `jupyter lab`
2. **Google Colab** — Each notebook includes an "Open in Colab" button; click it to run in your browser with no local setup

See the class-specific READMEs (e.g., `class-2-machine-learning-basics/README.md`) for detailed setup instructions.

## Workflow Notes

- Editing: Edit files using your preferred IDE (PyCharm, Cursor, Geany, etc.)
- Running Code: Run Python code locally or in Colab
- Git: Perform Git operations from your local machine

## Key Links & Resources

- [Course Syllabus](https://drive.google.com/file/d/13ZoVr0B51PqaOcS31l4vcKWXuaTPDbWu/view?usp=sharing)
- Course Folder: <removed>

## Cert Prep

- [AI-900 Azure AI Fundamentals Prep Plan](AI-900_PREP_PLAN.md)

## Class 2

- Jupyter setup and notebook: `class-2-machine-learning-basics/`
