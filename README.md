# AI Fundamentals Code Repository

This repository contains the code, notes, and projects for the Unique System Skills AI Fundamentals course.

## Overview

This course is designed for absolute beginners to understand the foundation of Artificial
Intelligence, including Machine Learning (ML), Deep Learning (DL), Natural Language Processing
(NLP), and Computer Vision (CV), with hands-on coding using Python and real-world applications.

## Eligibility

Students should have basic knowledge of a computer programming language and be familiar with
computer fundamentals. Basic understanding of any programming language is mandatory (Python
knowledge required).

## Schedule

The course covers the following core topics:
- Introduction to Artificial Intelligence
- Core Concepts in AI
- Machine Learning Basics
- Deep Learning Basics
- Natural Language Processing (NLP)
- Computer Vision Basics
- Tools & Platforms for Al
- Ethics & Responsible Al
- Capstone Mini Projects
- Review & Assessment

## Development Environment Setup

The course uses Python 3.10 and the Geany IDE for hands-on coding.

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

## Workflow Notes

- Editing: Edit files using Cursor (macOS).
- Running Code: Run Python code in Windows (e.g., via Geany).
- Git: Perform Git operations on macOS only.

## Key Links & Resources

- [Course Syllabus](https://drive.google.com/file/d/13ZoVr0B51PqaOcS31l4vcKWXuaTPDbWu/view?usp=sharing)
- Course Folder: [Sharepoint Folder](https://usskills-my.sharepoint.com/personal/training_usa_systemskills_com/_layouts/15/onedrive.aspx?id=%2Fpersonal%2Ftraining%5Fusa%5Fsystemskills%5Fcom%2FDocuments%2FTraining%20%2D%20Main%2FUSS%20IT%20Training%20USA%20%2D%20IMPORTANT%2FInstructor%20Shared%20Folder%2FGanesh%20Bhosale%2FAI%20Fundamentals&ga=1)

## Class 2

- Jupyter setup and notebook: `class-2-machine-learning-basics/`
