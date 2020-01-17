---
layout: extension
name: userdatasets
title: CKAN plugin to allow users with 'member' role within an organization to create/edit/delete their own datasets
author: Natural History Museum, London
homepage: https://github.com/NaturalHistoryMuseum/ckanext-userdatasets
github_user: NaturalHistoryMuseum
github_repo: ckanext-userdatasets
category: Extension
featured: 
permalink: /extension/userdatasets/
---


# ckanext-userdatasets

[![Travis](https://img.shields.io/travis/NaturalHistoryMuseum/ckanext-userdatasets/master.svg?style=flat-square)](https://travis-ci.org/NaturalHistoryMuseum/ckanext-userdatasets)
[![Coveralls](https://img.shields.io/coveralls/github/NaturalHistoryMuseum/ckanext-userdatasets/master.svg?style=flat-square)](https://coveralls.io/github/NaturalHistoryMuseum/ckanext-userdatasets)
[![CKAN](https://img.shields.io/badge/ckan-2.9.0a-orange.svg?style=flat-square)](https://github.com/ckan/ckan)

_A CKAN extension that allows organisation members to create datasets, and edit or delete the datasets they have created._


# Overview

This extension changes the permissions of users with the 'Member' role in an organisation, allowing them to create
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


# Installation

Path variables used below:
- `$INSTALL_FOLDER` (i.e. where CKAN is installed), e.g. `/usr/lib/ckan/default`
- `$CONFIG_FILE`, e.g. `/etc/ckan/default/development.ini`

1. Clone the repository into the `src` folder:

  ```bash
  cd $INSTALL_FOLDER/src
  git clone https://github.com/NaturalHistoryMuseum/ckanext-userdatasets.git
  ```

2. Activate the virtual env:

  ```bash
  . $INSTALL_FOLDER/bin/activate
  ```

3. Install the requirements from requirements.txt:

  ```bash
  cd $INSTALL_FOLDER/src/ckanext-userdatasets
  pip install -r requirements.txt
  ```

4. Run setup.py:

  ```bash
  cd $INSTALL_FOLDER/src/ckanext-userdatasets
  python setup.py develop
  ```

5. Add 'userdatasets' to the list of plugins in your `$CONFIG_FILE`:

  ```ini
  ckan.plugins = ... userdatasets
  ```

# Configuration

These are the options that can be specified in your .ini config file. It's not recommended to change these settings unless you know what you're doing!

Name|Description|Options|Default
--|--|--|--
`ckanext.userdatasets.default_auth_module`|Module that holds the default implementation of the auth functions.||`ckan.logic.auth`
`ckanext.userdatasets.default_action_module`|Module that holds the default implementation of the action functions.||`ckan.logic.action`


# Usage

## Actions

No new actions are defined in this extension; three are overridden to modify validators and permissions.

### `package_create`

### `package_update`

### `organization_list_for_user`
