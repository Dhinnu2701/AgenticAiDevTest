# Repository Health Checker

This beginner-friendly project contains small command-line tools for checking
whether a repository has useful files in place. Both tools use only the Python
standard library, so no packages need to be installed.

## Requirements

- Python 3.8 or newer

## Setup

1. Clone or download this repository.
2. Open a terminal in the project folder.
3. (Optional) Create and activate a virtual environment:

	```bash
	python3 -m venv .venv
	source .venv/bin/activate
	```

	On Windows, activate it with `.venv\\Scripts\\activate` instead.

4. No package installation is needed. `requirements.txt` is included to show
	that the project has no third-party dependencies.

## Usage

Run the main checker on this folder:

```bash
python3 app.py
```

Pass a folder path to check a different repository:

```bash
python3 app.py /path/to/repository
```

`app.py` checks for a README file, a `test` or `tests` folder, and
`requirements.txt`. It prints `OK` for items it finds and `MISSING` for items
that need attention. The command exits with status `1` if an item is missing.

The additional `health_check.py` script checks for a README, Git metadata,
Python files, and Python test files:

```bash
python3 health_check.py
```

It also accepts an optional repository path.

## Run the tests

Run the project's tests with Python's built-in test runner:

```bash
python3 -m unittest discover -s tests
```