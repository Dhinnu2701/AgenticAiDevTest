import contextlib
import io
import tempfile
import unittest
from pathlib import Path

from app import check_repository


class CheckRepositoryTests(unittest.TestCase):
    def test_reports_healthy_repository(self):
        with tempfile.TemporaryDirectory() as temporary_folder:
            repository = Path(temporary_folder)
            (repository / "README.md").write_text("Example project\n")
            (repository / "tests").mkdir()
            (repository / "requirements.txt").write_text("\n")
            report = io.StringIO()

            with contextlib.redirect_stdout(report):
                is_healthy = check_repository(repository)

        self.assertTrue(is_healthy)
        self.assertIn("[OK] README file", report.getvalue())
        self.assertIn("Repository looks healthy.", report.getvalue())

    def test_reports_missing_repository_items(self):
        with tempfile.TemporaryDirectory() as temporary_folder:
            report = io.StringIO()

            with contextlib.redirect_stdout(report):
                is_healthy = check_repository(Path(temporary_folder))

        self.assertFalse(is_healthy)
        self.assertIn("[MISSING] requirements.txt", report.getvalue())
        self.assertIn("Repository needs attention.", report.getvalue())

    def test_rejects_a_path_that_is_not_a_directory(self):
        with tempfile.TemporaryDirectory() as temporary_folder:
            missing_folder = Path(temporary_folder) / "missing"
            report = io.StringIO()

            with contextlib.redirect_stdout(report):
                is_healthy = check_repository(missing_folder)

        self.assertFalse(is_healthy)
        self.assertIn("is not a folder", report.getvalue())


if __name__ == "__main__":
    unittest.main()