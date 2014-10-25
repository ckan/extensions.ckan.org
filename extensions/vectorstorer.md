---
layout: extension
name: vectorstorer
title: CKAN extension to upload vector geospatial data, store and publish through OGC services
author: PublicaMundi
homepage: https://github.com/PublicaMundi/ckanext-vectorstorer
github_user: PublicaMundi
github_repo: ckanext-vectorstorer
category: Extension
featured: 
permalink: /extension/vectorstorer/
---


CKAN Vector Storer Extension
============================


Overview
--------

Vector Storer is a CKAN extension that allows users to upload vector geospatial data, store and publish through OGC services.


Installation
------------

**1.  Install required Debian packages**

Install compression-related libraries

    $ sudo apt-get install unzip unrar p7zip-full

Install GDAL libraries and Python bindings (at system-level):

    $ sudo apt-get install python-gdal   

**2.  Install CKAN extension**

    $ git clone https://github.com/PublicaMundi/ckanext-vectorstorer.git
    $ python setup.py develop
    $ pip install -r pip-requirements.txt


Configuration
-------------

**1.  Enabling Vector Storer**

  To enable the Vector Storer Extension add this to ckan plugins in the config file :
 
        ckan.plugins = vectorstorer

    
**2.  Vector Storer config options**

  The following should be set in the CKAN config :

        # ckanext-vectorstorer settings
        ckanext-vectorstorer.geoserver_url= (e.g. http://ckan_services_server/geoserver)
        ckanext-vectorstorer.geoserver_workspace= (e.g. CKAN)
        ckanext-vectorstorer.geoserver_admin= (e.g. admin)
        ckanext-vectorstorer.geoserver_password= (e.g. geoserver)
        ckanext-vectorstorer.geoserver_ckan_datastore=(e.g. ckan_datastore_default)
        ckanext-vectorstorer.gdal_folder= (e.g. /usr/lib/python2.7/dist-packages)

  Geoserver workspace and datastore have to be created in advance. The datastore must be connected to the CKAN datastore database.

**3.  Datastore configuration**

  Enable the postgis extension in the Datastorer database


