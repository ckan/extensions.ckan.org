---
layout: extension
name: userdatasets
title: CKAN plugin to allow users with 'member' role within an organization to create/edit/delete their own datasets
author: U.K. Natural History Museum
homepage: https://github.com/NaturalHistoryMuseum/ckanext-userdatasets
github_user: NaturalHistoryMuseum
github_repo: ckanext-userdatasets
category: Extension
featured: 
permalink: /extension/userdatasets/
---


<img src=".github/nhm-logo.svg" align="left" width="150px" height="100px" hspace="40"/>

ckanext-userdatasets
====================

[![Travis](https://img.shields.io/travis/NaturalHistoryMuseum/ckanext-userdatasets/master.svg?style=flat-square)](https://travis-ci.org/NaturalHistoryMuseum/ckanext-userdatasets)
[![Coveralls](https://img.shields.io/coveralls/github/NaturalHistoryMuseum/ckanext-userdatasets/master.svg?style=flat-square)](https://coveralls.io/github/NaturalHistoryMuseum/ckanext-userdatasets)
[![CKAN](https://img.shields.io/badge/ckan-2.9.1-orange.svg?style=flat-square)](https://github.com/ckan/ckan)
[![Python](https://img.shields.io/badge/python-3.6%20%7C%203.7%20%7C%203.8-blue.svg?style=flat-square)](https://www.python.org/)

*A CKAN extension that allows organisation members to create datasets,
and edit or delete the datasets they have created.*

Overview
========

This extension changes the permissions of users with the 'Member' role
in an organisation, allowing them to create datasets, and to edit or
delete the datasets they have created. Unlike users with the 'Editor'
role, they cannot edit or delete datasets created by other users.

Notes:

-   This applies to the existing 'Member' role rather than creating a
    new one as it is currently not possible to add new roles from an
    extension;
-   The plugin works with custom dataset types, however it will not work
    with other plugins which override package/resource
    update/create/delete authorization functions, and
    package\_create/update actions.

**Warning: This plugin modifies CKAN's permission system. The current
implementation cannot be considered fully safe and should only be used
AT YOUR OWN RISK in a trusted environment. Ensure you run the tests with
your plugins enabled.**

Installation
============

Path variables used below:

-   `$INSTALL_FOLDER` (i.e. where CKAN is installed), e.g.
    `/usr/lib/ckan/default`
-   `$CONFIG_FILE`, e.g. `/etc/ckan/default/development.ini`

1.  Clone the repository into the `src` folder:

``` bash
cd $INSTALL_FOLDER/src
git clone https://github.com/NaturalHistoryMuseum/ckanext-userdatasets.git
```

1.  Activate the virtual env:

``` bash
. $INSTALL_FOLDER/bin/activate
```

1.  Install the requirements from requirements.txt:

``` bash
cd $INSTALL_FOLDER/src/ckanext-userdatasets
pip install -r requirements.txt
```

1.  Run setup.py:

``` bash
cd $INSTALL_FOLDER/src/ckanext-userdatasets
python setup.py develop
```

1.  Add 'userdatasets' to the list of plugins in your `$CONFIG_FILE`:

``` ini
ckan.plugins = ... userdatasets
```

Configuration
=============

There are no configuration options for this extension.

Usage
=====

Actions
-------

No new actions are defined in this extension; three are overridden to
modify validators and permissions.

### `package_create`

### `package_update`

### `organization_list_for_user`

Testing
=======

*Test coverage is currently extremely limited.*

To run the tests in this extension, there is a Docker compose
configuration available in this repository to make it easy.

To run the tests against ckan 2.9.x on Python3:

1.  Build the required images

``` bash
docker-compose build
```

1.  Then run the tests. The root of the repository is mounted into the
    ckan container as a volume by the Docker compose configuration, so
    you should only need to rebuild the ckan image if you change the
    extension's dependencies.

``` bash
docker-compose run ckan
```

The ckan image uses the Dockerfile in the `docker/` folder which is
based on `openknowledge/ckan-dev:2.9`.

Note that currently the tests mock the Datacite API and therefore don't
require an internet connection nor your Datacite credentials to run.

