# yamlmod

[![Build Status](https://travis-ci.org/sciyoshi/yamlmod.svg?branch=master)](https://travis-ci.org/sciyoshi/yamlmod)

This project allows you to import YAML files directly from Python code.

## Installation

Install it using `pip`:

    pip install yamlmod

To use it, simply add the following line of code to one of your files:

	import yamlmod

This will install a global import hook that will check for files with a `.yml`
extension.

## Why?

This should be seen mostly as an example on how to customize Python's import
system. However, it can be useful when developing Django or Flask applications
that have an auto-reload feature. If your config is stored in a separate file,
these frameworks won't detect changes. By using `yamlmod`, the config will
simply look like a regular module to Django, and it will automatically reload
the module for you when the file changes.
