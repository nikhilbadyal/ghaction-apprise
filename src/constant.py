"""Constants."""
from environs import Env

env = Env()
env.read_env()
apprise_url = env.str("INPUT_APPRISE_URL")
apprise_notification_body = env.str("INPUT_APPRISE_NOTIFICATION_BODY")
apprise_notification_title = env.str("INPUT_APPRISE_NOTIFICATION_TITLE")
apprise_attachments = env.list("INPUT_APPRISE_ATTACHMENTS", [])
