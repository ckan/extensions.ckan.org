---
layout: extension
name: datasetversions
title: Support for different versions of a dataset
author: Aptivate
homepage: https://github.com/aptivate/ckanext-datasetversions
github_user: aptivate
github_repo: ckanext-datasetversions
category: Extension
featured: 
permalink: /extension/datasetversions/
---


ckanext-datasetversions
=======================

This CKAN extension adds support for different versions of a dataset. Sometimes is is desirable to store and display together different versions of a dataset, for example a daily situation report-style map during a humanitarian crisis.

This plugin provides an action `dataset_version_create`, for example:

    toolkit.get_action('dataset_version_create')(
        context, {
            'id': dataset['id'],
            'base_name': base_name,
            'owner_org': owner_org
        }
    )

The plugin models dataset versions internally by creating a parent dataset, with minimal metadata and no resources. A child dataset is created for each version.

`dataset_version_create` will create a parent-child relationship between the dataset specified by `base_name` and that specified by `id`. If the dataset specified by `base_name` does not exist, it will be created.

Note that this plugin overrides CKAN's `package_show` action. The original `package_show` is made available as `ckan_package_show`.

For datasets with different versions, the overridden `package_show` will return:

-   The latest, public, active version of the dataset if the parent name or id is specified
-   A specific version of the dataset if the child name or id is specified

The version ordering is determined by the integer value of `version` in the dataset metadata.

In addition, `package_show` will return a list of the names and URLs of all active versions as `_versions` in the dictionary.

The plugin provides templates to list versions of a dataset alongside that currently viewed and to warn the user if they are looking at an old version of a dataset.

Requirements
------------

This plugin will not work 'out of the box'. You will need to write code to call the `dataset_version_create` action. A site-specific example is available at <https://github.com/aptivate/ckanext-mapactionimporter>

This is known to work with CKAN 2.5.2, though note there are problems when purging datasets with relationships. See:

-   <https://github.com/ckan/ckan/pull/3112>
-   <https://github.com/ckan/ckan/issues/2186>

Installation
------------

To install ckanext-datasetversions:

1.  Activate your CKAN virtual environment, for example:

        . /usr/lib/ckan/default/bin/activate

2.  Install the ckanext-datasetversions Python package into your virtual environment:

        pip install ckanext-datasetversions

3.  Add `datasetversions` to the `ckan.plugins` setting in your CKAN config file (by default the config file is located at `/etc/ckan/default/production.ini`).
4.  Restart CKAN. For example if you've deployed CKAN with Apache on Ubuntu:

        sudo service apache2 reload

Config Settings
---------------

None

Development Installation
------------------------

To install ckanext-datasetversions for development, activate your CKAN virtualenv and do:

    git clone https://github.com/aptivate/ckanext-datasetversions.git
    cd ckanext-datasetversions
    python setup.py develop
    pip install -r dev-requirements.txt

Running the Tests
-----------------

To run the tests, do:

    nosetests --nologcapture --with-pylons=test.ini

To run the tests and produce a coverage report, first make sure you have coverage installed in your virtualenv (`pip install coverage`) then run:

    nosetests --nologcapture --with-pylons=test.ini --with-coverage --cover-package=ckanext.datasetversions --cover-inclusive --cover-erase --cover-tests

Registering ckanext-datasetversions on PyPI
-------------------------------------------

ckanext-datasetversions should be availabe on PyPI as <https://pypi.python.org/pypi/ckanext-datasetversions>. If that link doesn't work, then you can register the project on PyPI for the first time by following these steps:

1.  Create a source distribution of the project:

        python setup.py sdist

2.  Register the project:

        python setup.py register

3.  Upload the source distribution to PyPI:

        python setup.py sdist upload

4.  Tag the first release of the project on GitHub with the version number from the `setup.py` file. For example if the version number in `setup.py` is 0.0.1 then do:

        git tag 0.0.1
        git push --tags

Releasing a New Version of ckanext-datasetversions
--------------------------------------------------

ckanext-datasetversions is availabe on PyPI as <https://pypi.python.org/pypi/ckanext-datasetversions>. To publish a new version to PyPI follow these steps:

1.  Update the version number in the `setup.py` file. See [PEP 440](http://legacy.python.org/dev/peps/pep-0440/#public-version-identifiers) for how to choose version numbers.
2.  Create a source distribution of the new version:

        python setup.py sdist

3.  Upload the source distribution to PyPI:

        python setup.py sdist upload

4.  Tag the new release of the project on GitHub with the version number from the `setup.py` file. For example if the version number in `setup.py` is 0.0.2 then do:

        git tag 0.0.2
        git push --tags

About
-----

Copyright (c) 2016 [MapAction](http://mapaction.org). Developed by [Aptivate](http://aptivate.org).

Development of v1 of this plugin was funded by [ECHO](http://ec.europa.eu/echo).

!["Funded by European Union Humanitarian Aid"](http://www.echo-visibility.eu/wp-content/uploads/2014/02/EU_Flag_HA_2016_EN-300x272.png)

