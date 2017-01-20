---
layout: extension
name: ogdch_actions
title: Additional action APIs for opendata
author: OGD Switzerland
homepage: https://github.com/ogdch/ckanext-ogdch_actions
github_user: ogdch
github_repo: ckanext-ogdch_actions
category: Extension
featured: 
permalink: /extension/ogdch_actions/
---


ckanext-ogdch\_actions
======================

Additional action APIs for opendata.admin.ch

Installation
------------

Use `pip` to install this plugin. This example installs it in `/home/www-data`

``` bash
source /home/www-data/pyenv/bin/activate
pip install -e git+https://github.com/ogdch/ckanext-ogdch_actions.git#egg=ckanext-ogdch_actions --src /home/www-data
cd /home/www-data/ckanext-ogdch-actions
python setup.py develop
```

Make sure to add `ogdch_actions` to `ckan.plugins` in your config file.

### For development

-   install the `pre-commit.sh` script as a pre-commit hook in your local repositories:
    \*\* `ln -s ../../pre-commit.sh .git/hooks/pre-commit`


