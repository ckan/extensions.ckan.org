---
layout: extension
name: zhstat
title: Harvester for the Statistical Office of Canton of Zurich
author: OGD Switzerland
homepage: https://github.com/ogdch/ckanext-zhstat
github_user: ogdch
github_repo: ckanext-zhstat
category: Extension
featured: 
permalink: /extension/zhstat/
---


ckanext-zhstat
==============

Harvester for the Statistical Office of Canton of Zurich

Installation
------------

Use `pip` to install this plugin. This example installs it in `/home/www-data`

``` bash
source /home/www-data/pyenv/bin/activate
pip install -e git+https://github.com/ogdch/ckanext-zhstat.git#egg=ckanext-zhstat --src /home/www-data
cd /home/www-data/ckanext-zhstat
pip install -r pip-requirements.txt
python setup.py develop
```

Make sure to add `zhstat` and `zhstat_harvester` to `ckan.plugins` in your config file.

### For development

-   install the `pre-commit.sh` script as a pre-commit hook in your local repositories:
    \*\* `ln -s ../../pre-commit.sh .git/hooks/pre-commit`

Run harvester
-------------

``` bash
source /home/www-data/pyenv/bin/activate
paster --plugin=ckanext-zhstat harvester gather_consumer -c development.ini &
paster --plugin=ckanext-zhstat harvester fetch_consumer -c development.ini &
paster --plugin=ckanext-zhstat harvester run -c development.ini
```

