from puts import get_logger

logger = get_logger(stream_only=True)

logger.debug("Hello world!")
logger.info("Hello world!")
logger.warning("Hello world!")
logger.error("Hello world!")
logger.critical("Hello world!")
