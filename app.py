"""Check a repository for a README, tests folder, and requirements file."""

import argparse
from pathlib import Path


def check_repository(repository_path):
    """Print a health report and return True when all checks pass."""
    if not repository_path.is_dir():
        print(f"Error: '{repository_path}' is not a folder.")
        return False

    readme_found = any(
        (repository_path / name).is_file()
        for name in ("README.md", "Readme.md", "readme.md")
    )
    tests_found = any(
        (repository_path / name).is_dir()
        for name in ("test", "tests")
    )
    requirements_found = (repository_path / "requirements.txt").is_file()

    checks = [
        ("README file", readme_found),
        ("Test folder", tests_found),
        ("requirements.txt", requirements_found),
    ]

    print(f"Repository health report for: {repository_path}")
    for name, found in checks:
        status = "OK" if found else "MISSING"
        print(f"[{status}] {name}")

    is_healthy = all(found for _, found in checks)
    if is_healthy:
        print("\nRepository looks healthy.")
    else:
        print("\nRepository needs attention.")

    return is_healthy


def main():
    parser = argparse.ArgumentParser(
        description="Check a repository for a README, tests folder, and requirements.txt."
    )
    parser.add_argument(
        "path",
        nargs="?",
        default=".",
        help="repository folder to check (defaults to the current folder)",
    )
    arguments = parser.parse_args()

    repository_path = Path(arguments.path).expanduser().resolve()
    return 0 if check_repository(repository_path) else 1


if __name__ == "__main__":
    raise SystemExit(main())