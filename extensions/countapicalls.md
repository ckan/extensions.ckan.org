---
layout: extension
name: ckanext-countapicalls
title: Simple API dataset hits counter
author: Alexandre Bulté
homepage: https://github.com/abulte/ckanext-countapicalls
github_user: abulte
github_repo: ckanext-countapicalls
category: Extension
featured: 
permalink: /extension/ckanext-countapicalls/
---


CKAN Count API Calls Extension
==============================

**Status:** Development

**CKAN Version:** 1.XXX


Overview
--------

A CKAN extension for counting and storing in DB the number of call to the "show" API for a given dataset (package).

Installation
------------

1. Install the extension as usual, e.g. (from an activated virtualenv):

		$ pip install -e  XXX


2. Run the following command from ``src/ckanext-countapicalls`` to
   set up the required database tables (of course, altering the
   ``--config`` option to point to your site config file)::

		paster initdb --config=../ckan/development.ini

3. Restart CKAN (e.g. by restarting Apache) <- do we need that ??

4. Make some calls to the API and watch the DB table 'api_package_stats', it should contain stats about your API hits.

Testing
-------

XXX

Future
------

XXX
