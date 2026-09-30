"""A small command-line tool for checking the basics of a Python repository."""

import argparse
from pathlib import Path


def check_repository(repository_path):
    """Return a list of status and message pairs for a repository."""
    if not repository_path.is_dir():
        return [("FAIL", f"'{repository_path}' is not a directory.")]

    python_files = list(repository_path.rglob("*.py"))
    python_files = [
        path for path in python_files
        if not {".git", ".venv", "venv", "__pycache__"}.intersection(path.parts)
    ]
    test_files = [
        path for path in python_files
        if path.name.startswith("test_") or path.name.endswith("_test.py")
    ]

    checks = [
        ("README.md", (repository_path / "README.md").is_file()),
        ("Git repository", (repository_path / ".git").exists()),
        ("Python files", bool(python_files)),
        ("Python tests", bool(test_files)),
    ]

    return [
        ("PASS" if passed else "WARN", f"{name}: {'found' if passed else 'not found'}")
        for name, passed in checks
    ]


def main():
    parser = argparse.ArgumentParser(
        description="Check a repository for a README, Git metadata, Python files, and tests."
    )
    parser.add_argument(
        "path",
        nargs="?",
        default=".",
        help="repository folder to check (defaults to the current folder)",
    )
    arguments = parser.parse_args()

    repository_path = Path(arguments.path).expanduser().resolve()
    results = check_repository(repository_path)

    print(f"Repository health check: {repository_path}")
    for status, message in results:
        print(f"[{status}] {message}")

    has_warnings = any(status != "PASS" for status, _ in results)
    if has_warnings:
        print("\nSome checks need attention.")
        return 1

    print("\nAll checks passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())