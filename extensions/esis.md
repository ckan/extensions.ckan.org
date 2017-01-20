---
layout: extension
name: esis
title: Ckan extension adding additional fields and controls for spectral data
author: CSTARS
homepage: https://github.com/CSTARS/ckanext-esis
github_user: CSTARS
github_repo: ckanext-esis
category: Extension
featured: 
permalink: /extension/esis/
---


ckanext-ecosis
==============

EcoSIS extension for CKAN adding resource controls for spectra

EcoSIS Tutorials
----------------

[tutorial.ecospectra.org](http://tutorial.ecospectra.org)

CKAN 'IDE'
----------

info on pycharm package install can be found [here](http://ubuntuhandbook.org/index.php/2015/07/install-pycharm-ubuntu-1404/http://ubuntuhandbook.org/index.php/2015/07/install-pycharm-ubuntu-1404/)

#### start pycharm

    . /usr/lib/ckan/default/bin/activate
    # run ckan as root

    sudo pycharm-community

#### run setup

    select virtual env python as interpreter, then

    script = /usr/lib/ckan/default/bin/paster
    script paramters = --plugin=ckan serve /etc/ckan/default/development.ini

Allow local cross-site auth (dev only)
--------------------------------------

in ckan/lib/base.py

         def _set_cors(self):
    -        response.headers['Access-Control-Allow-Origin'] = "*"
    +        #response.headers['Access-Control-Allow-Origin'] = "*"
    +        if 'Origin' in request.headers:
    +            response.headers['Access-Control-Allow-Origin'] = request.headers['Origin']
    +        else:
    +            response.headers['Access-Control-Allow-Origin'] = "*"
    +
             response.headers['Access-Control-Allow-Methods'] = \
                 "POST, PUT, GET, DELETE, OPTIONS"
             response.headers['Access-Control-Allow-Headers'] = \
                 "X-CKAN-API-KEY, Authorization, Content-Type"

    +        response.headers['Access-Control-Allow-Credentials'] = "true"


