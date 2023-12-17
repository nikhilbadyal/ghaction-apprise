"""Apprise utils."""
import sys

import apprise
from apprise.common import NotifyFormat
from loguru import logger

# Local Imports
from src.constant import apprise_attachments, apprise_notification_body, apprise_notification_title, apprise_url


def send_message() -> bool:
    """Send message."""
    ap_obj = apprise.Apprise()

    ap_obj.add(apprise_url)
    logger.debug(f"Uploading {apprise_attachments}")
    if not apprise_url:
        logger.error("No apprise URL")
        sys.exit(1)

    return bool(
        ap_obj.notify(
            body=apprise_notification_body,
            title=apprise_notification_title,
            attach=apprise_attachments,
            body_format=NotifyFormat.MARKDOWN,
        ),
    )
