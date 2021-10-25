import unittest
from pathlib import Path

from puts import title_cap

project_root_dir = Path(__file__).resolve().parent.parent
res_dir = project_root_dir / "tests/resources"


class TestString(unittest.TestCase):
    def test_title_cap(self):
        self.assertEqual(
            "Shakespeare Wrote Romeo and Juliet.",
            title_cap("shakespeare wrote romeo and juliet."),
        )
        self.assertEqual(
            "East of Eden was a Popular Book by John Steinbeck.",
            title_cap("east of eden was a popular book by john steinbeck."),
        )

    def test_title_cap_advanced(self):
        self.assertEqual(
            "The Assassin’s Cloak: An Anthology of the World’s Greatest Diarists",
            title_cap(
                "the assassin’s cloak: an anthology of the world’s greatest diarists"
            ),
        )
