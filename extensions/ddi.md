---
layout: extension
name: ddi
title: DDI import tool for CKAN
author: Kata team repository
homepage: https://github.com/kata-csc/ckanext-ddi
github_user: kata-csc
github_repo: ckanext-ddi
category: Extension
featured: 
permalink: /extension/ddi/
---


============================================
DDI2 parser command and harvester for CKAN
============================================

This extension for ckanext-harvester enables the parsing of a DDI2 metadata
source to having them as datasets for CKAN.

Paster parsing command (Not implemented yet!)
---------------------------------------------

The parser is quite simple to use, it has 2 modes, first single file/url or second
a URL/file to a list of urls. 

Mode 1:

    paster ddi_import fetch http://www.fsd.uta.fi/fi/aineistot/luettelo/FSD1008/FSD1008.xml --config=../ckan/development.ini

Mode 2:
 
    paster ddi_import multifile http://www.fsd.uta.fi/fi/aineistot/luettelo/fsd-ddi-records-uris-fi.txt --config=../ckan/development.ini

Harvester configuration
-----------------------

Please make sure you have ckanext-harvester installed. In the harvester source 
addition/edition UI, please add the URL in which the XML files for DDI2 reside.

Configuration options:
 *  limit: Import only first 'limit' number of XML files.

Here is an example of a configuration object (the one that must be entered in
the configuration field)::

    {
     "limit": 10,
    }

