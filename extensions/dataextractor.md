---
layout: extension
name: dataextractor
title: Alternate Data Explorer Resource View with Filtering UI
author: Energinet.dk
homepage: https://gitlab.com/energinet/eds/ckanext-dataextractor
github_user: energinet
github_repo: eds
category: Extension
featured: 
permalink: /extension/dataextractor/
---


[![image](https://travis-ci.com/ViderumGlobal/ckanext-dataextractor.svg?token=pzRbH1jQsFTh9wzwvJtq&branch=master)](https://travis-ci.com/ViderumGlobal/ckanext-dataextractor)

[![image](https://coveralls.io/repos/viderumglobal/ckanext-dataextractor/badge.svg)](https://coveralls.io/r/viderumglobal/ckanext-dataextractor)

[![Downloads](https://pypip.in/download/ckanext-dataextractor/badge.svg)](https://pypi.python.org/pypi//ckanext-dataextractor/)

[![Latest Version](https://pypip.in/version/ckanext-dataextractor/badge.svg)](https://pypi.python.org/pypi/ckanext-dataextractor/)

[![Supported Python versions](https://pypip.in/py_versions/ckanext-dataextractor/badge.svg)](https://pypi.python.org/pypi/ckanext-dataextractor/)

[![Development Status](https://pypip.in/status/ckanext-dataextractor/badge.svg)](https://pypi.python.org/pypi/ckanext-dataextractor/)

[![License](https://pypip.in/license/ckanext-dataextractor/badge.svg)](https://pypi.python.org/pypi/ckanext-dataextractor/)

  -----------------------
  ckanext-dataextractor
  -----------------------

Requirements
============

For example, you might want to mention here which versions of CKAN this
extension works with.

Installation
============

To install ckanext-dataextractor:

1.  Activate your CKAN virtual environment, for example:

        . /usr/lib/ckan/default/bin/activate

2.  Install the ckanext-dataextractor Python package into your virtual
    environment:

        pip install ckanext-dataextractor

3.  Add `dataextractor` to the `ckan.plugins` setting in your CKAN
    config file (by default the config file is located at
    `/etc/ckan/default/production.ini`).
4.  Restart CKAN. For example if you\'ve deployed CKAN with Apache on
    Ubuntu:

        sudo service apache2 reload

Config Settings
===============

Add Azure storage account settings:

    ckanext.dataextractor.azure_storage_account_name = ...
    ckanext.dataextractor.azure_storage_account_key = ...
    ckanext.dataextractor.azure_storage_container_name = ...

Add blobs expiration in days config:

    ckanext.dataextractor.blob_expiration_days = ...

Add resource rows per page limit, default max is 10:

    ckanext.dataextractor.resource_rows_limit = ...

Add pagination pages shown limit, default max is 6:

    ckanext.dataextractor.pagination_limit = ...

Limit the number of records shown when using datastore\_resource\_search
action (defaults to 10000):

    ckanext.dataextractor.default_search_limit = ...

Setup query timeout limit (in milliseconds) for datastore read- only
account (defaults to 60000):

    ckanext.dataextractor.query_timeout = ...

Override default search limit and retrieve/download all data for a given
resource (defaults to False):

    ckanext.dataextractor.enable_full_download = ...

Change datastore root url shown in the examples in Data API window:

    ckanext.dataextractor.datastore_root_url = ...

Development Installation
========================

To install ckanext-dataextractor for development, activate your CKAN
virtualenv and do:

    git clone https://github.com/viderumglobal/ckanext-dataextractor.git
    cd ckanext-dataextractor
    python setup.py develop
    pip install -r dev-requirements.txt

Documentation
=============

In order to view the documentation for all API actions open
`documentation/index.html`.

If you want to update or rebuild the documentation please visit the
[guide for writing
documentation](http://docs.ckan.org/en/latest/contributing/documentation.html).

Running the Tests
=================

To run the tests, do:

    nosetests --nologcapture --with-pylons=test.ini

To run the tests and produce a coverage report, first make sure you have
coverage installed in your virtualenv (`pip install coverage`) then run:

    nosetests --nologcapture --with-pylons=test.ini --with-coverage --cover-package=ckanext.dataextractor --cover-inclusive --cover-erase --cover-tests

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--Registering
ckanext-dataextractor on PyPI
\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

ckanext-dataextractor should be availabe on PyPI as
<https://pypi.python.org/pypi/ckanext-dataextractor>. If that link
doesn\'t work, then you can register the project on PyPI for the first
time by following these steps:

1.  Create a source distribution of the project:

        python setup.py sdist

2.  Register the project:

        python setup.py register

3.  Upload the source distribution to PyPI:

        python setup.py sdist upload

4.  Tag the first release of the project on GitHub with the version
    number from the `setup.py` file. For example if the version number
    in `setup.py` is 0.0.1 then do:

        git tag 0.0.1
        git push --tags

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--Releasing
a New Version of ckanext-dataextractor
\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

ckanext-dataextractor is availabe on PyPI as
<https://pypi.python.org/pypi/ckanext-dataextractor>. To publish a new
version to PyPI follow these steps:

1.  Update the version number in the `setup.py` file. See [PEP
    440](http://legacy.python.org/dev/peps/pep-0440/#public-version-identifiers)
    for how to choose version numbers.
2.  Create a source distribution of the new version:

        python setup.py sdist

3.  Upload the source distribution to PyPI:

        python setup.py sdist upload

4.  Tag the new release of the project on GitHub with the version number
    from the `setup.py` file. For example if the version number in
    `setup.py` is 0.0.2 then do:

        git tag 0.0.2
        git push --tags
