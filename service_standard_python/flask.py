import functools
import time
from flask import request
from prometheus_client import make_wsgi_app
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from service_standard_python.metrics import HTTP_REQUESTS_TOTAL, HTTP_REQUEST_DURATION_SECONDS


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


def add_prometheus(app):
    app.wsgi_app = DispatcherMiddleware(app.wsgi_app, {
        '/metrics': make_wsgi_app()
    })
