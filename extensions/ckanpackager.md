---
layout: extension
name: ckanpackager
title: A stand-alone service to pack a given CKAN resource in a ZIP file and email the link to a user
author: Natural History Museum, London
homepage: https://github.com/NaturalHistoryMuseum/ckanext-ckanpackager
github_user: NaturalHistoryMuseum
github_repo: ckanext-ckanpackager
category: Extension
featured: 
permalink: /extension/ckanpackager/
---


# ckanext-ckanpackager

[![Travis](https://img.shields.io/travis/NaturalHistoryMuseum/ckanext-ckanpackager/master.svg?style=flat-square)](https://travis-ci.org/NaturalHistoryMuseum/ckanext-ckanpackager)
[![Coveralls](https://img.shields.io/coveralls/github/NaturalHistoryMuseum/ckanext-ckanpackager/master.svg?style=flat-square)](https://coveralls.io/github/NaturalHistoryMuseum/ckanext-ckanpackager)
[![CKAN](https://img.shields.io/badge/ckan-2.9.0a-orange.svg?style=flat-square)](https://github.com/ckan/ckan)

_A CKAN extension that provides a user interface to download resources with [ckanpackager](http://github.com/NaturalHistoryMuseum/ckanpackager)._


# Overview

**This extension will not work without [ckanpackager](http://github.com/NaturalHistoryMuseum/ckanpackager).**

Ckanpackager is a stand-alone service that can be instructed to fetch data on a [CKAN](http://ckan.org) site using the datastore API, pack the data in a ZIP file and email the link to a given address. See the [ckanpackager github page](http://github.com/NaturalHistoryMuseum/ckanpackager) for more information.

The extension provides an HTML snippet that can be used to replace the Download button on resources. The new button will:
- Provide an overlay explaining the link will be sent later on;
- If anonymous downloading is enabled, provide a form for users to enter the destination email address;
- On resource pages, the button will ensure that currently applied filters and searches are forwarded on to the ckanpackager service.

This extension uses a database table in the CKAN database to store stats about packaging events.


# Installation

Path variables used below:
- `$INSTALL_FOLDER` (i.e. where CKAN is installed), e.g. `/usr/lib/ckan/default`
- `$CONFIG_FILE`, e.g. `/etc/ckan/default/development.ini`

1. Clone the repository into the `src` folder:

  ```bash
  cd $INSTALL_FOLDER/src
  git clone https://github.com/NaturalHistoryMuseum/ckanext-ckanpackager.git
  ```

2. Activate the virtual env:

  ```bash
  . $INSTALL_FOLDER/bin/activate
  ```

3. Install the requirements from requirements.txt:

  ```bash
  cd $INSTALL_FOLDER/src/ckanext-ckanpackager
  pip install -r requirements.txt
  ```

4. Run setup.py:

  ```bash
  cd $INSTALL_FOLDER/src/ckanext-ckanpackager
  python setup.py develop
  ```

5. Add 'ckanpackager' to the list of plugins in your `$CONFIG_FILE`:

  ```ini
  ckan.plugins = ... ckanpackager
  ```


# Configuration

There are two options that _must_ be specified in your .ini config file.

## **[REQUIRED]**

Name|Description|Options
--|--|--
`ckanpackager.url`|URL to the ckanpackager endpoint|
`ckanpackager.secret`|Shared secret with the ckanpackager instance|


# Further Steps

1. Initialise the database table:

  ```bash
  paster --plugin=ckanext-ckanpackager initdb -c $CONFIG_FILE
  ```

# Usage

## Actions

### `packager_stats`
Provides statistical information about the download requests made to the packager. All of the items in the `data_dict` are optional.

```python
from ckan.plugins import toolkit

data_dict = {
                'resource_id': RESOURCE_ID,
                'offset': 0,
                'limit': 100,
                'email': REQUESTER_EMAIL
            }

toolkit.get_action('packager_stats')(
    context,
    data_dict
)
```

## Commands

### `initdb`
Initialises the ckanpackager database table.

1.
    ```bash
    paster --plugin=ckanext-ckanpackager initdb -c $CONFIG_FILE
    ```

## Templates

Add the following snippet to templates where you want the button to appear:

```html+jinja
{% snippet 'ckanpackager/snippets/package_resource.html',
   res=res, pkg=pkg, bt_class="fas fa-download", bt_text=_('Download')
%}
```
