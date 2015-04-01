---
layout: extension
name: ckanext-mapsearch
title: A CKAN extension to add an scale-aware map-centred search
author: bopen
homepage: https://github.com/bopen/ckanext-mapsearch
github_user: bopen
github_repo: ckanext-mapsearch
category: Extension
featured: 
permalink: /extension/ckanext-mapsearch/
---


CKAN Mapsearch extension
========================

ABOUT
-----

Mapsearch is a CKAN-extension to add a scale-aware, map-centered search
to the *CKAN spatial extension* [(ckanext-spatial)](https://github.com/ckan/ckanext-spatial).

![Full screenshot](https://raw.githubusercontent.com/bopen/ckanext-mapsearch/master/ckanext-mapsearch/ckanext/mapsearch/public/mapsearch_shot.png)

FEATURES
--------

Its main distinguishing factor is the scale-awareness of the
search-engine.

This scale-awareness lets you see how many results there are on 5
different scales for the same geographic area of interest, by using an
extra area field during indexing. see [this](#4-prepare-the-schema-for-the-extension) paragraph below.

![screenshot scales](https://raw.githubusercontent.com/bopen/ckanext-mapsearch/master/ckanext-mapsearch/ckanext/mapsearch/public/mapsearch_scales.png)

DEMO
----

see a working demo on [bopen.eu](http://ckan.bopen.eu/mapsearch).

INSTALLATION
------------

*ckanext-mapsearch* is installed like any ckan extension. However, as it
depends on *ckanext-spatial* to be installed, make sure mapsearch comes
after ckanext-spatial in the plugin list (see [below](#2-add-the-extension-as-a-plugin)).

It also requires solr >= 3.1, as per http://docs.ckan.org/projects/ckanext-spatial/en/latest/spatial-search.html#choosing-a-backend-for-the-spatial-search.

### 1. install the extension with pip

```
pip install -e  git+https://github.com/bopen/ckanext-mapsearch.git#egg=ckanext-mapsearch
```

### 2. add the extension as a plugin

add the plugin to the plugins-line in your configuration *.ini* file.

**NB. It must be included with, but after *spatial\_query***

```
ckan.plugins = stats text_preview resource_proxy recline_preview spatial_metadata spatial_query harvest csw_harvester ckan_harvester mapsearch
```

### 3. configure the extension

-   set the initial mapextent

    add a line to your ini-file specifying the initial map extent ([bottom-left, upper-right]). To show Europe area on loadpage add the following line:

```
ckanext.mapsearch.initial_map_extent = [[30.4806, -12.9449], [72.9295, 40.7210]]
```

-   make sure the spatial extension uses solr-spatial field as the
    backend.

    **NB.: the search-backend of the spatial extension *must* be set to
    ‘solr-spatial-field’, as with simple ‘solr’ the extension will work
    poorly and with ‘postgis’ it will not work at all!**

```
ckanext.spatial.search_backend = solr-spatial-field
```

### 4. prepare the schema for the extension

the extension needs an extra field in the solr index, add the following
line to the schema.xml file in the ‘\<fields\>’ section.

```
<fields>
    <!-- ... -->
    <field name="spatial_area" type="float" indexed="true" stored="true" />
</fields>
```

### 5. restart solr

TESTS
-----

there are few basic selenium webdriver tests in `tests` folder. 

NB: 
- You will need full working instance with a minimum of data to run the tests. 
- The tests assume you have an instance running on 'http://localhost:5000/mapsearch'. 
However, you can override this by setting the *environment variable* MAPSEARCH_INSTANCE_URL appropriately.

```
export MAPSEARCH_INSTANCE_URL="http://ckan.bopen.eu/mapsearch"
```

LICENSE
=======

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as
published by the Free Software Foundation, either version 3 of the
License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program. If not, see http://www.gnu.org/licenses/.

Acknowledgements
================
The development of this software, up to version *0.1.2*, has been partially funded by `Filas <http://www.filas.eu>`_ under `POR FESR Lazio 2007-2013 <http://porfesr.lazio.it>`_.

