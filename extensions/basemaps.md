---
layout: extension
name: ckanext-basemaps
title: ckanext basemaps plugin
author: 
homepage: https://github.com/gsi-cyberjapan/ckanext-basemaps
github_user: gsi-cyberjapan
github_repo: ckanext-basemaps
category: Extension
featured: 
permalink: /extension/ckanext-basemaps/
---


BaseMaps for CKAN
=================

-   Installation\_
-   Configuration\_

Installation
------------

**This plugin dependencies ckanext-spatial Plugin.**

The current version of ckanext-basemaps has been developed and tested again **CKAN 2.1.x**. We assume a running CKAN 2.1.x instance.

The installation has the following steps, assuming you have a running copy of CKAN:

1.  Install the extension from its source repository:

        (pyenv) $ pip install -e git+https://github.com/gsi-cyberjapan/ckanext-basemaps

Configuration
-------------

These are the configuration options used by the extension

1.  Map Names:

        ckanext.basemaps.laylers.names = &#22320;&#29702;&#38498;&#22320;&#22259;&#65288;&#27161;&#28310;&#65289;, &#22320;&#29702;&#38498;&#22320;&#22259;&#65288;&#30333;&#22320;&#22259;&#65289;,&#38651;&#23376;&#22269;&#22303;&#22522;&#26412;&#22259;&#65288;&#12458;&#12523;&#12477;&#30011;&#20687;&#65289;

2.  Map URLs:

        ckanext.basemaps.laylers.urls = http://cyberjapandata.gsi.go.jp/xyz/std/{z}/{x}/{y}.png, http://cyberjapandata.gsi.go.jp/xyz/blank/{z}/{x}/{y}.png, http://cyberjapandata.gsi.go.jp/xyz/ort/{z}/{x}/{y}.jpg



