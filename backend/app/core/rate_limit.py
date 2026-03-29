import time
from collections import defaultdict
from typing import Dict, List

from app.core.exceptions import RateLimitError

_window_seconds = 15 * 60
_max_requests = 5
_timestamps: Dict[str, List[float]] = defaultdict(list)


def check_contact_rate_limit(client_ip: str) -> None:
    now = time.time()
    bucket = _timestamps[client_ip]
    bucket[:] = [t for t in bucket if now - t < _window_seconds]
    if len(bucket) >= _max_requests:
        raise RateLimitError(
            "Too many contact submissions from this address. Try again in 15 minutes."
        )
    bucket.append(now)
