---
layout: extension
name: meteoswiss
title: Harvester for the Federal Office of Meteorology and Climatology MeteoSwiss
author: OGD Switzerland
homepage: https://github.com/ogdch/ckanext-meteoswiss
github_user: ogdch
github_repo: ckanext-meteoswiss
category: Extension
featured: 
permalink: /extension/meteoswiss/
---


ckanext-meteoswiss
==================

Harvester for the Federal Office of Meteorology and Climatology MeteoSwiss

Installation
------------

Use `pip` to install this plugin. This example installs it in `/home/www-data`

``` bash
source /home/www-data/pyenv/bin/activate
pip install -e git+https://github.com/ogdch/ckanext-meteoswiss.git#egg=ckanext-meteoswiss --src /home/www-data
cd /home/www-data/ckanext-meteoswiss
pip install -r pip-requirements.txt
python setup.py develop
```

Make sure to add `meteoswiss_harvest` to `ckan.plugins` in your config file.

### For development

-   install the `pre-commit.sh` script as a pre-commit hook in your local repositories:
    \*\* `ln -s ../../pre-commit.sh .git/hooks/pre-commit`

Run harvester
-------------

``` bash
source /home/www-data/pyenv/bin/activate
paster --plugin=ckanext-meteoswiss meteoswiss_harvest gather_consumer -c development.ini &
paster --plugin=ckanext-meteoswiss meteoswiss_harvest fetch_consumer -c development.ini &
paster --plugin=ckanext-meteoswiss meteoswiss_harvest run -c development.ini
```

