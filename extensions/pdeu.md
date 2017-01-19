---
layout: extension
name: pdeu
title: Custom CKAN Extension for PublicData
author: Open Knowledge
homepage: https://github.com/okfn/ckanext-pdeu
github_user: okfn
github_repo: ckanext-pdeu
category: Extension
featured: 
permalink: /extension/pdeu/
---


# ckanext-pdeu

Custom CKAN extension for [publicdata.eu](http://publicdata.eu/)

## How to Install Locally for Development

1. Install CKAN from source.

2. Install ckanext-pdeu. Activate your CKAN virtual environment and:

        git clone git@github.com:okfn/ckanext-pdeu.git
        cd ckanext-pdeu
        python setup.py develop
        pip install -r pip-requirements.txt

3. Add the following settings to the `[app:main]` section of your CKAN config
   file (e.g. `development.ini` or `pdeu.ini`):

        pdeu.beta = true

   and edit the following settings:

        ckan.plugins = stats dcat_api pdeu_customizations
        ckan.site_title = publicdata.eu
        ckan.site_description = Europe's Public Data

4. Run CKAN, e.g. `paster serve pdeu.ini`

Note on CKAN versions: at the time of writing the `master` branch of
ckanext-pdeu is intended to work with CKAN 2.0 (currently the `master` branch
of ckan).
The `task-migrate-to-ckan-1.7` branch of ckanext-pdeu works with CKAN 1.7.

## How to Load publicdata.eu's Apps & Ideas as CKAN Related Items

`related.json` is a dump of the Apps & Ideas (ckanext-apps extension) that were
on publicdata.eu as of 16th Oct 2012, made using the
`paster ckanext-apps-migrate dump` command. You can load the Apps & Ideas into
your CKAN database as CKAN 'Related Items' with a command like this, from your
ckanext-apps directory:

    paster ckanext-apps-migrate -c ../ckan/pdeu.ini load ../ckanext-pdeu/related.json

