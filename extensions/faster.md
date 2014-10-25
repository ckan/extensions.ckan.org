---
layout: extension
name: faster
title: A CKAN extension that makes CKAN run faster
author: Sean Hammond
homepage: https://github.com/seanh/ckanext-faster
github_user: seanh
github_repo: ckanext-faster
category: Extension
featured: 
permalink: /extension/faster/
---


ckanext-faster
==============

A CKAN extension that makes CKAN run faster.

So far, all this does is insert the `'return_id_only' = True` option into the
context for the `package_create` and `package_update` actions, but other
optimizations could be added.

See [Performance tips for large imports](https://github.com/okfn/ckan/wiki/Performance-tips-for-large-imports)
for more CKAN performance tips.


Installation
------------

Activate your CKAN virtualenv, then run:

    pip install -e 'git+https://github.com/seanh/ckanext-faster.git#egg=ckanext-faster'

