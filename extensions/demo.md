---
layout: extension
name: demo
title: ckan demo site extension
author: Open Knowledge
homepage: https://github.com/okfn/ckanext-demo
github_user: okfn
github_repo: ckanext-demo
category: Extension
featured: 
permalink: /extension/demo/
---


CKANEXT-DEMO
============

CKAN 2.0 demo theme.

Installation
------------

    git clone https://github.com/okfn/ckanext-demo
    cd ckanext-demo
    pip install -e .
    pip install -r pip-requirements.txt

In the CKAN config file, enable the demo and dataset\_extent\_map plugins
(the latter is found in ckanext-spatial).

