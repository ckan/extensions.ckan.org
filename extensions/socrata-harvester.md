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

A harvester to allow CKAN directories to keep in sync with a Socrata store.

In order to use this tool, you need to have the CKAN harvester extension (https://github.com/okfn/ckanext-harvest)
installed and loaded for your CKAN instance.

Building
---------

To build and use this plugin, simply:

    git clone git@github.com:socrata/socrata-harvester.git
    cd socrata-harvester
    pip install -r pip-requirements.txt
    python setup.py develop

Then you will need to update your CKAN configuration to include the new harvester.  This will mean adding the
socrata_harvester plugin as a plugin.  E.g.

    ckan.plugins = harvest socrata_harvester

Using
---------

After setting this up, you should be able to go to:
    http://localhost:5000/harvest

And have a new "Socrata" harvest type show up when creating sources.
