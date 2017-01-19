---
layout: extension
name: ogdch
title: CKAN templates and translations for opendata
author: OGD Switzerland
homepage: https://github.com/ogdch/ckanext-ogdch
github_user: ogdch
github_repo: ckanext-ogdch
category: Extension
featured: 
permalink: /extension/ogdch/
---


ckanext-ogdch
=============

CKAN templates and translations for opendata.admin.ch

## Installation

Use `pip` to install this plugin. This example installs it in `/home/www-data`

```bash
source /home/www-data/pyenv/bin/activate
pip install -e git+https://github.com/ogdch/ckanext-ogdch.git#egg=ckanext-ogdch --src /home/www-data
cd /home/www-data/ckanext-ogdch
python setup.py develop
```

Make sure to add `ogdch` to `ckan.plugins` in your config file.

### For development
* install the `pre-commit.sh` script as a pre-commit hook in your local repositories:
** `ln -s ../../pre-commit.sh .git/hooks/pre-commit`


