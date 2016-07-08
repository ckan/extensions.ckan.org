---
layout: extension
name: userautoadd
title: dd new users automatically to an organization with a given role
author: Aptivate
homepage: https://github.com/aptivate/ckanext-userautoadd
github_user: aptivate
github_repo: ckanext-userautoadd
category: Extension
featured: 
permalink: /extension/userautoadd/
---


[![image](https://travis-ci.org/aptivate/ckanext-userautoadd.svg?branch=master)](https://travis-ci.org/aptivate/ckanext-userautoadd)

![image](https://coveralls.io/repos/aptivate/ckanext-userautoadd/badge.svg)

> target  
> <https://coveralls.io/r/aptivate/ckanext-userautoadd>
>
[![Downloads](https://pypip.in/download/ckanext-userautoadd/badge.svg)](https://pypi.python.org/pypi//ckanext-userautoadd/)

[![Latest Version](https://pypip.in/version/ckanext-userautoadd/badge.svg)](https://pypi.python.org/pypi/ckanext-userautoadd/)

[![Supported Python versions](https://pypip.in/py_versions/ckanext-userautoadd/badge.svg)](https://pypi.python.org/pypi/ckanext-userautoadd/)

[![Development Status](https://pypip.in/status/ckanext-userautoadd/badge.svg)](https://pypi.python.org/pypi/ckanext-userautoadd/)

[![License](https://pypip.in/license/ckanext-userautoadd/badge.svg)](https://pypi.python.org/pypi/ckanext-userautoadd/)

|---------------------|
| ckanext-userautoadd |

Adds new users to an existing organization.

Requirements
============

Tested with CKAN v2.5.2

Installation
============

To install ckanext-userautoadd:

1.  Activate your CKAN virtual environment, for example:

        . /usr/lib/ckan/default/bin/activate

2.  Install the ckanext-userautoadd Python package into your virtual environment:

        pip install ckanext-userautoadd

3.  Add `userautoadd` to the `ckan.plugins` setting in your CKAN config file (by default the config file is located at `/etc/ckan/default/production.ini`).
4.  Restart CKAN. For example if you've deployed CKAN with Apache on Ubuntu:

        sudo service apache2 reload

Config Settings
===============

> \# The organization to which new users are added ckan.userautoadd.organization\_name = my\_organization
>
> \# The role the new users will have ckan.userautoadd.organization\_role = editor

Development Installation
========================

To install ckanext-userautoadd for development, activate your CKAN virtualenv and do:

    git clone https://github.com/aptivate/ckanext-userautoadd.git
    cd ckanext-userautoadd
    python setup.py develop
    pip install -r dev-requirements.txt

Running the Tests
=================

To run the tests, do:

    nosetests --nologcapture --with-pylons=test.ini

To run the tests and produce a coverage report, first make sure you have coverage installed in your virtualenv (`pip install coverage`) then run:

    nosetests --nologcapture --with-pylons=test.ini --with-coverage --cover-package=ckanext.userautoadd --cover-inclusive --cover-erase --cover-tests

---------------------------------Registering ckanext-userautoadd on PyPI ---------------------------------

ckanext-userautoadd should be availabe on PyPI as <https://pypi.python.org/pypi/ckanext-userautoadd>. If that link doesn't work, then you can register the project on PyPI for the first time by following these steps:

1.  Create a source distribution of the project:

        python setup.py sdist

2.  Register the project:

        python setup.py register

3.  Upload the source distribution to PyPI:

        python setup.py sdist upload

4.  Tag the first release of the project on GitHub with the version number from the `setup.py` file. For example if the version number in `setup.py` is 0.0.1 then do:

        git tag 0.0.1
        git push --tags

----------------------------------------Releasing a New Version of ckanext-userautoadd ----------------------------------------

ckanext-userautoadd is availabe on PyPI as <https://pypi.python.org/pypi/ckanext-userautoadd>. To publish a new version to PyPI follow these steps:

1.  Update the version number in the `setup.py` file. See [PEP 440](http://legacy.python.org/dev/peps/pep-0440/#public-version-identifiers) for how to choose version numbers.
2.  Create a source distribution of the new version:

        python setup.py sdist

3.  Upload the source distribution to PyPI:

        python setup.py sdist upload

4.  Tag the new release of the project on GitHub with the version number from the `setup.py` file. For example if the version number in `setup.py` is 0.0.2 then do:

        git tag 0.0.2
        git push --tags



