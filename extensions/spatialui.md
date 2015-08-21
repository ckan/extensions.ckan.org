---
layout: extension
name: spatialui
title: Map and search map support for ckanext-spatial
author: XVTSolutions
homepage: https://github.com/XVTSolutions/ckanext-spatialUI
github_user: XVTSolutions
github_repo: ckanext-spatialUI
category: Extension
featured: 
permalink: /extension/spatialui/
---


ckanext-spatialUI
=============

This extension provides the UI elements for spatial search. 

+ Spatial search widget
+ Dataset extent map

These UI elements are not part of ckanext-spatial and need to be added to templates as part of an extension as is [described here](http://docs.ckan.org/projects/ckanext-spatial/en/latest/spatial-search.html#spatial-search-widget). This extension provides these elements.

Installation
------------
> Requires [ckanext-spatial](https://github.com/ckan/ckanext-spatial) to be installed and configured for spatial search. [See these instructions](http://docs.ckan.org/projects/ckanext-spatial/en/latest/spatial-search.html#spatial-search) for configuring spatial search. 

Using the default ckan installation directory

```
cd /usr/lib/ckan/default/src
git clone https://github.com/XVTSolutions/ckanext-spatialUI
cd ckanext-spatialUI
python setup.py develop
```
Add this to your CKAN configuration file 

```plugins = ... spatialUI```

Restart apache

