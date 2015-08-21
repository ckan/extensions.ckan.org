---
layout: extension
name: geonetwork
title: GeoNetwork harvester for CKAN
author: geosolutions-it
homepage: https://github.com/geosolutions-it/ckanext-geonetwork
github_user: geosolutions-it
github_repo: ckanext-geonetwork
category: Extension
featured: 
permalink: /extension/geonetwork/
---


ckanext-geonetwork
==================

GeoNetwork harvester for CKAN
-----------------------------

Main purposes:
* Handle some GeoNetwork specific coding (e.g. OGC:WMS* protocol in ``onlineResource`` maps to the specific wms ``format`` in CKAN)
* Provide mapping from GeoNetwork categories into CKAN groups
* Some schemas provide GML elements with the old namespace URI ``http://www.opengis.net/gml`` while the standard CKAN CSW harvester parses elements with the ``http://www.opengis.net/gml/3.2`` namespace. This harvester enables both URIs.
* Since GeoNetwork provides also front-end services, the harvester may build some extras fields containing URL pointing to well-known services (e.g. the extra value ``gn_view_metadata_url`` will automatically be created with a value of the related entry in geonetwork:  ``http://yourgnportal/geonetwork/srv/it/metadata.show?uuid=arw_3km_High_cloud_cover_HCY_20150323T000000000Z``).

