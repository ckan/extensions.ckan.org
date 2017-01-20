---
layout: extension
name: krzn
title: Custom CKAN extension for KRZN
author: Dominik Moritz
homepage: https://github.com/domoritz/ckanext-krzn
github_user: domoritz
github_repo: ckanext-krzn
category: Extension
featured: 
permalink: /extension/krzn/
---


ckanext-krzn
============

Custom CKAN extension for KRZN

How to Install Locally for Development
--------------------------------------

1.  Install CKAN from source.

2.  Install ckanext-krzn. Activate your CKAN virtual environment and:

``` bash
git clone git@github.com:okfn/ckanext-krzn.git
cd ckanext-krzn
python setup.py develop
pip install -r pip-requirements.txt
```

1.  Edit the following settings in the `[app:main]` section of your CKAN config
    file (e.g. `development.ini` or `production.ini`):

<!-- -->

    ckan.plugins = krzn

1.  Run CKAN, e.g. `paster serve production.ini`

Edit the style
--------------

After editing the less files, they need to be recompiled. This can be done by calling `ckanext/krzn/theme/less`.

