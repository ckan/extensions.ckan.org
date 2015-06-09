---
layout: extension
name: lire
title: CKAN extension for managing datasets relationships
author: Petar Milic
homepage: https://github.com/milicp/ckanext-lire
github_user: milicp
github_repo: ckanext-lire
category: Extension
featured: 1
permalink: /extension/lire/
---


CKAN Relations manager
======================

The ckanext-lire (LInked RElationships) extension provide GUI interface for managing datasets relationships. Each dataset is represented via graphical element. It enables previewing existing relationships between datasets. Preview can be filtered by tag, group, organization or random number of datasets. If user escapes filtering, all datasets from portal and their relations will be loaded. With given datasets, user can: create, update and delete relationships between dataset and to select dataset for which he want to obtain semantic description. Semantic description of dataset in RDF is updated, and contains a part in which his relationships is appropriately shown.

Requirements
------------

Before installing ckanext-lire, make sure that you have installed the following:

-   CKAN 2.0+

Installation
------------

Install the plugin using pip. Download it, then from the ckanext-semre directory, run

    $ pip install -e ./

This will register a plugin entry point, so you can now add the following to the `[app:main]` section of your CKAN .ini file:

    ckan.plugins = lire <other-plugins>

After you reload the site, the LIRE plugin will be available from <http://url-of-your-ckan/lire>

Using The LIRE Extension ----------------------

**LIRE**: enables user interface for managing dataset relations.

After user access LIRE, a HTML form is available for users to choose parameter by which they want to filter the display of initial datasets for working on them. Supported parameters is by tag, by organization, by group and random number of datasets. If user do not choose parameter, all datasets from portal will be loaded.

For relating datasets, user first need to choose relationship type from menu above display, and to connect two datasets. After that, user can decide whether he wants to keep relationship type he previously choosed, or to use the new one, suggested by extension. Pending actions table will then be updated. That table is available for previewing via SHOW button. End step is committing changes by clicking on COMMIT button.

:

