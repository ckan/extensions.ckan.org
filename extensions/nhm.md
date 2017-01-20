---
layout: extension
name: nhm
title: CKAN extension for data
author: Natural History Museum
homepage: https://github.com/NaturalHistoryMuseum/ckanext-nhm
github_user: NaturalHistoryMuseum
github_repo: ckanext-nhm
category: Extension
featured: 
permalink: /extension/nhm/
---


ckanext-nhm
===========

CKAN extension for data.nhm.ac.uk

paster datastore update-stats -c /etc/ckan/default/development.ini

echo 'flush\_all' | nc localhost 11211

Requirements
============

Shapely&lt;1.3 is added as a requirement but is not used by ckanext-nhm.

This is to fix a bug with ckanext-spatial trying to install an incompatible version.

See <https://github.com/ckan/ckanext-spatial/issues/94>.

