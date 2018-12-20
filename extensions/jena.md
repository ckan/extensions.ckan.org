---
layout: extension
name: jena
title: Semantic data management with Apache Jena
author: Chau Nguyen - ETRI
homepage: https://github.com/etri-odp/ckanext-jena
github_user: etri-odp
github_repo: ckanext-jena
category: Extension
featured: 
permalink: /extension/jena/
---


ckanext-jena - Semantic data management extension
=================================================

ckanext-jena is an extension for enabling the semantic aspect of CKAN
with Apache Jena.

This extension provides an ability to let users store a certain semantic
resource (e.g. rdf, ttl, owl) in Apache Jena and perform SPARQL semantic
queries.

Notes:

-   Apache Jena and Fuseki server need to be running.
-   jena\_search\_sparql api can be called with `resource_id` and `q`
    parameters for semantic queries.

Requirements
------------

This extension was developed and tested under CKAN-2.7.3 and Apache
Jena-3.9.0

Installation
------------

To install ckanext-jena:

1.  Activate your CKAN virtual environment, for example:

        . /usr/lib/ckan/default/bin/activate

2.  Install the ckanext-jena Python package into your virtual
    environment:

        pip install ckanext-jena

3.  Add `jena` setting in your CKAN config file (by default the config
    file is located at `/etc/ckan/default/production.ini`) as follows:

        ckan.plugins = jena <other-plugins>
        ckan.jena.fuseki.url = http://127.0.0.1:3030/
        ckan.jena.fuseki.username = admin
        ckan.jena.fuseki.password = admin

4.  Restart CKAN. For example if you've deployed CKAN with Apache on
    Ubuntu:

        sudo service apache2 reload

Development Installation
------------------------

To install ckanext-jena for development, activate your CKAN virtualenv
and do:

    git clone https://github.com/etri-odp/ckanext-jena.git
    cd ckanext-jena
    python setup.py develop
    pip install -r dev-requirements.txt

Running the Tests
-----------------

To run the tests, do:

    nosetests --nologcapture --with-pylons=test.ini

To run the tests and produce a coverage report, first make sure you have
coverage installed in your virtualenv (`pip install coverage`) then run:

    nosetests --nologcapture --with-pylons=test.ini --with-coverage --cover-package=ckanext.jena --cover-inclusive --cover-erase --cover-tests

Registering ckanext-jena on PyPI
--------------------------------

ckanext-jena should be available on PyPI as
<https://pypi.python.org/pypi/ckanext-jena>. If that link doesn't work,
then you can register the project on PyPI for the first time by
following these steps:

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

Acknowledgements
================

This work was supported by Institute for Information & communications
Technology Promotion (IITP) grant funded by the Korea government (MSIT)
(No.2017-00253, Development of an Advanced Open Data Distribution
Platform based on International Standards)

