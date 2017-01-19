---
layout: extension
name: semantictags
title: SemanticTags for CKAN Datasets
author: Alan Tygel
homepage: https://github.com/alantygel/ckanext-semantictags
github_user: alantygel
github_repo: ckanext-semantictags
category: Extension
featured: 
permalink: /extension/semantictags/
---


ckanext-semantictags
====================

CKAN SemanticTags plugin offers the possibility for Open Data Portals to tag their datasets with semantic resources.

What can you do with the SemanticTags plugin? -------------------------------------------With the SemanticTags plugin you can:

-   Relate your CKAN tags to semantic resources;
-   Define custom RDF predicates for linking your datasets with the Linked Open Data cloud
-   Connect several CKAN instances through the use of global semantic tags

Why a SemanticTags plugin?
--------------------------

CKAN offers from core an RDF description of the set of metadata of each database. However, linking the databases to external semantic resources was not possible. SemanticTags fills this gap, allowing datasets to be tagged with LOD resources.

Screenshots
-----------

Settings - Associations between tags and registered semantic tags.

![image](http://stodap.org/tags/images/9/97/CKAN_Semantictags_Plugin.png)

Dataset - Link to tags and associated semantic tags

![image](http://stodap.org/tags/images/0/0c/CKAN_Semantictags_Plugin_-_Dataset.png)

RDF output, linking dataset to the Linked Open Data cloud.

![image](http://stodap.org/tags/images/2/2a/CKAN_Semantictags_Plugin_-_RDF.png)

### Requirements

CKAN &gt;= 2.4

### Installation

To install ckanext-semantictags:

1.  Activate your CKAN virtual environment, for example:

        . /usr/lib/ckan/default/bin/activate

2.  Install the ckanext-semantictags Python package into your virtual environment:

        pip install ckanext-semantictags

3.  Run the database migration:

        paster --plugin=ckanext-semantictags semantictags migrate -c /etc/ckan/default/production.ini   

4.  Add `semantictags` to the `ckan.plugins` setting in your CKAN config file (by default the config file is located at `/etc/ckan/default/production.ini`).
5.  Restart CKAN. For example if you've deployed CKAN with Apache on Ubuntu:

        sudo service apache2 reload

### Development Installation

To install ckanext-semantictags for development, activate your CKAN virtualenv and do:

    git clone https://github.com/alantygel/ckanext-semantictags.git
    cd ckanext-semantictags
    python setup.py develop
    paster --plugin=ckanext-semantictags semantictags migrate -c /etc/ckan/default/development.ini

Add `semantictags` to the `ckan.plugins` setting in your CKAN  
config file (by default the config file is located at `/etc/ckan/default/development.ini`).

Use
---

Navigate to yoursite/semantictags

Acknowledgements
----------------

This work was driven in the context of the research [STODaP](http://stodap.org/) project, developed at the Federal University of Rio de Janeiro (Brazil) and the University of Bonn (Germany)

