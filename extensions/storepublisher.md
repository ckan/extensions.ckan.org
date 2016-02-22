---
layout: extension
name: storepublisher
title: CKAN extension to publish public datasets in the FIWARE Store as offerings
author: CoNWeT
homepage: https://github.com/conwetlab/ckanext-storepublisher
github_user: conwetlab
github_repo: ckanext-storepublisher
category: Extension
featured: 
permalink: /extension/storepublisher/
---


CKAN Store Publisher [![Build Status](https://build.conwet.fi.upm.es/jenkins/buildStatus/icon?job=ckan_storepublisher)](https://build.conwet.fi.upm.es/jenkins/job/ckan_storepublisher/)
=====================

CKAN extension that allows users to publish datasets in the FIWARE Store (as offerings) in a simpler way. To do so, a new tab is added in the Datasets *Manage* menu that offers a form to set the basic options of the offering.

Offerings are **not** automatically published so the dataset creator must access this form and complete it in order to publish the dataset in the FIWARE Store.

**Note:** This software is intended to integrate a CKAN instance with the FIWARE Store so it won't probably work with other Stores.

Requirements
------------

* A CKAN instance able to connect to the FIWARE Store via HTTP(s)
* [FIWARE Store v0.4 or higher](https://github.com/conwetlab/wstore/)
* [OAuth2 CKAN Extension](https://github.com/conwetlab/ckanext-oauth2/). This extension is needed since the requests sent to the Store must include the OAuth2 credentials to identify the user that is creating the offering.
* Optional: [CKAN Private Dataset Extension](https://github.com/conwetlab/ckanext-privatedatasets/)


Installation
------------
Install this extension in your CKAN instance is as easy as intall any other CKAN extension.

* Download the source from this GitHub repo.
* Activate your virtual environment (generally by running `. /usr/lib/ckan/default/bin/activate`)
* Install the extension by running `python setup.py install`
* Modify your configuration file (generally in `/etc/ckan/default/production.ini`) and add `storepublisher` in the `ckan.plugins` setting. 
* In the same config file, specify the location of FIWARE Store by adding the `ckan.storepublisher.store_url` setting. In addition, you must also set the Repository used by the store. To do so, add the `ckan.storepublisher.repository` setting
* Restart your apache2 reserver (`sudo service apache2 restart`)
* That's All!

Tests
-----
This sofware contains a set of test to detect errors and failures. You can run this tests by running the following command:
```
nosetests --ckan --with-pylons=test.ini ckanext/storepublisher/tests/
```
**Note:** The `test.ini` file contains a link to the CKAN `test-core.ini` file. You will need to change that link to the real path of the file in your system (generally `/usr/lib/ckan/default/src/ckan/test-core.ini`). 

You can also generate coverage reports by running:
```
nosetests --ckan --with-xunit --with-pylons=test.ini ckanext/storepublisher/tests/ --with-coverage --cover-package=ckanext.storepublisher --cover-inclusive --cover-erase . --cover-xml

