---
layout: extension
name: resourceauthorizer
title: ACL-based permission control at resource-level
author: Chau Nguyen - ETRI
homepage: https://github.com/etri-odp/ckanext-resourceauthorizer
github_user: etri-odp
github_repo: ckanext-resourceauthorizer
category: Extension
featured: 
permalink: /extension/resourceauthorizer/
---


ckanext-resourceauthorizer - Resource authorizing extension
===========================================================

Resourceauthorizer is a extension for enalbing the acl-based permission control at resource-level in CKAN, which currently only support role-based access permission at dataset-level.

This extension provides an ability to let users specify who (users or organizations) can or cannot access a certain resource.

Notes:

-   Access permission setting for an organization will affect all members of the organization.
-   Extension always uses access permission at user-level as the final decision if there exist both rules for user and organization.
-   Allowing user/organization to access a resource will enable the access of the dataset metadata for that user/organization.

![image](https://drive.google.com/uc?id=1QUiZNw96luC8uE8ujy1cF4N8F_sYYQgV)

Requirements
------------

This extension was developed and tested under CKAN-2.7.3

Installation
------------

To install ckanext-resourceauthorizer:

1.  Activate your CKAN virtual environment, for example:

        . /usr/lib/ckan/default/bin/activate

2.  Install the ckanext-resourceauthorizer Python package into your virtual environment:

        pip install ckanext-resourceauthorizer

3.  Add `resourceauthorizer` to the `ckan.plugins` setting in your CKAN config file (by default the config file is located at `/etc/ckan/default/production.ini`).
4.  Restart CKAN. For example if you've deployed CKAN with Apache on Ubuntu:

        sudo service apache2 reload

Config Settings
---------------

Run the following command to create the necessary tables in the database (ensuring the pyenv is activated):

    (pyenv) $ paster --plugin=ckanext-resourceauthorizer resourceauthorizer initdb --config=/etc/ckan/default/production.ini

Run the following command to reindex the CKAN metadata in solr (ensuring the pyenv is activated):

    (pyenv) $ paster --plugin=ckan search-index rebuild --config=/etc/ckan/default/production.ini

Finally, restart CKAN to have the changes take affect:

> sudo service apache2 restart

Development Installation
------------------------

To install ckanext-resourceauthorizer for development, activate your CKAN virtualenv and do:

    git clone https://github.com/etri-odp/ckanext-resourceauthorizer.git
    cd ckanext-resourceauthorizer
    python setup.py develop
    pip install -r dev-requirements.txt

Running the Tests
-----------------

To run the tests, do:

    nosetests --nologcapture --with-pylons=test.ini

To run the tests and produce a coverage report, first make sure you have coverage installed in your virtualenv (`pip install coverage`) then run:

    nosetests --nologcapture --with-pylons=test.ini --with-coverage --cover-package=ckanext.resourceauthorizer --cover-inclusive --cover-erase --cover-tests

Registering ckanext-resourceauthorizer on PyPI
----------------------------------------------

ckanext-resourceauthorizer should be availabe on PyPI as <https://pypi.python.org/pypi/ckanext-resourceauthorizer>. If that link doesn't work, then you can register the project on PyPI for the first time by following these steps:

1.  Create a source distribution of the project:

        python setup.py sdist

2.  Register the project:

        python setup.py register

3.  Upload the source distribution to PyPI:

        python setup.py sdist upload

4.  Tag the first release of the project on GitHub with the version number from the `setup.py` file. For example if the version number in `setup.py` is 0.0.1 then do:

        git tag 0.0.1
        git push --tags

Acknowledgements
================

This work was supported by Institute for Information & communications Technology Promotion (IITP) grant funded by the Korea government (MSIT) (No.2017-00253, Development of an Advanced Open Data Distribution Platform based on International Standards)

