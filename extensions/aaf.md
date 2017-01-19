---
layout: extension
name: aaf
title: Allows AAF (Australian Acceess Federation) authentication to log into a CKAN installation
author: Louis des Landes (Swinburne University)
homepage: https://github.com/Psykar/ckanext-aaf
github_user: Psykar
github_repo: ckanext-aaf
category: Extension
featured: 
permalink: /extension/aaf/
---


[![image](https://travis-ci.org/Psykar/ckanext-aaf.svg?branch=master)](https://travis-ci.org/Psykar/ckanext-aaf)

![image](https://coveralls.io/repos/github/Psykar/ckanext-aaf/badge.svg)

> target  
> <https://coveralls.io/r/Psykar/ckanext-aaf>

[![Downloads](https://img.shields.io/pypi/dm/ckanext-aaf.svg)](https://pypi.python.org/pypi/ckanext-aaf/)

[![Latest Version](https://img.shields.io/pypi/v/ckanext-aaf.svg)](https://pypi.python.org/pypi/ckanext-aaf/)

[![Supported Python versions](https://img.shields.io/pypi/pyversions/ckanext-aaf.svg)](https://pypi.python.org/pypi/ckanext-aaf/)

[![Development Status](https://img.shields.io/pypi/status/ckanext-aaf.svg)](https://pypi.python.org/pypi/ckanext-aaf/)

[![License](https://img.shields.io/pypi/l/ckanext-aaf.svg)](https://pypi.python.org/pypi/ckanext-aaf/)

ckanext-aaf
===========

Allows AAF (Australian Access Federation) authentication to log into a CKAN installation.

Requirements
------------

Tested with CKAN 2.5.1, should be fairly easy to port across versions as the codebase is quite small - PR's welcome! Requires an AAF 'Rapid Conect' application to be setup (see <https://rapid.aaf.edu.au/> or <https://rapid.test.aaf.edu.au/>) For a live installation, will require SSL (as AAF will not allow callbacks to a non SSL URL)

Installation
------------

To install ckanext-aaf:

1.  Activate your CKAN virtual environment, for example:

        . /usr/lib/ckan/default/bin/activate

2.  Install the ckanext-aaf Python package into your virtual environment:

        pip install ckanext-aaf

3.  Add `aaf` to the `ckan.plugins` setting in your CKAN config file (by default the config file is located at `/etc/ckan/default/production.ini`).
4.  Setup config settings (described below), required to decode the JWT tokens passed back by AAF.
5.  Restart CKAN. For example if you've deployed CKAN with Apache on Ubuntu:

        sudo service apache2 reload

Config Settings
---------------

These settings are required (the settings below will not work, register your own application!):

    # The unique URL given by AAF Rapid Connect (get one from rapid.aaf.edu.au or rapid.test.aaf.edu.au)
    ckanext.aaf.url = https://rapid.aaf.edu.au/jwt/authnrequest/research/xxxxyyyzzzz
    # The secret used to set up the above URL
    ckanext.aaf.secret = asdfasdf#$#$#$asdfasdf
    # The URL of your application, as provided to Rapid Connect (doesn't have to match the callback URL)
    # Note this must match *exactly* what was provided to Rapid Connect - check the trailing slash!
    ckanext.aaf.aud = http://myappurl.edu.au

These settings are optional:

    # Enables use of aaf's test rapid connect service https://rapid.test.aaf.edu.au 
    # (defaults to using the live one https://rapid.aaf.edu.au )
    ckanext.aaf.debug = False
    # Allows overriding of 'ckan.auth.create_user_via_web' so that AAF users can be
    # created even if normal registrations are disabled. Defaults to False
    ckanext.aaf.allow_creation_always = False

Development Installation
------------------------

To install ckanext-aaf for development, activate your CKAN virtualenv and do:

    git clone https://github.com/Psykar/ckanext-aaf.git
    cd ckanext-aaf
    pip install -e .
    pip install -r dev-requirements.txt

Running the Tests
-----------------

To run the tests, do:

    nosetests --nologcapture --with-pylons=test.ini

To run the tests and produce a coverage report, first make sure you have coverage installed in your virtualenv (`pip install coverage`) then run:

    nosetests --nologcapture --with-pylons=test.ini --with-coverage --cover-package=ckanext.aaf --cover-inclusive --cover-erase --cover-tests

Releasing a New Version of ckanext-aaf
--------------------------------------

ckanext-aaf is availabe on PyPI as <https://pypi.python.org/pypi/ckanext-aaf>. To publish a new version to PyPI follow these steps:

1.  Update the version number in the `setup.py` file. See [PEP 440](http://legacy.python.org/dev/peps/pep-0440/#public-version-identifiers) for how to choose version numbers.
2.  Create a source distribution of the new version:

        python setup.py sdist

3.  Upload the source distribution to PyPI:

        python setup.py sdist upload

4.  Tag the new release of the project on GitHub with the version number from the `setup.py` file. For example if the version number in `setup.py` is 0.0.2 then do:

        git tag -a 0.0.2
        git push --tags



