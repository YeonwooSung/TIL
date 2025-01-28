# Python

* [AST](./abstrct_syntax_tree/)
* [Batch Processing](./batch-processing/)
    * [Airflow for building ETL pipeline](./batch-processing/airflow/)
    * [Joblib for building Batch Processing Pipeline](./batch-processing/simple-joblib-pipeline.py)
* [D-Bus](./dbus/)
* [CFFI and ctypes](./cffi_and_ctypes/)
* [concurrency](./concurrency/)
* [crawling](./crawling/)
* [date and time](./date_and_time/)
* [decorator](./decorator/)
* [design patterns](./design_pattern/)
    * [event handler](./design_pattern/event-handler/)
    * [observer pattern](./design_pattern/observer/)
* [dictionary tricks](./dictionary_tricks/)
* [extension - clang](./extension_clang/)
* [faker](./faker/)
    * [testing with fake time](./faker/faking_time.py)
    * [testing with fake data](./faker/test_mailer.py)
* [file paths](./path/)
* [flask](./flask/)
    * [Make Flask app to handle non-blocking I/O by using asyncio-based decorator](./flask/flask_asyncio_decorator.py)
    * [Object Oriented programming with Flask](./flask/flask_oop_wrapping.py)
* [generator](./generator/)
* [geoinformation](./geoinformation/)
    * [pgeocode](./geoinformation/pgeocode_examples/)
* [GUI in python](./gui/)
    * [tk](./gui/pytk/)
    * [pyqt](./gui/pyqt/)
* [logging](./logging/)
    * [Capture errors with sentry](./logging/sentry_error_capturing/)
    * [Configure logging from configurations](./logging/logging-configuration/)
    * [Distributed tracing with jaeger](./logging/distributed-tracing-with-jaeger/)
    * [Use prometheus for log managing and visualization](./logging/using-prometheus/)
* [mutation testing](./mut-test/)
* [object oriented programming](./oop/)
* [PyTorch](./pytorch/)
* [Performance Profiling](./profile-performance/)
* [regular expression](./regex/)
* [string handling (i.e. format string)](./string/)
* [test-driven development](./tdd/)
* [webserver from scratch!](./web_server_from_scratch/)

## setup.py

1. Create `dist` directory and `wheel` file:
```bash
python setup.py sdist bdist_wheel
```

2. Use twine to upload the package to PyPI:
```bash
pip install twine

python -m twine upload dist/*
```
