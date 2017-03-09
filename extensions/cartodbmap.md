---
layout: extension
name: cartodbmap
title: CartoDB resource view extension
author: OpenGov
homepage: https://github.com/opengov-opendata/ckanext-cartodbmap
github_user: opengov-opendata
github_repo: ckanext-cartodbmap
category: Extension
featured: 1
permalink: /extension/cartodbmap/
---


|                                              |
|----------------------------------------------|
| ckanext-cartodbmap (CKAN Carto ResourceView) |

Use Carto as a more powerful/performant way to visualize geospatial data in CKAN. And not just visualize, but actually start telling stories as well with round-tripping support with the Carto Builder editor.

Config Settings
===============

Add following in config settings:

    ckanext.cartodbmap.cartodb.username = <CartoDB Username Here> 
    ckanext.cartodbmap.cartodb.key = <API Key here> 

The following can also be optionally added:

Set a limit for DataStore resources. Resources with a row count higher than the limit will not have a view created, the default value is 100000:

    ckanext.cartodbmap.datastore.limit = 100000

Remove geojson\_preview from ckan.plugins list

Disable current default geojson view (removes geojson from the list):

    ckan.preview.json_formats = json gjson

Development Installation
========================

To install ckanext-cartodbmap for development, activate your CKAN virtualenv and do:

    git clone https://github.com/Ontodia/ckanext-cartodbmap.git
    cd ckanext-cartodbmap
    python setup.py develop
    pip install -r dev-requirements.txt

