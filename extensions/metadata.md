---
layout: extension
name: metadata
title: SPARQL endpoint analyzer and metadata generator for CKAN
author: unaguil
homepage: https://github.com/unaguil/ckanext-metadata
github_user: unaguil
github_repo: ckanext-metadata
category: Extension
featured: 
permalink: /extension/metadata/
---


ckanext-metadata
================

SPARQL endpoint analyzer and metadata generator for CKAN.

Tested with CKAN 1.8

 Installation
--------------

**Install plugin**

    python setup.py install
    
**Update CKAN development.ini file to load the plugin**

    ckan.plugins = stats metadata

**Initialize new tables on CKAN database (Change user & pass)**

    python ckanext/metadata/model/initDB.py

**Add plugin configuration variables to CKAN development.ini**

Append this configuration snippet to the file. Do not forget to **change the admin API** key with yours.

	[plugin:metadata]
	#admin api key used for connection from celery
	# change this API key
	api_key = xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx

	#run every s seconds, for debugging purposes
	#run_every = 30

	#metadata analyzer task cron
	cron_hour = 03
	cron_minute = 00

Also check that CKAN site URL is configured. For example

    ckan.site_url = http://127.0.0.1:5000	
    
**Apply patch to CKAN code for adding periodic task support to paster launcher**

Copy patch content from https://gist.github.com/4547407 to a file named *beat_support.patch*
and execute next line on CKAN source directory

    git apply beat_support.patch
    
**Celery task queue initialization**
This plugin uses Celery (http://celeryproject.org/) for task queueing. 

Start the CKAN instance

    paster serve development.ini
    
Start the Celery server

    paster celeryd run beat


Entidades financiadoras
------------------------

 **Ministerio de Ciencia e Innovación, Subprograma INNPACTO 2011 (IPT-2011- 0949 -430000)**
 
 ![Ministerio de Economía y Competitividad](https://www.fundacionctic.org/sites/default/files/images/2011-Web-EconomiaC-63px2.jpg) ![Programa INNPACTO](https://www.fundacionctic.org/sites/default/files/images/innpacto.jpeg) ![Fondo Europeo de Desarrollo Regional](https://www.fundacionctic.org/sites/default/files/images/feder.jpg)

