---
layout: extension
name: sparql
title: SPARQL Interface for Ckan
author: georgepm
homepage: https://github.com/georgepm/ckanext-sparql
github_user: georgepm
github_repo: ckanext-sparql
category: Extension
featured: 
permalink: /extension/sparql/
---


CKAN Sparql Interface Extension
-------------------------------

Note: The ``ckanext-sparql`` extension was tested using ``Virtuoso sparql instances`` such as http://semantic.ckan.net/sparql.

I will try to make it work for other type of sparql instances ;)

- **Version:** 1.01
- **Status:** Development
- **CKAN Version:** >= 2.*

Description
===========
This is a simple extension, but may be useful for someone that wants to include a Sparql Interface Editor in their CKAN instances. The idea is based on the Sparql Editor of the LODUM project from the University of Munsters Open Data initiative (http://data.uni-muenster.de/php/sparql/).

Requeriments
============

The extension use:

- ``CodeMirror`` for the code editor in the browser -> (http://codemirror.net/)

May be extended to use ``SPARQLWrapper`` (http://sparql-wrapper.sourceforge.net/) library - SPARQL Endpoint interface to Python

Installation
============
::

	$ cd /usr/lib/ckan/default/src
	$ git clone https://github.com/georgepm/ckanext-sparql.git
	$ cd ckanext-sparql/
	$ sudo python setup.py develop

Add it in your configuration file:
::

	$ vim /etc/ckan/default/production.ini

Go the plugins line and add the ``sparql_interface`` plugin
::
	ckan.plugins = sparql_interface ..... (other plugins...)

Reload Apache:
::

	$ sudo service apache2 reload
  
USE
===

Go to:
::
	http://[Custom URL]/sparql

Querys work in:
::
	http://[Custom URL]/query?query=

To send code through ``http`` to the sparql interface:
::
	http://[Custom URL]/sparql?view_code=
  
Notes
=====

You can edit the code ``templates/ckanext/sparql/index.html`` to add your custom sparql endpoint URL and default query:
::
	Line 44
	<input..... value="http://[custom url]/sparql" placeholder=".....

Then
::
	Line 54, After
	<textarea id="sparql_code" name="sparql_code"  resize="both">
	Here replace the query
  
Changelog
=========

- Version: 1.01: Fix Bugs 

Example
=======

- http://data.upf.edu/sparql

