"""
Day 60 - Optimized API Layer
"""

import time


def optimized_response(data):

    start = time.perf_counter()

    result = {
        "data": data
    }

    latency = (time.perf_counter() - start) * 1000

    return {
        "success": True,
        "result": result,
        "latency_ms": round(latency, 3)
    }


if __name__ == "__main__":
    print(optimized_response({"candidate": "C001"}))