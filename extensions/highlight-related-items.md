---
layout: extension
name: highlight-related-items
title: Surface a dataset's related items more visibly
author: City of Philadelphia
homepage: https://github.com/CityOfPhiladelphia/ckanext-highlight-related-items
github_user: CityOfPhiladelphia
github_repo: ckanext-highlight-related-items
category: Extension
featured: 
permalink: /extension/highlight-related-items/
---


# ckanext-highlight-related-items
Surface a dataset's related items more visibly. Normally, a dataset page
provides a text description of the dataset and then a bunch of "resources" in
various formats. For very technical users, this is perfect. For everyone else,
visualizations and applications are far more approachable. But they're buried in
the "Related" tab. This plugin simply surfaces those items above the "resources."

![screenshot of dataset view page with related items beneath the
description](http://i.imgur.com/M8dmuPc.png)

## Installation

```
 . /usr/lib/ckan/default/bin/activate
 cd /usr/lib/ckan/default/src
 git clone https://github.com/CityOfPhiladelphia/ckanext-highlight-related-items
 cd ckanext-highlight-related-items
 python setup.py develop
```

## Note
From CKAN v2.6, Related Items has been removed from CKAN, and replaced by the [Showcase extension](https://github.com/ckan/ckanext-showcase), which works with CKAN 2.3 and above.
