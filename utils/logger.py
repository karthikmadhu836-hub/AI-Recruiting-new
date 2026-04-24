from loguru import logger
import os

LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

logger.add(
    f"{LOG_DIR}/app.log",
    rotation="1 MB",
    retention="10 days",
    level="INFO"
)

def get_logger():
    return logger