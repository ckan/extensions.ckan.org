---
layout: extension
name: sourceplanet
title: CKAN extension for SourcePlanet project
author: Jon Lázaro Aduna
homepage: https://github.com/jonlazaro/ckanext-sourceplanet
github_user: jonlazaro
github_repo: ckanext-sourceplanet
category: Extension
featured: 
permalink: /extension/sourceplanet/
---


CKAN SourcePlanet Extension
===========================

**Status:** Alpha

**CKAN Version:** 1.8

The aim of [SourcePlanet project](http://dev.morelab.deusto.es/sourceplanet/) is using CKAN for managing Open Source Software Projects' metadata. For that purpouse, SourcePlanet manages three entities identifying:

-   Open Source Projects (project)
-   Open Source Products (product)
-   Organizations / Companies (organization)

As CKAN Dataset/Package model is basically based on project-like models, SourcePlanet uses it for "Project"s and "Product"s (with some modifications).

"Organization"s support is based on [ckanext-organizations extension](https://github.com/okfn/ckan/tree/master/ckanext/organizations) provided by CKAN by default.

This extension provides CKAN customization for SourcePlanet project with functionalities like:

-   New entitites project and product instead of dataset entity.
-   New forms for projects and products.
-   Quality related info in project and producs.
-   New interface according to SourcePlanet needs.
-   Preliminar modification of RDF descriptions adapting them to software project descriptions (using [DOAP ontology](https://github.com/edumbill/doap)).

Installation (not recommended)
------------------------------

To install this package, from your CKAN virtualenv, run the following from your CKAN base folder (e.g. `pyenv/`):

    pip install -e git+https://github.com/jonlazaro/ckanext-sourceplanet#egg=ckanext-sourceplanet

Then activate SourcePlanet extension (and also needed Organizations extension) by setting `ckan.plugins = sourceplanet organizations` in your main `ini`-file.

> At this moment, changes on CKAN default Package and Related controllers are required to make the extension work (not included by the moment)

