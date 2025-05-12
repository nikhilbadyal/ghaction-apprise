"""Entrypoint."""

from loguru import logger

from src.apprise import send_message

logger.info(send_message())
