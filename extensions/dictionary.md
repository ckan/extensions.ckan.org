---
layout: extension
name: dictionary
title: Data Dictionaries for Datasets
author: Heinz/CMU Capstone Team
homepage: https://github.com/cmuphillycapstone/ckanext-dictionary
github_user: cmuphillycapstone
github_repo: ckanext-dictionary
category: Extension
featured: 
permalink: /extension/dictionary/
---


|--------------------|
| ckanext-dictionary |

The extension adds the ability to include a data dictionary (metadata) for each dataset. Admins can create the data dictionary when adding the dataset, or create/modify it any other time. Users see the data dictionary as another tab for each dataset. Since this dictionary extension utilizes the DataStore extension, Data Dictionary information can be accessed via API.

![Additional stage added to dataset setup](https://github.com/cmuphillycapstone/ckanext-dictionary/blob/master/screenshots/admin-setup.png?raw=true)

*Additional stage added to dataset setup*

![Editing data dictionary for a dataset](https://github.com/cmuphillycapstone/ckanext-dictionary/blob/master/screenshots/admin-edit.png)

*Editing data dictionary for a dataset*

![User view of the data dictionary](https://github.com/cmuphillycapstone/ckanext-dictionary/blob/master/screenshots/user-view.png)

*User view of the data dictionary*

Requirements
============

The extension requires the DataStore extension to also be installed. Additionally, it only works on CKAN versions that have two current stages in the 'add dataset' dialog.

Installation
============

To install ckanext-dictionary:

1.  Activate your CKAN virtual environment, for example:

        . /usr/lib/ckan/default/bin/activate

2.  Install the ckanext-dictionary Python package into your virtual environment:

        pip install ckanext-dictionary

3.  Add `dictionary` to the `ckan.plugins` setting in your CKAN config file (by default the config file is located at `/etc/ckan/default/production.ini`).
4.  Restart CKAN. For example if you've deployed CKAN with Apache on Ubuntu:

        sudo service apache2 reload

Config Settings
===============

This version includes no user config settings.

Development Installation
========================

To install ckanext-dictionary for development, activate your CKAN virtualenv and do:

    git clone https://github.com/cmuphillycapstone/ckanext-dictionary.git
    cd ckanext-dictionary
    python setup.py develop
    pip install -r dev-requirements.txt

Running the Tests
=================

There are presently no tests included with the extension.

----------------------------------------Releasing a New Version of ckanext-dictionary ----------------------------------------

ckanext-dictionary is availabe on PyPI as <https://pypi.python.org/pypi/ckanext-dictionary>. To publish a new version to PyPI follow these steps:

1.  Update the version number in the `setup.py` file. See [PEP 440](http://legacy.python.org/dev/peps/pep-0440/#public-version-identifiers) for how to choose version numbers.
2.  Create a source distribution of the new version:

        python setup.py sdist

3.  Upload the source distribution to PyPI:

        python setup.py sdist upload

4.  Tag the new release of the project on GitHub with the version number from the `setup.py` file. For example if the version number in `setup.py` is 0.0.2 then do:

        git tag 0.0.2
        git push --tags



