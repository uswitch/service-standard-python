from prometheus_client import Counter, Histogram
import functools
import time
from flask import request

HTTP_REQUESTS_TOTAL = Counter(
    'http_requests_total',
    'Count of all HTTP requests',
    ['method', 'status', 'path', 'host']
    )

HTTP_REQUEST_DURATION_SECONDS = Histogram(
    'http_request_duration_seconds',
    'HTTP request duration buckets',
    ['method', 'status', 'path', 'host'],
    buckets=[0.001, 0.005, 0.01, 0.05, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 5.0, 10.0, 60.0]
    )

ERRORS_TOTAL = Counter(
    'errors_total',
    'Count of all non-HTTP errors',
    ['type']
    )


def service_standard_flask_wrapper(httpHandler):
    @functools.wraps(httpHandler)
    def wrapper_measure(*args, **kwargs):
        start_time = time.perf_counter()
        # Parse request
        method = request.method
        path = request.path
        host = request.host
        # Handle request
        resp = httpHandler(*args, **kwargs)
        status = resp[1]
        # Record metrics
        HTTP_REQUESTS_TOTAL.labels(
            method=method,
            status=status,
            path=path,
            host=host
        ).inc()
        HTTP_REQUEST_DURATION_SECONDS.labels(
            method=method,
            status=status,
            path=path,
            host=host
        ).observe(time.perf_counter() - start_time)
        return resp
    return wrapper_measure
