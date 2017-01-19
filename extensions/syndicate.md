---
layout: extension
name: syndicate
title: Syndicate datasets to another CKAN instance
author: Aptivate
homepage: https://github.com/aptivate/ckanext-syndicate
github_user: aptivate
github_repo: ckanext-syndicate
category: Extension
featured: 
permalink: /extension/syndicate/
---


ckanext-syndicate
=================

CKAN plugin to syndicate datasets to another CKAN instance.

This plugin provides a mechanism to syndicate datasets to another instance of CKAN. If a dataset has the `syndicate` flag set to `True` in its custom metadata, any updates to the dataset will be reflected in the syndicated version. Resources in the syndicated dataset are stored as the URLs of the resources in the original. You must have the API key of a user on the target instance of CKAN. See the Config Settings section below.

Plugins can modify data sent for syndication by implementing the action `update_dataset_for_syndication` and modifying the `dataset_dict` value. This is useful if the schemas are different between CKAN instances.

Requirements
------------

-   Tested with CKAN 2.5.2
-   Requires `celery`
-   To work over SSL, requires `pyOpenSSL`, `ndg-httpsclient` and `pyasn1`
-   It may be useful to run Celery in a production environment through [supervisor](http://supervisord.org/)

Installation
------------

To install ckanext-syndicate:

1.  Activate your CKAN virtual environment, for example:

        . /usr/lib/ckan/default/bin/activate

2.  Install the ckanext-syndicate Python package into your virtual environment:

        pip install ckanext-syndicate

3.  Add `syndicate` to the `ckan.plugins` setting in your CKAN config file (by default the config file is located at `/etc/ckan/default/production.ini`).
4.  Restart CKAN. For example if you've deployed CKAN with Apache on Ubuntu:

        sudo service apache2 reload

5.  You will also need to set up celery. In a development environment this can be done with the following paster command from within your virtual environment:

        paster --plugin=ckan celeryd run -c /etc/ckan/default/development.ini

6.  In a production environment, celery can be configured through supervisor, for example `/etc/supervisor/conf.d/celery.conf`:

        [program:celery]
        autorestart=true
        autostart=true
        command=/usr/lib/ckan/default/bin/paster --plugin=ckan celeryd --config=/etc/ckan/default/production.ini
        numprocs=1
        priority=998
        redirect_stderr=true
        startsecs=10
        stderr_logfile=/var/log/celeryd.log
        stdout_logfile=/var/log/celeryd.log
        stopwaitsecs=600
        user=www-data

Config Settings
---------------

    # The URL of the site to be syndicated to
    ckan.syndicate.ckan_url = https://data.humdata.org/

    # The API key of the user on the syndicated site
    ckan.syndicate.api_key = 9efdd954-c643-444a-97a1-c9c374cef861

    # The custom metadata flag used for syndication
    # (optional, default: syndicate).
    ckan.syndicate.flag = syndicate_to_hdx

    # The custom metadata field to store the syndicated dataset ID
    # on the original dataset
    # (optional, default: syndicated_id)
    ckan.syndicate.id = hdx_id

    # A prefix to apply to the name of the syndicated dataset
    # (optional, default: )
    ckan.syndicate.name_prefix = my-prefix

    # The name of the organization on the target CKAN to use when creating
    # the syndicated datasets
    # (optional, default: None)
    ckan.syndicate.organization = my-org-name

    # The user agent
    # (optional, default: constructed from ckanapi version and url)
    ckan.syndicate.user_agent = My User Agent

Development Installation
------------------------

To install ckanext-syndicate for development, activate your CKAN virtualenv and do:

    git clone https://github.com/aptivate/ckanext-syndicate.git
    cd ckanext-syndicate
    python setup.py develop
    pip install -r dev-requirements.txt

See also Installation

Running the Tests
-----------------

To run the tests, do:

    nosetests --nologcapture --with-pylons=test.ini

To run the tests and produce a coverage report, first make sure you have coverage installed in your virtualenv (`pip install coverage`) then run:

    nosetests --nologcapture --with-pylons=test.ini --with-coverage --cover-package=ckanext.syndicate --cover-inclusive --cover-erase --cover-tests

Registering ckanext-syndicate on PyPI
-------------------------------------

ckanext-syndicate should be availabe on PyPI as <https://pypi.python.org/pypi/ckanext-syndicate>. If that link doesn't work, then you can register the project on PyPI for the first time by following these steps:

1.  Create a source distribution of the project:

        python setup.py sdist

2.  Register the project:

        python setup.py register

3.  Upload the source distribution to PyPI:

        python setup.py sdist upload

4.  Tag the first release of the project on GitHub with the version number from the `setup.py` file. For example if the version number in `setup.py` is 0.0.1 then do:

        git tag 0.0.1
        git push --tags

Releasing a New Version of ckanext-syndicate
--------------------------------------------

ckanext-syndicate is availabe on PyPI as <https://pypi.python.org/pypi/ckanext-syndicate>. To publish a new version to PyPI follow these steps:

1.  Update the version number in the `setup.py` file. See [PEP 440](http://legacy.python.org/dev/peps/pep-0440/#public-version-identifiers) for how to choose version numbers.
2.  Create a source distribution of the new version:

        python setup.py sdist

3.  Upload the source distribution to PyPI:

        python setup.py sdist upload

4.  Tag the new release of the project on GitHub with the version number from the `setup.py` file. For example if the version number in `setup.py` is 0.0.2 then do:

        git tag 0.0.2
        git push --tags



