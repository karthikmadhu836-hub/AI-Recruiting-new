"""
Final Error Handler
"""


def safe_run(func, fallback=None):

    try:
        return func()

    except Exception as error:

        return {
            "error": str(error),
            "fallback": fallback,
            "status": "handled"
        }