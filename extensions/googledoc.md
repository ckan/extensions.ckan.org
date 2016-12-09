---
layout: extension
name: googledoc
title: CKAN plugin for supporting Google Docs
author: Consumer Data Research Centre (CDRC)
homepage: https://github.com/ESRC-CDRC/ckan-ckanext-googledoc
github_user: ESRC-CDRC
github_repo: ckan-ckanext-googledoc
category: Extension
featured: 
permalink: /extension/googledoc/
---


[![image](https://travis-ci.org/spacelis/ckan-ckanext-googledoc.svg?branch=master)](https://travis-ci.org/spacelis/ckan-ckanext-googledoc)

![image](https://coveralls.io/repos/spacelis/ckan-ckanext-googledoc/badge.png?branch=master)

> target  
> <https://coveralls.io/r/spacelis/ckan-ckanext-googledoc?branch=master>

[![Downloads](https://pypip.in/download/ckan-ckanext-googledoc/badge.svg)](https://pypi.python.org/pypi//ckan-ckanext-googledoc/)

[![Latest Version](https://pypip.in/version/ckan-ckanext-googledoc/badge.svg)](https://pypi.python.org/pypi/ckan-ckanext-googledoc/)

[![Supported Python versions](https://pypip.in/py_versions/ckan-ckanext-googledoc/badge.svg)](https://pypi.python.org/pypi/ckan-ckanext-googledoc/)

[![Development Status](https://pypip.in/status/ckan-ckanext-googledoc/badge.svg)](https://pypi.python.org/pypi/ckan-ckanext-googledoc/)

[![License](https://pypip.in/license/ckan-ckanext-googledoc/badge.svg)](https://pypi.python.org/pypi/ckan-ckanext-googledoc/)

|                        |
|------------------------|
| ckan-ckanext-googledoc |

Requirements
============

For example, you might want to mention here which versions of CKAN this extension works with.

Installation
============

To install ckan-ckanext-googledoc:

1.  Activate your CKAN virtual environment, for example:

        . /usr/lib/ckan/default/bin/activate

2.  Install the ckan-ckanext-googledoc Python package into your virtual environment:

        pip install ckan-ckanext-googledoc

3.  Add `googledoc` to the `ckan.plugins` setting in your CKAN config file (by default the config file is located at `/etc/ckan/default/production.ini`).
4.  Restart CKAN. For example if you've deployed CKAN with Apache on Ubuntu:

        sudo service apache2 reload

Config Settings
===============

Document any optional config settings here. For example:

    # The minimum number of hours to wait before re-checking a resource
    # (optional, default: 24).
    ckanext.googledoc.some_setting = some_default_value

Development Installation
========================

To install ckan-ckanext-googledoc for development, activate your CKAN virtualenv and do:

    git clone https://github.com/spacelis/ckan-ckanext-googledoc.git
    cd ckan-ckanext-googledoc
    python setup.py develop
    pip install -r dev-requirements.txt

Running the Tests
=================

To run the tests, do:

    nosetests --nologcapture --with-pylons=test.ini

To run the tests and produce a coverage report, first make sure you have coverage installed in your virtualenv (`pip install coverage`) then run:

    nosetests --nologcapture --with-pylons=test.ini --with-coverage --cover-package=ckanext.googledoc --cover-inclusive --cover-erase --cover-tests

---------------------------------Registering ckan-ckanext-googledoc on PyPI ---------------------------------

ckan-ckanext-googledoc should be availabe on PyPI as <https://pypi.python.org/pypi/ckan-ckanext-googledoc>. If that link doesn't work, then you can register the project on PyPI for the first time by following these steps:

1.  Create a source distribution of the project:

        python setup.py sdist

2.  Register the project:

        python setup.py register

3.  Upload the source distribution to PyPI:

        python setup.py sdist upload

4.  Tag the first release of the project on GitHub with the version number from the `setup.py` file. For example if the version number in `setup.py` is 0.0.1 then do:

        git tag 0.0.1
        git push --tags

----------------------------------------Releasing a New Version of ckan-ckanext-googledoc ----------------------------------------

ckan-ckanext-googledoc is availabe on PyPI as <https://pypi.python.org/pypi/ckan-ckanext-googledoc>. To publish a new version to PyPI follow these steps:

1.  Update the version number in the `setup.py` file. See [PEP 440](http://legacy.python.org/dev/peps/pep-0440/#public-version-identifiers) for how to choose version numbers.
2.  Create a source distribution of the new version:

        python setup.py sdist

3.  Upload the source distribution to PyPI:

        python setup.py sdist upload

4.  Tag the new release of the project on GitHub with the version number from the `setup.py` file. For example if the version number in `setup.py` is 0.0.2 then do:

        git tag 0.0.2
        git push --tags



