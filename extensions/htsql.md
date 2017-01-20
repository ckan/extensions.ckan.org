---
layout: extension
name: htsql
title: An extension that enables htsql queries for the new datastore
author: Open Knowledge
homepage: https://github.com/okfn/ckanext-htsql
github_user: okfn
github_repo: ckanext-htsql
category: Extension
featured: 1
permalink: /extension/htsql/
---


ckanext-htsql
=============

An extension that enables HTSQL queries for the new datastore in CKAN. This extension adds an API endpoint `datastore_search_htsql` that allows HSQML queries on the datastore. Because of restrictions with the sql endpoint, not all HTSQL queries are possible.

[Documentation for the datastore](http://docs.ckan.org/en/latest/datastore.html)

installation
============

You need CKAN and the new datastore enabled for this extension to work. To install this extension, follow the instructions in the [CKAN documentation on extensions](http://docs.ckan.org/en/latest/extensions.html).

The basic steps are:

-   Install the extension by running `pip install ckanext-htsql`
-   Enable the extension in CKAN by adding `ckan.plugins = htsql` to your `.ini` file


