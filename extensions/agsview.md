---
layout: extension
name: agsview
title: Resource viewer display ESRI ArcGIS Map services (cached, dynamic) and Feature layer services in CKAN
author: AppGeo
homepage: https://github.com/AppGeo/ckanext-agsview
github_user: AppGeo
github_repo: ckanext-agsview
category: Extension
featured: 
permalink: /extension/agsview/
---


ckanext-agsview - Esri ArcGIS Server CKAN resources
===================================================

This extension contains view plugins to display ArcGIS Map services (cached, dynamic) and Feature layer services in CKAN. It uses an [Esri Leaflet Viewer](https://github.com/Esri/esri-leaflet) for display.

Available plugins
-----------------

-   [ArcGIS Feature Layer Viewer (ags\_fs\_view)]()
-   [ArcGIS MapService Viewer (ags\_ms\_view)]()

### ArcGIS Feature Layer Viewer (ags\_fs\_view)

The ArcGIS Feature Layer Viewer provides access to different ArcGIS Feature Layers within a MapService or FeatureService. Each instance of a view has the following configuration options:

-   \`ags\_url\`: ArcGIS Server layer end point with layer id included:

        http://gis.cityofboston.gov/arcgis/rest/services/CityServices/OpenData/MapServer/0

-   \`basemap\_url\`: Can accept [Esri basemap name](http://esri.github.io/esri-leaflet/api-reference/layers/basemap-layer.html) or generic tile url template:

        Gray

        http://gis.cityofboston.gov/arcgis/rest/services/Basemaps/base_map_webmercatorV2/MapServer/tile/{z}/{x}/{y}

### ArcGIS MapService Viewer (ags\_ms\_view)

The ArcGIS MapServer Viewer provides access to MapService and the ability to set which layers are to view within that MapService. Each instance of a view has the following configuration options:

-   \`ags\_url\`: ArcGIS Server MapService end point:

        http://gis.cityofboston.gov/arcgis/rest/services/CityServices/OpenData/MapServer

-   \`list\_ids\`: Comma delimited list of ids to include in the map (an empty list will return all the layers):

        0,5

-   \`basemap\_url\`: Can accept [Esri basemap name](http://esri.github.io/esri-leaflet/api-reference/layers/basemap-layer.html) or generic tile url template:

        Gray

        http://gis.cityofboston.gov/arcgis/rest/services/Basemaps/base_map_webmercatorV2/MapServer/tile/{z}/{x}/{y}

Configuration Options (.ini)
----------------------------

**ckanext.agsview.default\_basemap\_url**

Can accept [Esri basemap name](http://esri.github.io/esri-leaflet/api-reference/layers/basemap-layer.html) or generic tile url template:

    ckanext.agsview.default_basemap_url = Gray

    ckanext.agsview.default_basemap_url = http://example.com/MapServer/tile//{z}/{x}/{y}

Installation
------------

To install ckanext-agsview on a production site:

1.  Activate your CKAN virtual environment, for example:

        . /usr/lib/ckan/default/bin/activate

2.  Install the ckanext-agsview Python package into your virtual environment:

        pip install ckanext-agsview

3.  Add `ags_fs_view` and/or `ags_ms_view` to the `ckan.plugins` setting in your CKAN config (ini) file (by default the config file is located at `/etc/ckan/default/production.ini`):

        ckan.plugins = ... ags_fs_view ags_ms_view

4.  Restart CKAN. For example if you've deployed CKAN with Apache on Ubuntu:

        sudo service apache2 reload

Development Installation
------------------------

To install ckanext-agsview for development:

1.  Clone the source:

        cd /usr/lib/ckan/default/src
        git clone https://github.com/ckan/ckanext-agsview.git

2.  Activate your CKAN virtual environment, for example:

        . /usr/lib/ckan/default/bin/activate

3.  Install the ckanext-agsview Python package into your python virtual environment:

        cd ckanext-agsview
        python setup.py develop

4.  Continue with the main installation instructions above (step 3 onwards).

### Quick development Install

1.  Copy the following code into a shell script named **setup-agsview.sh** and update the paths as needed:

        . /usr/lib/ckan/default/bin/activate
        cd ~/projects/ckanext-agsview/
        python setup.py develop
        sed -i.bak -e "s/ckan.plugins = /ckan.plugins = ags_fs_view ags_ms_view /g" /etc/ckan/default/production.ini
        sed -i.bak '/^ckan.plugins/a ckanext.ags_view_default_basemap_url = Gray' /etc/ckan/default/production.ini
        sudo service apache2 reload

2.  Run the shell script from the command line:

        sh setup-agsview.sh



