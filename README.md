# service-standard-python
The Service Standard Library for Python services.

This library covers implementations for various areas documented in the [Service Standard](https://github.com/uswitch/service-standard-docs)

## Setup


## Usage
To track Flask HTTP requests, use this:
```python
from service-standard-python import service_standard_flask_wrapper

...

@app.route('/', methods=['GET'])
@service_standard_flask_wrapper
def myHandlerFunc():
```

To count errors, use this:
```python
from service-standard-python import ERRORS_TOTAL

...

def myErrorHandler(e):
    ERRORS_TOTAL.labels(type=type(e).__name__).inc()
    handleError(e)
```