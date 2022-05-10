import unittest

from puts import timestamp_microseconds, timestamp_milliseconds, timestamp_seconds


class TestTimestamp(unittest.TestCase):
    def test_timestamp_microseconds(self):
        self.assertTrue(isinstance(timestamp_microseconds(), str))
        self.assertTrue(" " not in timestamp_microseconds())
        self.assertEqual(len(timestamp_microseconds()), 22)
        self.assertFalse(timestamp_microseconds() == timestamp_microseconds())

    def test_timestamp_milliseconds(self):
        self.assertTrue(isinstance(timestamp_milliseconds(), str))
        self.assertTrue(" " not in timestamp_milliseconds())
        self.assertEqual(len(timestamp_milliseconds()), 19)

    def test_timestamp_seconds(self):
        self.assertTrue(isinstance(timestamp_seconds(), str))
        self.assertTrue(" " not in timestamp_seconds())
        self.assertEqual(len(timestamp_seconds()), 15)
