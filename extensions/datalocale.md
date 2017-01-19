---
layout: extension
name: datalocale
title: extension CKAN développée pour le projet http-//catalogue
author: portail de données ouvertes datalocale.fr
homepage: https://github.com/datalocale/ckanext-datalocale
github_user: datalocale
github_repo: ckanext-datalocale
category: Extension
featured: 
permalink: /extension/datalocale/
---


[![image](https://travis-ci.org/logilab/ckanext-datalocale.svg?branch=master)](https://travis-ci.org/logilab/ckanext-datalocale)

![image](https://coveralls.io/repos/logilab/ckanext-datalocale/badge.svg)

> target  
> <https://coveralls.io/r/logilab/ckanext-datalocale>

[![Downloads](https://pypip.in/download/ckanext-datalocale/badge.svg)](https://pypi.python.org/pypi//ckanext-datalocale/)

[![Latest Version](https://pypip.in/version/ckanext-datalocale/badge.svg)](https://pypi.python.org/pypi/ckanext-datalocale/)

[![Supported Python versions](https://pypip.in/py_versions/ckanext-datalocale/badge.svg)](https://pypi.python.org/pypi/ckanext-datalocale/)

[![Development Status](https://pypip.in/status/ckanext-datalocale/badge.svg)](https://pypi.python.org/pypi/ckanext-datalocale/)

[![License](https://pypip.in/license/ckanext-datalocale/badge.svg)](https://pypi.python.org/pypi/ckanext-datalocale/)

|                    |
|--------------------|
| ckanext-datalocale |

Requirements
============

For example, you might want to mention here which versions of CKAN this extension works with.

Installation
============

To install ckanext-datalocale:

1.  Activate your CKAN virtual environment, for example:

        . /usr/lib/ckan/default/bin/activate

2.  Install the ckanext-datalocale Python package into your virtual environment:

        pip install ckanext-datalocale

3.  Add `datalocale` to the `ckan.plugins` setting in your CKAN config file (by default the config file is located at `/etc/ckan/default/production.ini`).
4.  Restart CKAN. For example if you've deployed CKAN with Apache on Ubuntu:

        sudo service apache2 reload

Config Settings
===============

Document any optional config settings here. For example:

    # The minimum number of hours to wait before re-checking a resource
    # (optional, default: 24).
    ckanext.datalocale.some_setting = some_default_value

Development Installation
========================

To install ckanext-datalocale for development, activate your CKAN virtualenv and do:

    git clone https://github.com/logilab/ckanext-datalocale.git
    cd ckanext-datalocale
    python setup.py develop
    pip install -r dev-requirements.txt

Running the Tests
=================

To run the tests, do:

    nosetests --nologcapture --with-pylons=test.ini

To run the tests and produce a coverage report, first make sure you have coverage installed in your virtualenv (`pip install coverage`) then run:

    nosetests --nologcapture --with-pylons=test.ini --with-coverage --cover-package=ckanext.datalocale --cover-inclusive --cover-erase --cover-tests

---------------------------------Registering ckanext-datalocale on PyPI ---------------------------------

ckanext-datalocale should be availabe on PyPI as <https://pypi.python.org/pypi/ckanext-datalocale>. If that link doesn't work, then you can register the project on PyPI for the first time by following these steps:

1.  Create a source distribution of the project:

        python setup.py sdist

2.  Register the project:

        python setup.py register

3.  Upload the source distribution to PyPI:

        python setup.py sdist upload

4.  Tag the first release of the project on GitHub with the version number from the `setup.py` file. For example if the version number in `setup.py` is 0.0.1 then do:

        git tag 0.0.1
        git push --tags

----------------------------------------Releasing a New Version of ckanext-datalocale ----------------------------------------

ckanext-datalocale is availabe on PyPI as <https://pypi.python.org/pypi/ckanext-datalocale>. To publish a new version to PyPI follow these steps:

1.  Update the version number in the `setup.py` file. See [PEP 440](http://legacy.python.org/dev/peps/pep-0440/#public-version-identifiers) for how to choose version numbers.
2.  Create a source distribution of the new version:

        python setup.py sdist

3.  Upload the source distribution to PyPI:

        python setup.py sdist upload

4.  Tag the new release of the project on GitHub with the version number from the `setup.py` file. For example if the version number in `setup.py` is 0.0.2 then do:

        git tag 0.0.2
        git push --tags



