---
layout: extension
name: tdt
title: DataTank extension for CKAN
author: tdt
homepage: https://github.com/tdt/ckanext-tdt
github_user: tdt
github_repo: ckanext-tdt
category: Extension
featured: 
permalink: /extension/tdt/
---


An extension for CKAN
=====================

CKAN is a metadata platform that enables organisations to publish datasets.

This extension is a hook for each time when a dataset is added, when that dataset is proxyable through The DataTank, CKAN will automatically change the URL with a The DataTank adapter and deliver the data in XML, JSON and CSV.

Configure
---------

You need 3 extra values in your CKAN ini file (typically stored in /etc/ckan/default/development.ini)

``` ini
tdt.user = username
tdt.pass = password
tdt.host = http://yourhostname/subdir/ # mind the trailing slash!
```

