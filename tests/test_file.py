import unittest
from pathlib import Path

from puts.file import alternative_file_path

project_root_dir = Path(__file__).resolve().parent.parent
res_dir = project_root_dir / "tests/resources"


class TestFile(unittest.TestCase):
    def test_alternative_file_path_0(self):
        self.assertTrue(isinstance(alternative_file_path("TEST"), str))
        self.assertTrue(isinstance(alternative_file_path("TEST.test"), str))
        self.assertTrue(isinstance(alternative_file_path(Path("TEST")), Path))
        self.assertTrue(isinstance(alternative_file_path(Path("TEST.test")), Path))

    def test_alternative_file_path_1(self):
        test_fp = res_dir / "x.txt"
        self.assertEqual(alternative_file_path(test_fp), test_fp)

    def test_alternative_file_path_2(self):
        test_fp = res_dir / "test.txt"
        test_fp_new = res_dir / "test-1.txt"
        self.assertEqual(alternative_file_path(test_fp), test_fp_new)

    def test_alternative_file_path_3(self):
        test_fp = str(res_dir / "test.txt")
        test_fp_new = str(res_dir / "test-1.txt")
        self.assertEqual(alternative_file_path(test_fp), test_fp_new)
