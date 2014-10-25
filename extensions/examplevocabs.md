---
layout: extension
name: examplevocabs
title: Example tag vocabularies CKAN plugin
author: Sean Hammond
homepage: https://github.com/seanh/ckanext-examplevocabs
github_user: seanh
github_repo: ckanext-examplevocabs
category: Extension
featured: 
permalink: /extension/examplevocabs/
---


ckanext-examplevocabs
=====================

An example CKAN extension that adds a tag vocabulary to datasets as a custom
metadata field.

Installation
------------

1. Activate your ckan virtualenv

2. cd to the virtualenv directory

3. `git clone https://github.com/okfn/ckanext-examplevocabs.git`

4. `cd ckanext-examplevocabs`

5. `python setup.py install`

6. Add `example_vocabs_plugin` to the plugins in your CKAN ini file, e.g.:

       ckan.plugins = stats synchronous_search example_vocabs_plugin

7. From the `ckanext-examplevocabs` directory, run:

       paster vocabs create -c ../ckan/development.ini

   replacing `../ckan/development.ini` with the path to your CKAN ini file.

8. Start CKAN. Now when you create or edit a dataset, you should see an extra
   field 'Country Code' with a set selection of possible values.

