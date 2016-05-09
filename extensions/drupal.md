---
layout: extension
name: drupal
title: This is simple CKAN extension that works with the od_package Drupal module
author: Open Data Initiative - Initiative sur les données ouvertes
homepage: https://github.com/open-data/ckanext-drupal
github_user: open-data
github_repo: ckanext-drupal
category: Extension
featured: 
permalink: /extension/drupal/
---


ckanext-drupal
==============

This is simple CKAN extension that works with the od\_package (<https://github.com/open-data/opendata_package>) Drupal module.

Right now, this extension reads some basic package information from the Canadian Government meta-data schema and writes it into the database table (od\_package) created by the module.

For now, this package does not use SQLAlchemy and simply reads and writes directly using psycopg2.

To use this extension, it is necessary to set the configuration value "ckan.drupal.url" in your CKAN configuration file. This value provides the Postgres database URL needed to write into the table. For example: `ckan.drupal.url = postgresql://user:password@host/database`

