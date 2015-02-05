---
layout: extension
name: ckanext-userdatasets
title: CKAN plugin to allow users with 'member' role within an organization to create/edit/delete their own datasets
author: U.K. Natural History Museum
homepage: https://github.com/NaturalHistoryMuseum/ckanext-userdatasets
github_user: NaturalHistoryMuseum
github_repo: ckanext-userdatasets
category: Extension
featured: 
permalink: /extension/ckanext-userdatasets/
---


ckanext-userdatasets
====================

Overview
--------

A CKAN extension to allow organization members to create datasets, and edit or delete the datasets they have created.

This extension changes the permissions of users with the 'Member' role in an organization allowing them to create
datasets, and to edit or delete the datasets they have created. Unlike users with the 'Editor' role, they cannot
edit or delete datasets created by other users.

Notes: 
- This applies to the existing 'Member' role rather than creating a new one as it is currently not possible to add
  new roles from an extension;
- The plugin works with custom dataset types, however it will not work with other plugins which override 
  package/resource update/create/delete authorization functions, and package_create/update actions.
  
**Warning: This plugin modifies CKAN's permission system. The current implementation cannot be considered fully
 safe and should only be used AT YOUR OWN RISK in a trusted environment. Ensure you run the tests with your plugins
 enabled.**

Compatibility
-------------

- v0.1 for CKAN 2.2

Configuration
-------------

The following configuration directives are available:

- `userdatasets.default_auth_module`: The name of the module that holds the default implementation of the auth 
                                      functions. Only change this if you know what you are doing! Defaults to 
                                      `ckan.logic.auth`
- `userdatasets.default_action_module`: The name of the module that holds the default implementation of the action
                                        functions. Only change this if you know what you are doing! Defaults to 
                                        `ckan.logic.actin`


Usage
-----

1. Install the package *in your ckan virtual environment*: 

```sh
    pip install git+https://github.com/NaturalHistoryMuseum/ckanext-userdatasets#egg=ckanext-userdatasets
```


2. Add `userdatasets` to `ckan.plugins` in your configuration file. 

Testing
-------

The plugin contains both unit tests and functional tests. From the source directory, run:

```sh
    nosetests --ckan --with-pylons=test.ini ckanext/userdatasets/tests
```

This assumes that ckan's test.ini is in ../ckan/test.ini. Adjust accordingly.
