---
layout: extension
name: ytp-main
title: Avoindata main CKAN extension
author: yhteentoimivuuspalvelut
homepage: https://github.com/yhteentoimivuuspalvelut/ckanext-ytp-main
github_user: yhteentoimivuuspalvelut
github_repo: ckanext-ytp-main
category: Extension
featured: 
permalink: /extension/ytp-main/
---


ckanext-ytp-main
================

Main CKAN extension for avoindata.fi

Installation
------------

Requires celery. See [ckanext-ytp-tasks](https://github.com/yhteentoimivuuspalvelut/ckanext-ytp-tasks).

This project requires files from [ytp-assets-common](https://github.com/yhteentoimivuuspalvelut/ytp-assets-common).

    git clone https://github.com/yhteentoimivuuspalvelut/ytp-assets-common.git
    sudo cp ytp-assets-common/resources /var/www/resource

Installed as CKAN extension: ytp\_user ytp\_dataset ytp\_organizations ytp\_theme

    git clone https://github.com/yhteentoimivuuspalvelut/ckanext-ytp-main.git
    cd ckanext-ytp-user
    python setup.py develop # or install with pip

Add *ytp\_user* *ytp\_dataset* *ytp\_organizations* *ytp\_theme* to CKAN plugins `/etc/ckan/default/production.ini` and restart the server.

[See how to install CKAN extensions.](http://docs.ckan.org/en/latest/extensions/tutorial.html#installing-the-extension)

Configuration
-------------

Add *ckanext.ytp.organizations.default\_organization\_name* and *ckanext.ytp.organizations.default\_organization\_title* variables to ckan ini file.

    ckanext.ytp.organizations.default_organization_name = "default_organization"
    ckanext.ytp.organizations.default_organization_title = "Default Organization"

Credits
-------

This extension uses parts of [ckanext-hierarchy](https://github.com/datagovuk/ckanext-hierarchy).

