---
layout: extension
name: multiedit
title: Multiedit
author: Helsinki Region Infoshare
homepage: https://github.com/Helsingin-kaupungin-tietokeskus/ckanext-multiedit
github_user: Helsingin-kaupungin-tietokeskus
github_repo: ckanext-multiedit
category: Extension
featured: 
permalink: /extension/multiedit/
---


Provides CKAN with a table style display of datasets. Allows easy editing of multiple datasets simultaneously according to used form model.

Install
=======

In an activated python environment run:
pip install -e git+<https://github.com/Helsingin-kaupungin-tietokeskus/ckanext-multiedit.git#egg=ckanext-multiedit>

\[The plugin is compatible only with CKAN 2.x versions\]

Tested with: CKAN 2.1.1

Enabling
========

Enable by adding to your ckan.plugins line in CKAN config:

ckan.plugins = ... multiedit

Also add the following settings required by the plugin:

multiedit.package\_type = your.package.type
multiedit.limit = X

where X is your prefered limit for datasets shown. Note that showing and editing hundreds of datasets simultaneously
can be taxing to your server, so choose a sensible limit.

your.package.type is package type your form extension returns with package\_types() -function
(search extension development documentation <http://ckan.readthedocs.org/en/latest/extensions/index.html> for more details).
This is used for connecting your customized form to multiedit. Note: this feature has not been tested extensively,
thus only using the default "multiedit.package\_type = package" is recommended.

Usage
=====

Point your browser to: your.ckan.address/multiedit

Note that you need to be logged in to use multiedit, since it needs your apikey to make updates.
Search works just like regular CKAN search.

