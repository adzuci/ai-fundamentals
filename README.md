# AI Fundamentals Code Repository

This repository contains the code, notes, and projects for the AI Fundamentals course.

## Overview

This course is designed for absolute beginners to understand the foundations of Artificial
Intelligence (AI), including Machine Learning (ML), Deep Learning (DL), Natural Language
Processing (NLP), and Computer Vision (CV), with hands-on coding using Python and real-world
applications.

## Prerequisites

Students should have:
- Basic knowledge of a computer programming language and familiarity with computer fundamentals.
- Basic understanding of any programming language is mandatory (Python knowledge required).

## Course Schedule

The course covers the following core topics:
- Introduction to Artificial Intelligence
- Core Concepts in AI
- Machine Learning Basics
- Deep Learning Basics
- Natural Language Processing (NLP)
- Computer Vision Basics
- Tools & Platforms for AI
- Ethics & Responsible AI
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

- Course Syllabus:
- Course Folder: Sharepoint Folder
