---
layout: extension
name: ckanext-noregistration
title: Plugin to disable user registration on a CKAN instance
author: OGD Switzerland
homepage: https://github.com/ogdch/ckanext-noregistration
github_user: ogdch
github_repo: ckanext-noregistration
category: Extension
featured: 
permalink: /extension/ckanext-noregistration/
---


ckanext-noregistration
======================

Plugin to disable user registration on a CKAN instance (based on [this answer on StackOverflow](http://stackoverflow.com/questions/18171937/ckan-prevent-user-from-auto-registering/18183850#18183850))

## Installation

Use `pip` to install this plugin. This example installs it in `/home/www-data`

```bash
source /home/www-data/pyenv/bin/activate
pip install -e git+https://github.com/ogdch/ckanext-noregistration.git#egg=ckanext-noregistration --src /home/www-data
cd /home/www-data/ckanext-noregistration
python setup.py develop
```

Make sure to add `noregistration` to `ckan.plugins` in your config file.

### For development
* install the `pre-commit.sh` script as a pre-commit hook in your local repositories:
** `ln -s ../../pre-commit.sh .git/hooks/pre-commit`

