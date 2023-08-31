# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)
and this project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).

## [Unreleased]

When upgrading to this version, `ALLOWED_UNKNOWN_CONTENT_TYPES` must be set in the Django settings file, ideally from the settings file included with this library.

## Added

- base.html: Wrap default terms and conditions in template block so it can be overridden
- utils.py: get_file_type_for_flatten_tool: consider content type too
- settings.ALLOWED_UNKNOWN_CONTENT_TYPES.

## Fixed

- utils.py: get_file_type_for_flatten_tool: include an error message in raise at end https://github.com/OpenDataServices/lib-cove-web-2/issues/3

## [0.2.0] - 2023-07-11

## Added

- Model SuppliedDataFile has new method storage_name for use with Django storage (like storage_dir on SuppliedData)

## [0.1.0] - 2023-06-16

First Release

