---
layout: extension
name: ckanext-dgu-local
title: Support for harvesting from Local Authorities
author: Data.Gov.UK - Cabinet Office
homepage: https://github.com/datagovuk/ckanext-dgu-local
github_user: datagovuk
github_repo: ckanext-dgu-local
category: Extension
featured: 
permalink: /extension/ckanext-dgu-local/
---


# ckanext-dgu-local

This extension provides support for harvesting from Local Authority data portal that exposes datasets according to the LGA Inventory spec: https://github.com/datagovuk/ckanext-dgu-local/blob/master/ckanext/dgulocal/data/inventory.xsd . 

This currently has dependencies on UK specific data, but the extension should work if the inventory document doesn't reference the UK specific publisher and temporal URLs.


## Dependencies

The LGA Inventory harvester relies on this version of ckanext-harvest:

    https://github.com/datagovuk/ckanext-harvest/tree/1508-update

## Installation

For development you should install ckanext-dgu-local as follows.

1. Install this extension as normal using pip in your activated environment:

    (pyenv) $ pip install -e "git+https://github.com/datagovuk/ckanext-dgu-local.git#egg=ckanext-dgu-local"

2. Activate the plugins by adding them to the CKAN config and then restarting CKAN:

    ckan.plugins = ...other_plugins... dgu_local lga_harvester

3. Setup the database tables:

    paster --plugin=ckanext-dgu-local dgulocal init --config=ckan_default.ini


## Plugins

`dgu_local` will provide any UI/search enhancements

`lga_harvester` is used for harvesting from the LGA Inventory format.


## Running tests

The tests for ckanext-dgu-local can be run from the ckanext-dgu-local folder using:

    nosetests --ckan --with-pylons=test-core.ini ckanext/dgulocal/tests

And some tests do not use the database so can be run in sqlite:

    nosetests --ckan --with-pylons=test.ini ckanext/dgulocal/tests/test_harvester.py


## Metadata

This extension relies on PackageExtras being added to packages that are created, or updated.  The Extras used the identifier field for a given publisher which is documented as being unique for that publisher (but no necessarily globally unique).

### Package Extras

|Key|Value|
|--|--|
|lga_identifier|The publisher-wide unique identifier for this dataset|
|lga_services|A JSON list of service URL/Label pairs|
|lga_functions|A JSON list of function URL/Label pairs|

### Group (publisher) Extras

|Key|Value|
|--|--|
|geo_boundary|The GEOJson describing the polygon within which this authority lives - not used in this release|


## Licence

(c) Crown Copyright
Code in this repository is subject to Crown Copyright and licensed under the GNU Affero General Public License (AGPL) v3.0.

AGPL terms: http://www.fsf.org/licensing/licenses/agpl-3.0.html


