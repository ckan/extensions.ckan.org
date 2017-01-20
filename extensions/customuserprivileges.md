---
layout: extension
name: customuserprivileges
title: Fine-tune who can edit dataset whether it's unowned or organization owned
author: cphsolutionslab, fadeit ApS (http://fadeit.dk)
homepage: https://github.com/cphsolutionslab/ckanext-customuserprivileges
github_user: cphsolutionslab
github_repo: ckanext-customuserprivileges
category: Extension
featured: 
permalink: /extension/customuserprivileges/
---


ckanext-customuserprivileges
============================

ckanext-customuserprivileges is [CKAN](https://github.com/ckan/ckan) extension for adding additional restrictions for dataset management. It adds an extra autocomplete field to the dataset to specify users who can administer it. This works for both unowned datasets that by default can be managed by any authenticated user and datasets within company which requires the member to have sufficient permissions within the company and additionally be a manager.

Installing
----------

**NB! This module is developed on CKAN v2.4.0, compatibility with other version is not ensured**
1) Clone this repository

``` sh
#activate virtualenv
source /usr/lib/ckan/default/bin/activate
cd /usr/lib/ckan/default/src
https://github.com/cphsolutionslab/ckanext-customuserprivileges
cd ckanext-customuserprivileges
python setup.py develop
sudo nano /etc/ckan/default/production.ini
# Enable plugin in configuration
# ckan.plugins = datastore ... customuserprivileges
```

Usage
-----

Extra field for specifying dataset administrators is visible when creating or editing the dataset. Users will be specified by their username.![Extra field](https://i.imgur.com/HVG2ofP.png)

By default when creating a dataset and not specifying any administrators, only the user who created it can manage it. For other users following applies:

Unowned dataset + dataset administrator = **can edit**

Company dataset + admin or editor within company + dataset administrator = **can edit**

Running tests
-------------

    #activate virtualenv
    source /usr/lib/ckan/default/bin/activate
    #install test dependencies
    pip install -r /usr/lib/ckan/default/src/ckan/dev-requirements.txt
    #create test database (if not created)
    sudo -u postgres createdb -O ckan_default ckan_test -E utf-8
    #edit test database connection string
    nano /usr/lib/ckan/default/src/ckan/test-core.ini
    #enter extension directory
    cd /usr/lib/ckan/default/src/ckanext-customuserprivileges
    #run test suite
    nosetests --ckan --with-pylons=test.ini ckanext/customuserprivileges/tests --nocapture

