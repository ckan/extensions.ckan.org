---
layout: extension
name: ckanext-semantic
title: integration of lodstats and personalization features based on it
author: Sven R. Kunze
homepage: https://github.com/srkunze/ckanext-semantic
github_user: srkunze
github_repo: ckanext-semantic
category: Extension
featured: 
permalink: /extension/ckanext-semantic/
---


Extracting semantic data of CKAN -- ckanext-semantic
====================================================

*A extension for CKAN*
----------------------

**Features**

> -   enhanced search (search after vocabularies, classes, properties, geographical and temporal coverage)
> -   new search type: SPARQL
> -   new subscription type: SPARQL subscriptions
> -   enriched dataset page (used vocabularies, geographical and temporal coverage)
> -   similar datasets
> -   personalized recommendations

**Installation instructions**

> -   install Virtuoso v6
> -   install FedX v2 (in case of more than 1 endpoint)
> -   apply db.sql file to add necessary tables
> -   install LODStats and Redland rdflib:
>
>         pip install -e git+https://github.com/srkunze/ckanext-semantic#egg=ckanext-semantic
>         pip install -e git+https://github.com/srkunze/LODStats#egg=lodstats
>
> -   add to your CKAN configuration file:
>
>         # add this to your plugins
>         ckan.plugins = semantic
>
>         # constants for dataset statistics update
>         ckan.semantic.waiting_time = 1
>         ckan.semantic.ratio_old_new = 0.4
>
>         # credentials for sparql clients (for delete and insert)
>         # pattern: SPARQL_{attribute}_{role}; attribute in [username, password, hostname]; role in [root]
>         ckan.semantic.SPARQL_username_root = dba
>         ckan.semantic.SPARQL_password_root = dba
>         ckan.semantic.SPARQL_hostname_root = localhost
>
>         # federation tool fedX required
>         ckan.semantic.FedX = {path to your FedX}/lib/*
>
>         # endpoints
>         # pattern: SPARQL_endpoint# from 0 to 20
>         ckan.semantic.SPARQL_endpoint1 = http://localhost:8890/sparql
>         ckan.semantic.SPARQL_endpoint1_name = CKAN Store
>         ckan.semantic.SPARQL_endpoint2 = http://dbpedia.org/sparql
>         ckan.semantic.SPARQL_endpoint2_name = DBPedia Store
>
> -   create CRON jobs to run these commands on a periodical basis:
>
>         paster semantic update_dataset_due_statistics --config=../ckan/development.ini
>         paster semantic update_dataset_statistics {dataset_name} --config=../ckan/development.ini
>         paster semantic update_vocabulary_statistics --config=../ckan/development.ini
>
> -   you may need a key for cloudmade; add it here:
>
>         ckanext-semantic/ckanext/semantic/theme/public/javascript/package/semantic.js
>         ckanext-semantic/ckanext/semantic/theme/public/javascript/search/semantic.js
>
------------------------------------------------------------------------

Copyright and License
=====================

&#169; 2013 Sven R. Kunze

Licensed under the GNU Affero General Public License (AGPL) v3.0

<http://www.fsf.org/licensing/licenses/agpl-3.0.html>

