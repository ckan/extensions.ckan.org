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
* Handle some GeoNetwork specific coding (e.g. protocol in ``onlineResource`` may map to specific ``format``, ``mimetype`` CKAN fields)
* Provide other heuristics tailored to GeoNetwork metadata handling (license, …)
* Some schemas may provide GML elements with the namespace URI ``http://www.opengis.net/gml/3.2`` while the standard CKAN CSW harvester parses elements with the ``http://www.opengis.net/gml`` namespace. This should be configurable.
* Since GeoNetwork provides also front-end services, the harvester may build some extras fields containing URL pointing to well-known services.

