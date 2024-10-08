Processing Pipeline
===================

Why?
----

The application lets you define a series of tasks that will be checked for each bit of uploaded data, in order.

Tasks need to be defined by each app, but there is a library of common tasks to make this easier.

This allows for maximum flexibility - each app can define the tasks they need, including non-standard tasks that are not used by other CoVE's.
(For example, BODS CoVE has a sample mode. When the user uploads big data, they can choose to run sample mode and only check some of it.
This is accomplished by a special task towards the start of the pipeline that generates a smaller file from the uploaded file.)

What happens when the user uploads data?
----------------------------------------

The background worker will start processing the data and the user will be redirected to the results page.

What happens when the user looks at a results page?
---------------------------------------------------

Everytime a user views a results page, the system will check the state of that data.

If it's currently being processed, the user will see a progress page with a wait message.

If it's not currently being processed, the system will call `is_processing_applicable` and `is_processing_needed` functions on each task to see if any work is needed.

If there is work to do, it will start the work and the user will see a progress page with a wait message.
This means that even after a task first finishes, a task can change it's mind and request to do more work.
(The most common use case for this is if the software is upgraded and how the processing is done is changed.)

If there is no work to do, the system will show a results page to the user.
`get_context` will be called on every task, so the task can load results from it's cache and present them to the user.

Other pages that may be shown to the user include:
    * An error page if a Python error occurred
    * An expired page, if the data is so old that it has been expired and removed from the system

How is the data actually processed?
-----------------------------------

To process the task, the background worker will call `process`.
This can take as long as it needs, and the results should be cached for speedy loading later.

Early tasks can also return data that will be passed to later tasks.
This means any information or work that is needed in multiple tasks does not need to be done multiple times, but can be done once then reused.


How should I define my tasks?
-----------------------------


Each task should be defined by extending a class. :doc:`For more information on the base class, see here. <python-api/process/base>`

And your tasks should then be defined in settings. :doc:`For more information on settings, see here. <django-settings>`

An example task pipeline
------------------------

.. code-block:: python


        PROCESS_TASKS = [
            # Get data if not already on disk - if the user provided a URL
            ("libcoveweb2.process.common_tasks.download_data_task", "DownloadDataTask"),
            # BOD's has a special Sample mode.
            # If that's activated, we'll make the sample data now for later tasks to use.
            ("cove_bods.process", "Sample"),
            # Make sure uploads are in primary format - for BOD's that is JSON
            # So any spreadsheets uploaded should be converted
            ("cove_bods.process", "WasJSONUploaded"),
            ("cove_bods.process", "ConvertSpreadsheetIntoJSON"),
            # Some information is reused in multiple tasks to come
            # So we'll process it once now and later tasks can reuse it.
            ("cove_bods.process", "GetDataReaderAndConfigAndSchema"),
            # Convert from primary JSON format into other output formats
            ("cove_bods.process", "ConvertJSONIntoSpreadsheets"),
            # Check and generate statistics from the JSON data
            ("cove_bods.process", "AdditionalFieldsChecksTask"),
            ("cove_bods.process", "PythonValidateTask"),
            ("cove_bods.process", "JsonSchemaValidateTask"),
        ]

