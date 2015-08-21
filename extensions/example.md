---
layout: extension
name: example
title: CKAN Extension that demonstrates some common patterns for customising a CKAN instance
author: Open Knowledge
homepage: https://github.com/okfn/ckanext-example
github_user: okfn
github_repo: ckanext-example
category: Extension
featured: 1
permalink: /extension/example/
---


This CKAN Extension demonstrates some common patterns for customising a CKAN instance.

It comprises:

-   A CKAN Extension "plugin" at `ckanext/example/plugin.py` which, when loaded, overrides various settings in the core `ini`-file to provide:
    -   A path to local customisations of the core templates and stylesheets
    -   A "stream filter" that replaces arbitrary strings in rendered templates
    -   A "route" to override and extend the default behaviour of a core CKAN page
-   A custom Pylons controller for overriding some core CKAN behaviour
-   A custom Package edit form
-   A custom Group edit form
-   A plugin that allows for custom forms to be used for datasets based on their "type".
-   A custom User registration and edition form
-   Some simple template customisations

Installation
============

To install this package, from your CKAN virtualenv, run the following from your CKAN base folder (e.g. `pyenv/`):

    pip install -e git+https://github.com/okfn/ckanext-example#egg=ckanext-example

Then activate it by setting `ckan.plugins = example` in your main `ini`-file.

Orientation
===========

-   Examine the source code, starting with `ckanext/example/plugin.py`
-   To understand the nuts and bolts of this file, which is a CKAN *Extension*, read in conjunction with the "Extension documentation": <http://docs.ckan.org/en/latest/extensions.html>
-   One thing the extension does is set the values of `extra_public_paths` and `extra_template_paths` in the CKAN config, which are "documented here": <http://docs.ckan.org/en/latest/configuration.html#extra-template-paths>
-   These are set to point at directories within `ckanext/example/theme/` (in this package). Here we: \* override the home page HTML `ckanext/example/theme/templates/home/index.html` \* provide some extra style by serving `extra.css` (which is loaded using the `ckan.template_head_end` option \* customise the navigation and header of the main template in the file `layout.html`.

    The latter file is a great place to make global theme alterations. It uses the \_layout template\_ pattern "described in the Genshi documentation":<http://genshi.edgewall.org/wiki/GenshiTutorial#AddingaLayoutTemplate>. This allows you to use Xpath selectors to override snippets of HTML globally.

-   The custom package edit form at `package_form.py` follows a deprecated way to make a form (using FormAlchemy). This part of the Example Theme needs updating. In the meantime, follow the instructions at: <http://docs.ckan.org/en/latest/forms.html>

Example Tags With Vocabularies
==============================

To add example tag vocabulary data to the database, from the ckanext-example directory run:

    paster example create-example-vocabs -c <path to your ckan config file>

This data can be removed with

    paster example clean -c <path to your ckan config file>

