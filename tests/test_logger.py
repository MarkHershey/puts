import unittest
from pathlib import Path

from puts.logger import init_logger

project_root_dir = Path(__file__).resolve().parent.parent
res_dir = project_root_dir / "tests/resources"


class TestLogging(unittest.TestCase):
    def test_logger(self):
        logger = init_logger(stream_only=True)
        logger.debug("Hello world!")
        logger.info("Hello world!")
        logger.warning("Hello world!")
        logger.error("Hello world!")
        logger.critical("Hello world!")
        logger.fatal("Hello world!")

    def test_logger_1(self):
        logger = init_logger(stream_only=True)
        self.assertTrue(logger.hasHandlers())
