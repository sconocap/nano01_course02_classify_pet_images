# Classify Pet Images

Hello! Thank you for taking the time to review this capstone project. I appreciate your feedback and guidance.

## About This Project

This project implements a pet image classification system using deep learning models. Coming from a TypeScript background, I used this project to explore two concepts that are important to me:

1. **Test-Driven Development (TDD)**: I've included basic tests in this project to practice writing tests alongside the implementation. While the test coverage is modest, it represents my first steps in applying TDD principles in python.

2. **Shared Code Management**: I wanted to understand how to manage code shared across multiple projects during my studies. This project depends on `ai-common`, a separate repository containing utilities I'll reuse across future capstone projects. As per my personal likes, I've decided to install this dependency from GitHub rather than PyPI. If it behaves like intended, the dependency will be installed when you run `pip install .`.

Also note, after a bit research, I've decided to use `uv` for dependency management on my end. I understand this should not impact your experience.

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/sconocap/nano01_course02_classify_pet_images.git
   cd nano01_course02_classify_pet_images
   ```

2. (Optional) Create and activate a virtual environment to isolate dependencies:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. Install the package and its dependencies:

   **Using pip (recommended):**
   ```bash
   pip install .
   ```

   **Alternatively, using uv:**
   ```bash
   uv sync
   ```

   Both methods will automatically install `ai-common` from GitHub as declared in `pyproject.toml`.