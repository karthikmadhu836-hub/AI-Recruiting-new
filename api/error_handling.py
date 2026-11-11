"""
Zecpath AI
Day 59 - API Error Handling
"""

import time


def retry_request(func, retries=3, delay=1):
    """
    Retry an API request before returning an error.
    """

    for attempt in range(retries):
        try:
            return func()
        except Exception:
            if attempt < retries - 1:
                time.sleep(delay)

    return {
        "error": "Max retries exceeded",
        "success": False
    }


if __name__ == "__main__":
    print(retry_request(lambda: 1))