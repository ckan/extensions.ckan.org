---
layout: extension
name: ckanext-vegaview
title: VegaJS' view extension for CKAN
author: Open Knowledge
homepage: https://github.com/okfn/ckanext-vegaview
github_user: okfn
github_repo: ckanext-vegaview
category: Extension
featured: 
permalink: /extension/ckanext-vegaview/
---


CKAN Vega Extension
===================

This plugin allows you to use VegaJS, a visualization grammar, to create graphs
for CKAN resources.

Requirements
------------

* DataPusher
* Resource View Branch

Installing
----------

Inside your pyenv, install using pip:

```
pip install -e git+git://github.com/okfn/ckanext-vegaview.git#egg=ckanext-vegaview
```

Then activate it by adding ```vegaview``` inside ```ckan.plugins``` in your .ini file.

Using
-----

First of all, the resource you want to create a graph for needs to be in
datapusher. Make sure it is, before proceeding.

To create a new view, you simply need to add Vega's specification to the
```Specification``` field. The resource's data is available in a ```data```
variable to be used in the specification. For example:

```
{
  ...
  "data": [
    {
      "name": "gold_prices",
      "values": data
    }
  ],
  ...
}
```

If needed, you can debug its format by inspecting the view page's HTML.

