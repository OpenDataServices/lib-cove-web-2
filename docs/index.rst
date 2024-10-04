LibCoveWeb2
===========


LibCoveWeb2 is a Django application to use as a library in your own Django apps.

It let's you create CoVE apps - CoVE exists to help people:

* Convert data between common formats (e.g. csv to json)
* Validate data against rules
* Explore data, that machines find easy, but humans find harder to read

The application consists of:

* Database Models to save details of user submitted data
* File storage space to save the user submitted data and cache results of processing
* A message queue
* Workers to process the data according to tasks you provide (but there is a library of common tasks in this application)
* A view to show users output information from the cache of results


.. toctree::
   :maxdepth: 2

   processing-pipeline.rst
   django-settings.rst
   python-api/index.rst
   migration-from-lib-cove-web.rst
   hosting/requirements.rst
   used-by.rst

