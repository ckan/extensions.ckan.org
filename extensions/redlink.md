---
layout: extension
name: ckanext-redlink
title: CKAN extension to connect to Redlink triple store.
author: redlink-gmbh
homepage: https://github.com/redlink-gmbh/ckanext-redlink
github_user: redlink-gmbh
github_repo: ckanext-redlink
category: Extension
featured: 
permalink: /extension/ckanext-redlink/
---


<a href="http://redlink.co"><img src="http://redlink-gmbh.github.io/ckanext-redlink/images/banner.png" /></a>

ckanext-redlink - Redlink CKAN extension
===========================================================================

This is a CKAN extension that provides *SPARQL querying* capabilities for datasets
hosted on [Redlink](http://redlink.co) using the *data preview* feature of CKAN.

The SPARQL interface is based on [Squebi](https://github.com/tkurz/squebi).

<p align="center">
  <img src="http://redlink-gmbh.github.io/ckanext-redlink/images/ckanext-redlink-preview.png" />
</p>


Requisites
==========

* An account and a published dataset on [Redlink](https://my.redlink.io/)
* A running CKAN 2 install (only version 2.2 has been tested so far)
* A sysadmin user
* Some datasets created


Installation
============

Install the extension as usual, in your activated virtualenv:

    pip install -e "git+https://github.com/redlink-gmbh/ckanext-redlink.git#egg=ckanext-redlink"

If you want to jump straight away to the end result, just add the plugin to
your CKAN configuration file:

    ckan.plugins = redlink

Add add your Redlink [application key](http://dev.redlink.io/faq#get-key) to your CKAN configuration
file:

    [DEFAULT]
    redlink.app.key = <your-redlink-application-key>

It is recommended though that you follow the individual steps as described in
the next section.

How it works
============

Get the id of the dataset located in [my.redlink.io](https://my.redlink.io) / datasets / dataset page.

<p align="center">
  <img src="http://redlink-gmbh.github.io/ckanext-redlink/images/redlink-dataset-id.png" />
</p>

In CKAN, configure a dataset and add a resource.

<p align="center">
  <img src="http://redlink-gmbh.github.io/ckanext-redlink/images/ckan-add-new-resource.png" />
</p>

In the resource settings, set the dataset id in the *Redlink Dataset* field and the default SPARQL query in the *SPARQL*.

<p align="center">
  <img src="http://redlink-gmbh.github.io/ckanext-redlink/images/redlink-resource.png" />
</p>

If you're unsure which SPARQL query to set, you can use this general all-purpose one:
```
SELECT * WHERE {
  ?subject ?property ?object
} LIMIT 10
```

License
=======

[Apache License Version 2.0](LICENSE.txt)

