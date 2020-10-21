# service-standard-python
The Service Standard Library for Python services.

This library covers implementations for various areas documented in the [Service Standard](https://github.com/uswitch/service-standard-docs)

## Setup

### Via pipenv
```
pipenv install -e "git+https://github.com/uswitch/service-standard-python.git@v0.1#egg=service-standard-python"
```
Your Pipfile should have a line like:
```
service-standard-python = {editable = true, git = "https://github.com/uswitch/service-standard-python.git", ref = "v0.1"}
```
### Via pip
```
pip install -e "git+https://github.com/uswitch/service-standard-python@v0.1#egg=service_standard_python"
```

Your requirements.txt should have a line specifying a link to the git repo.

## Usage
To track Flask HTTP requests, use this:
```python
from service_standard_python import service_standard_flask_wrapper

...

@app.route('/', methods=['GET'])
@service_standard_flask_wrapper
def myHandlerFunc():
```

To count errors, use this:
```python
from service_standard_python import ERRORS_TOTAL

...

def myErrorHandler(e):
    ERRORS_TOTAL.labels(type=type(e).__name__).inc()
    handleError(e)
```