---
layout: extension
name: basemaps
title: ckanext basemaps plugin
author: 
homepage: https://github.com/gsi-cyberjapan/ckanext-basemaps
github_user: gsi-cyberjapan
github_repo: ckanext-basemaps
category: Extension
featured: 
permalink: /extension/basemaps/
---


BaseMaps for CKAN
============================================================================


* `Installation`_
* `Configuration`_

Installation
------------

**This plugin dependencies ckanext-spatial Plugin.**

The current version of ckanext-basemaps has been developed and tested again
**CKAN 2.1.x**. We assume a running CKAN 2.1.x instance.
 
The installation has the following steps, assuming you have a running
copy of CKAN:

#. Install the extension from its source repository::

    (pyenv) $ pip install -e git+https://github.com/gsi-cyberjapan/ckanext-basemaps


Configuration
-------------

These are the configuration options used by the extension 

#. Map Names::

    ckanext.basemaps.laylers.names = 地理院地図（標準）, 地理院地図（白地図）,電子国土基本図（オルソ画像）

#. Map URLs::

    ckanext.basemaps.laylers.urls = http://cyberjapandata.gsi.go.jp/xyz/std/{z}/{x}/{y}.png, http://cyberjapandata.gsi.go.jp/xyz/blank/{z}/{x}/{y}.png, http://cyberjapandata.gsi.go.jp/xyz/ort/{z}/{x}/{y}.jpg



