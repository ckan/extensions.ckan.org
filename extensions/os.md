---
layout: extension
name: os
title: Ordnance Survey Widgets for DGU - CKAN Extension
author: Data.Gov.UK and Ordnance Survey
homepage: https://github.com/datagovuk/ckanext-os
github_user: datagovuk
github_repo: ckanext-os
category: Extension
featured: 
permalink: /extension/os/
---


OS Widgets for DGU - CKAN Extension
===================================

This extension contains the Map Based Search and Map Preview pages, seen on data.gov.uk and developed in the main by Ordnance Survey.

Licence
-------

All of this code is [c] Crown Copyright. Ordnance Survey developed the search and preview widgets, which were integrated into this CKAN extension by Cabinet Office.

This software is licensed pursuant to the terms of the BSD 3 Clause License, which can be found at: <http://opensource.org/licenses/BSD-3-Clause>

Although the code is open source, the mapping and gazetteer services at osinspiremappingprod.ordnancesurvey.co.uk are provided by Ordnance Survey exclusively for data.gov.uk use in support of UKLII. Please contact Ordnance Survey for details of their commercially-provided mapping services.

Install & Configuration
-----------------------

To install this extension's code into your pyenv:

    pip install -e git+https://github.com/datagovuk/ckanext-os#egg=ckanext-os

Now configure the parts of the extension that you want to enable, using the instructions in the sections below.

Widgets
-------

To enable the OS widgets, in your CKAN config add to ckan.plugins items, as follows:

    ckan.plugins = os_search os_preview

To improve performance of the geoserver WFS calls (for boundary information) configure a proxy in the Apache config (osinspiremappingprod.ordnancesurvey.co.uk is used here as an example only - it is for data.gov.uk use only):

    ProxyPass /geoserver/ http://osinspiremappingprod.ordnancesurvey.co.uk/geoserver/
    ProxyPassReverse /geoserver/ http://osinspiremappingprod.ordnancesurvey.co.uk/geoserver/

and enable Apache modules: `mod_proxy` and `mod_proxy_http`:

    sudo a2enmod proxy_http

To configure the servers used in the widgets, put the following lines in your ckan configuration file and change the values from the defaults shown (osinspiremappingprod.ordnancesurvey.co.uk is used here as an example only - it is for data.gov.uk use only):

    ckanext-os.geoserver.host = osinspiremappingprod.ordnancesurvey.co.uk
    ckanext-os.gazetteer.host = osinspiremappingprod.ordnancesurvey.co.uk
    ckanext-os.libraries.host = osinspiremappingprod.ordnancesurvey.co.uk
    ckanext-os.tiles.url = http://osinspiremappingprod.ordnancesurvey.co.uk/geoserver/gwc/service/wms
    ckanext-os.wms.url = /geoserver/wms
    ckanext-os.wfs.url = /geoserver/wfs
    ckanext-os.geoserver.apikey = 

Preview List
------------

This extension provides an API to help store a 'shopping basket'-style list of packages to preview. You can add and remove items from it and request a list.

### Examples

Add: a request to `api/2/util/preview_list/add/-municipal-waste-generation-in-england-from-2000-01-to-2009-10` adds this package to the list. The package can be specified as either an ID or name. The response is the full preview list (JSON-encoded).

Remove: a request to `api/2/util/preview_list/remove/-municipal-waste-generation-in-england-from-2000-01-to-2009-10` then removes it again. Again the response contains the full list.

List: You can also just request the list using `/api/2/util/preview_list`.

In an HTML template the list can be accessed as: `${session.get('preview_list', []}`

Spatial Database
----------------

Spatial Database allows map preview of data in CKAN that has geo-references (lat/longs, post codes etc). (Some datasets are in WMS format and can be previewed directly, without need for this functionality.)

There is a wrapper to call the Spatial Ingester, which is a Java tool that converts the data (usually CSV/XLS) and stores it in a PostGIS database. This data is served in WFS format for display in the Map Preview tool. It is currently in development.

The Spatial Ingester (Java tool) 'os-spatialingester' needs to be installed alongside this module - i.e. in the same folder as ckanext-os.

Configuration:

> ckan.plugins = os\_wfs\_server ckanext-os.spatial-datastore.sqlalchemy.url = postgresql://username:<password@localhost/spatial-db> ckanext-os.spatial-datastore.jdbc.url = jdbc:postgresql://localhost/spatial-db?user=username&password=password ckanext-os.spatial-ingester.filepath = /home/co/pyenv\_dgu/src/os-spatialingester/spatial.ingester

Creating the PostGIS database:

> owner=username db=spatial-db sudo -u postgres createdb -E UTF8 -O $owner $db sudo -u postgres psql -d $db -f /usr/share/postgresql/9.1/contrib/postgis-1.5/postgis.sql && sudo -u postgres psql -d $db -f /usr/share/postgresql/9.1/contrib/postgis-1.5/spatial\_ref\_sys.sql sudo -u postgres psql $db -c "ALTER TABLE geometry\_columns OWNER TO $owner; ALTER TABLE spatial\_ref\_sys OWNER TO $owner" sudo -u postgres psql -d $db -U $owner -h localhost -f ../os-spatialingester/spatial.ingester.ddl \# NB input the db user password

Note: the last command will start off with about 6 errors such as 'ERROR: relation "feature" does not exist' before going onto to create the tables. (The setup deletes tables first before regenerating them, so can be run again should the model change.)

Libraries
---------

In avoidance of doubt, here are the libraries and version numbers used by the Search and Preview Widgets.

-   jquery 1.7.1 - <http://jquery.com/>
-   underscore 1.1.6 - <http://underscorejs.org/>
-   backbone 0.5.1 - <http://backbonejs.org/>
-   bootstrap 2.0.3 - <http://twitter.github.com/bootstrap/>
-   ext-3.4.0 - <http://www.sencha.com/products/extjs3>
-   GeoExt 1.1 - <http://www.geoext.org/>
-   Open Layers 2.12 (85b836d)
-   proj4js-1.0.3 - <http://trac.osgeo.org/proj4js/>

Tests
-----

For the OS server tests you need to provide this option in your development.ini:

> ckanext-os.test.prod-apikey = \<key\>

Run the tests like this:

    nosetests --ckan --with-pylons=ckanext-os/test-core.ini ckanext-os/ckanext/os/tests/

