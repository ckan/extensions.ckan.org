---
layout: extension
name: socrata-harvester
title: Socrata harvester to allow CKAN to keep in sync with a Socrata store
author: OpenDataMonitor
homepage: https://github.com/opendatamonitor/socrata-harvester
github_user: opendatamonitor
github_repo: socrata-harvester
category: Extension
featured: 
permalink: /extension/socrata-harvester/
---


socrata-harvester
=================

A harvester to allow CKAN directories to keep in sync with a catalogue that provides API in order to fetch metadata.

In order to use this tool, you need to have the ODM CKAN harvester extension (https://github.com/opendatamonitor/ckanext-harvestodm)
installed and loaded for your CKAN instance.
Tested with CKAN v2.2 (http://docs.ckan.org/en/ckan-2.2/).


General
---------

This work is based on the socrata harvester extension (https://github.com/socrata/socrata-harvester).
The socrata-harvester plugin adds support in using the mongo DB as metadata repository. Also, changes or modifications added to original
code to comply with ODM project's (www.opendatamonitor.eu) requirements (see below).


Implementation
---------------

Main modifications are:

* add extra metadata fields (language, country, catalogue_url, platform) or use existing ones in different way (metadata_created and metadata_updated are synchronised 
to our platform's timings overriding the client's) check whether a metadata record is already present in the MongoDB database, and accordingly create or update

Building
---------

To build and use this plugin, simply:

    git clone https://github.com/opendatamonitor/socrata-harvester.git
    cd socrata-harvester
    pip install -r pip-requirements.txt
    python setup.py develop

Then you will need to update your CKAN configuration to include the new harvester.  This will mean adding the
socrata_harvester plugin as a plugin.  E.g.

    ckan.plugins = harvestodm socrata_harvest

Also you need to add the odm_extension settings to the development.ini file in your ckan folder.  

    [ckan:odm_extensions]
    mongoclient=localhost
    mongoport=27017
    log_path=/var/local/ckan/default/pyenv/src/
    
Using
---------

After setting this up, you should be able to go to:
    http://localhost:5000/harvest

In case that you don't have the ckanext-htmlharvest extension installed (https://github.com/opendatamonitor/ckanext-htmlharvest)

Then go to:
    
    http://localhost:5000/harvest/new

And have a new "Socrata" harvest type show up when creating sources.


Licence
---------

This work implements the ckanext-harvest template (https://github.com/ckan/ckanext-harvest) and thus 
licensed under the GNU Affero General Public License (AGPL) v3.0 (http://www.fsf.org/licensing/licenses/agpl-3.0.html).

