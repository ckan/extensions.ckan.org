---
layout: extension
name: ckanext-geoserver
title: Geoserver Extension for CKAN
author: ngds
homepage: https://github.com/ngds/ckanext-geoserver
github_user: ngds
github_repo: ckanext-geoserver
category: Extension
featured: 
permalink: /extension/ckanext-geoserver/
---


###Geoserver Extension for CKAN

custom configurations:

geoserver.rest_url = 'geoserver://admin:geoserver@localhost:8080/geoserver/rest'
geoserver.default_workspace = 'ckan'
geoserver.workspace_uri = 'http://localhost:5000/ckan'

Also requires this to be set:

ckan.datastore.write_url = 'postgresql://ckanuser:pass@localhost/datastore'
