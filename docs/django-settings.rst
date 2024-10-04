Django Settings
===============

To use this app you'll need to define several settings



Process Tasks
-------------

You need to define a `PROCESS_TASKS` setting. This lists all the tasks that will be processed for each uploaded data, in order of processing.

It should be a list of tuples and every tuple should be `('Python module', 'Python class name')`.
Each class should extend libcoveweb2.process.base.ProcessDataTask

Example:

.. code-block:: python

    PROCESS_TASKS = [
        # Get data if not already on disk
        ("libcoveweb2.process.common_tasks.download_data_task", "DownloadDataTask"),
        ...
    ]

Celery Message Queue
--------------------

Any Celery settings needed must be set up.

At a minimum this will include `CELERY_BROKER_URL`.


Settings to copy from library which have sensible defaults
----------------------------------------------------------

This application also needs a bunch of configuration values that already have defaults set. In most cases you can just reuse these variables.

:doc:`For a list of these settings see here. <python-api/settings>`

To do so, you can do something like this in your Django project's main setting.py file:

.. code-block:: python

    from libcoveweb2 import settings
    ALLOWED_JSON_CONTENT_TYPES = settings.ALLOWED_JSON_CONTENT_TYPES
    ALLOWED_JSON_EXTENSIONS = settings.ALLOWED_JSON_EXTENSIONS
    ...
