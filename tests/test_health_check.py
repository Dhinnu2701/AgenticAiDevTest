import tempfile
import unittest
from pathlib import Path

from health_check import check_repository


class CheckRepositoryTests(unittest.TestCase):
    def test_reports_present_repository_files(self):
        with tempfile.TemporaryDirectory() as temporary_folder:
            repository = Path(temporary_folder)
            (repository / "README.md").write_text("Example repository\n")
            (repository / ".git").mkdir()
            (repository / "app.py").write_text("print('hello')\n")
            (repository / "test_app.py").write_text("\n")

            results = check_repository(repository)

        self.assertTrue(all(status == "PASS" for status, _ in results))

    def test_rejects_a_path_that_is_not_a_directory(self):
        results = check_repository(Path("missing-repository-folder"))

        self.assertEqual(results[0][0], "FAIL")


if __name__ == "__main__":
    unittest.main()