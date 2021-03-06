# service-standard-python
The Service Standard Library for Python services.

This library covers implementations for various areas documented in the [Service Standard](https://github.com/uswitch/service-standard-docs)

## Setup

Any build environment will need access to this repo.

### Via pipenv
```
pipenv install -e "git+https://github.com/uswitch/service-standard-python.git@v0.3#egg=service-standard-python"
```
Your Pipfile should have a line like:
```
service-standard-python = {editable = true, git = "https://github.com/uswitch/service-standard-python.git", ref = "v0.3"}
```
### Via pip
```
pip install -e "git+https://github.com/uswitch/service-standard-python@v0.3#egg=service-standard-python"
```

Your requirements.txt should have a line specifying a link to the git repo.

## Usage

### HTTP requests & duration
To track Flask HTTP requests, use the flask wrapper for automatic timing and labelling:
```python
from service_standard_python.flask import service_standard_flask_wrapper

...

@app.route('/', methods=['GET'])
@service_standard_flask_wrapper
def myHandlerFunc():
```

### Errors
To count errors, use the exposed `ERRORS_TOTAL` counter:
```python
from service_standard_python.metrics import ERRORS_TOTAL

...

def myErrorHandler(e):
    ERRORS_TOTAL.labels(type=type(e).__name__).inc()
    handleError(e)
```

### Exposing the endpoint
For simple apps, `add_prometheus()` easily adds a `/metrics` endpoint:
```
from service_standard_python.flask import add_prometheus

app = Flask(__name__)

# Add prometheus wsgi middleware to route /metrics requests
add_prometheus(app)
```

Alternatively, if your application already has middlewares, you can instead use the [prometheus_client](https://pypi.org/project/prometheus-client/) package directly to create an endpoint with `make_wsgi_app()` like so:
```
app.wsgi_app = DispatcherMiddleware(app.wsgi_app, {
        '/other-endpoints': other_wsgi_app()
        '/metrics': make_wsgi_app()
    })
```
