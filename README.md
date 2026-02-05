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

### Recommended IDEs

Choose an IDE that fits your workflow:

- **[PyCharm](https://www.jetbrains.com/pycharm/)** — Full-featured Python IDE with excellent Jupyter support. Free Community Edition available.
- **[Cursor](https://cursor.sh/)** — Modern editor with AI assistance, great for notebooks and code navigation.

### Installing Python

**Option 1: Direct download (recommended for beginners)**
- Download Python 3.10.14 from [python.org/downloads](https://www.python.org/downloads/)
- Run the installer and check "Add Python to PATH" during installation

**Option 2: Using Chocolatey (Windows package manager)**

**What is Chocolatey?**  
[Chocolatey](https://chocolatey.org/) is a Windows package manager that lets you install software from the command line, similar to `apt` on Linux or `brew` on macOS. It simplifies installing and updating tools like Python, Geany, and other development software.

**Install Chocolatey:**
1. Open **PowerShell as Administrator**
2. Run:
   ```powershell
   iex ((New-Object Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
   ```
   Or visit [chocolatey.org/install](https://chocolatey.org/install) for detailed instructions.

**Install Python 3.10.14 via Chocolatey:**
```powershell
choco install python --version=3.10.14 -y --params="'/InstallAllUsers /PrependPath'"
```

**Disable Windows Store Python:** Go to Settings → Apps → App execution aliases and turn OFF `python.exe` and `python3.exe` to ensure the installed Python is used.

### Installing Geany (optional, lightweight editor)

**Option 1: Direct download**
- Download from [geany.org/download](https://www.geany.org/download/releases/)

**Option 2: Using Chocolatey**
```powershell
choco install geany -y
```

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

- Virtualization: Parallels Desktop is used to run Windows 11 (ARM).
- Windows Setup: Ensure Windows 11 is fully updated.
- Sharing: Enable Parallels Options > Sharing to share a local code directory
  (e.g., /Users/<username>/code) with the Windows VM (shared at \\Mac\Home\code\).
- Chocolatey: Open PowerShell (Admin) and install Chocolatey (package manager):
  ```
  iex ((New-Object Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
  ```
- Python: Install Python 3.10.14:
  ```
  choco install python --version=3.10.14 -y --params="'/InstallAllUsers /PrependPath'"
  ```
- Disable Store Python: Go to Settings > Apps > App execution aliases and turn OFF python.exe.
- Geany: Install the Geany IDE:
  ```
  choco install geany -y
  ```

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

## Class 2

- Jupyter setup and notebook: `class-2-machine-learning-basics/`
