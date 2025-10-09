Develop this library
====================

The git repository comes with a dev container and a sample Django app to see the library running and help you develop it.


To set up, run the dev container and:

.. code-block::

    pip install -e .[dev]
    python manage.py migrate


To run the web server in one terminal:

.. code-block::

    python manage.py runserver  0.0.0.0:8000

Open another terminal, and run the worker:

.. code-block::

    celery -A libfjordweb.celery worker -l debug -c 1


To lint code:

.. code-block::

    isort libfjordweb fjorddemo setup.py
    black libfjordweb fjorddemo setup.py
    flake8 libfjordweb fjorddemo setup.py
    mypy --install-types --non-interactive -p libfjordweb
    mypy --install-types --non-interactive -p fjorddemo

