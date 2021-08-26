---
layout: extension
name: silk
title: A plugin to integrate Silk Link Discovery Framework into CKAN
author: memaldi
homepage: https://github.com/memaldi/ckanext-silk
github_user: memaldi
github_repo: ckanext-silk
category: Extension
featured: 
permalink: /extension/silk/
---


ckanext-silk
============

A plugin to integrate Silk Link Discovery Framework into CKAN.

Tested with CKAN 1.8

Installation
------------

**Install plugin**

    python setup.py install
        

**Update CKAN development.ini file to load the plugin**

    ckan.plugins = stats silk

**Initialize new tables on CKAN database (Change user & pass)**

    python ckanext/silk/model/initDB.py

**Silk installation**

Download Silk from
<a href="http://wifo5-03.informatik.uni-mannheim.de/bizer/silk/" class="uri">http://wifo5-03.informatik.uni-mannheim.de/bizer/silk/</a>.
Tested with version 2.5.3

Extract file to some system directory

Add plugin configuration variables to CKAN development.ini

    [plugin:silk]
    silk_home = 'some_dir/silk_2.5.3'

**Celery task queue initialization** This plugin uses Celery
(<a href="http://celeryproject.org/" class="uri">http://celeryproject.org/</a>)
for task queueing.

Start the CKAN instance

    paster serve development.ini

Start the Celery server

    paster celeryd run

Entidades financiadoras
-----------------------

**Ministerio de Ciencia e Innovación, Subprograma INNPACTO 2011
(IPT-2011- 0949 -430000)**

![Ministerio de Economía y
Competitividad](https://www.fundacionctic.org/sites/default/files/images/2011-Web-EconomiaC-63px2.jpg)
![Programa
INNPACTO](https://www.fundacionctic.org/sites/default/files/images/innpacto.jpeg)
![Fondo Europeo de Desarrollo
Regional](https://www.fundacionctic.org/sites/default/files/images/feder.jpg)

