Hosting Requirements
====================

Database
----------

This is tested with PostgreSQL.

Message queue compatible with Celery
--------------------------------------

Normal options

File Storage
------------

A file storage area is needed. This holds the files supplied by users, and the cached results of processing.

All code access in this library to the file storage area should be through Django `DefaultStorage` API.
This means in theory, you are free to use:

* file storage by setting `MEDIA_ROOT` and `MEDIA_URL`.
* cloud bucket solutions (eg AWS S3, Azure Storage Container).
* any other Django compatible Storage API.

Nothing in this library requires the contents of this storage to be served on the web.

However, code in apps that uses this library may have:

* direct access to the file system, in which case file storage by setting `MEDIA_ROOT` and `MEDIA_URL` is required.
* direct users to URL's for download, in which case the contents of this storage must be served on the web.

All apps that use this library currently just use direct file storage by setting `MEDIA_ROOT` and `MEDIA_URL`,
and that should be considered the only tested solution.


Python web server for the Django app
------------------------------------

Normal options


A background worker
-------------------

Run using Celery's normal run options.

Cron tasks
----------

Some Django management commands should be run on a cron task.

* `expire_files` should be run daily

