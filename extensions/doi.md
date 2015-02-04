---
layout: extension
name: ckanext-doi
title: CKAN extension for assigning a digital object identifier (DOI) to datasets
author: U.K. Natural History Museum
homepage: https://github.com/NaturalHistoryMuseum/ckanext-doi
github_user: NaturalHistoryMuseum
github_repo: ckanext-doi
category: Extension
featured: 
permalink: /extension/ckanext-doi/
---


ckanext-doi
===========

CKAN extension for assigning a digital object identifier (DOI) to datasets, using DataCite DOI service.

ckanext.doi.account_name 
ckanext.doi.account_password
ckanext.doi.publisher = 
ckanext.doi.prefix = 
ckanext.doi.test_mode = True or False
ckanext.doi.site_url =  # Defaults to ckan.site_url if not set 

On launch, delete all test DOIs:

paster delete-test-doi -c /etc/ckan/default/development.ini



