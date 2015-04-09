---
layout: extension
name: ckanext-semre
title: CKAN extension for RDF description of dataset relationships
author: Petar Milic
homepage: https://github.com/milicp/ckanext-semre
github_user: milicp
github_repo: ckanext-semre
category: Extension
featured:  
permalink: /extension/ckanext-semre/
---


CKAN Extension for RDF Description of Dataset Relationships
===========================================================


The ckanext-semre (SEManticRElationships) extension will give RDF description of CKAN dataset relationships
when user request RDF desrciption of dataset (for example, when user access 
http://datahub.io/dataset/frb-linked-data.rdf)


Requirements
------------

Before installing ckanext-semre, make sure that you have installed the following:

* CKAN 2.0+

Installation
------------

Install the plugin using pip. Download it, then from the ckanext-qa directory, run

::

    $ pip install -e ./

This will register a plugin entry point, so you can now add the following 
to the ``[app:main]`` section of your CKAN .ini file:

::

    ckan.plugins = semre <other-plugins>

After you reload the site, the SEMRE plugin will do the job http://url-of-your-ckan/dataset/dataset-name.rdf

Using The SEMRE Extension
----------------------

**SEMRE**: give RDF description of CKAN dataset relationships.

::

    http://url-of-your-ckan/dataset/dataset-name.rdf
    
Simply access to RDF description of dataset via URL example given above.
 
::
 

