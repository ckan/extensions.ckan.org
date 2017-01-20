---
layout: extension
name: barnet
title: 
author: Open Knowledge
homepage: https://github.com/okfn/ckanext-barnet
github_user: okfn
github_repo: ckanext-barnet
category: Extension
featured: 
permalink: /extension/barnet/
---


ckanext-barnet
==============

Config, Extensions, and Themes for the Open Barnet CKAN Portal.

**Note**: This extension requires the `release-v2.2.1-barnet` branch from
<https://github.com/okfn/ckan-barnet> (contains a fix to allow custom dataset
fields and "free extras" to be used at the same time, back-ported to 2.2.1).
Once CKAN 2.3 is released the Barnet sites can be upgraded to it and won't need
a custom branch anymore.

Licenses
--------

To get the custom licenses:

    licenses_group_url =  https://open.barnet.gov.uk/licenses.json

in config file.

Themes
------

To switch themes: In plugin.py, change references to `theme_1` to `theme_2` (or vice versa).

### Theme 1

Available images

> /business.png
> /community.png
> /council.png
> /education.png
> /environment.png
> /finance.png
> /health.png
> /roads.png
> /waste.png

