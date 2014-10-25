---
layout: extension
name: datatable
title: An implementation of CKAN's IResourcePreview interface that uses the WET datatables
author: Open Data Initiative - Initiative sur les données ouvertes
homepage: https://github.com/open-data/ckanext-datatable
github_user: open-data
github_repo: ckanext-datatable
category: Extension
featured: 
permalink: /extension/datatable/
---


ckanext-datatable
=================

This is a CKAN extension that requires the WET-BOEW extension for CKAN 
(https://github.com/open-data/ckanext-wet-boew) and the core Datastore CKAN
Extension. 

ckanext-datatable implements the CKAN IPreviewResource interface 
and uses the WET Data Tables feature to provide a
preview of tabular resources that have been saved to the CKAN the datastore.

Because the CKAN IPreviewResource uses an IFRAME this version is not
suitable for use with the Canadian Open Data portal, but is made 
available for other sites that are based on the WET toolkit.

