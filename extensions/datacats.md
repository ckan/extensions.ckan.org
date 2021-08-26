---
layout: extension
name: datacats
title: Docker script for managing and deploying ckan environments
author: DataCats
homepage: https://github.com/datacats/datacats
github_user: datacats
github_repo: datacats
category: Extension
featured: 1
permalink: /extension/datacats/
---


datacats
========

[![Circle
CI](https://circleci.com/gh/datacats/datacats.svg?style=svg)](https://circleci.com/gh/datacats/datacats)
[![docs](https://readthedocs.org/projects/docs/badge/?version=latest)](http://docs.datacats.com/)

datacats uses Docker to give you fully self-contained
[CKAN](http://ckan.org) dev environments on any platform, and easy
deployment to any host.

Install
-------

Please see detailed OS-specific [installation instructions in the
docs](http://docs.datacats.com/guide.html#installation).

Create a CKAN environment
-------------------------

    datacats create mytown

This will create a new environment called "mytown" in the current
directory, new data files in "\~/.datacats/mytown" and start serving
your new site locally.

    Creating environment "mytown"............
    Installing ckan requirements
    Installing ckan
    Installing ckanext-mytowntheme
    Initializing database
    Starting web server at http://localhost:5306/ ...
    admin user password:

Open your brower to the address shown to try out your new site. Enter an
admin password at the prompt to create your first sysadmin user.

Customize your theme
--------------------

In your environment directory you will find "ckan" and
"ckanext-mytowntheme" subdirectories. "ckanext-mytowntheme" is a simple
example extension that extends some templates and adds some static
files.

Customize your Jinja2 templates in
"ckanext-mytowntheme/ckanext/mytowntheme/templates", using the files in
"ckan/ckan/templates" as a reference.

Full CKAN extension possibilities are covered in the official CKAN
documentation.

The site is run with "paster serve --reload" by default so changes to
templates and source files will be visible almost immediately after
saving them. Refresh your browser window to see the changes.

For changes to configuration files and new template files added use
"reload" to force a site reload.

    datacats reload mytown

You may omit "mytown" when running datacats commands from within the
environment directory or any subdirectory.

Add CKAN extensions
-------------------

Many of the [100+ existing CKAN extensions](http://extensions.ckan.org/)
are already compatible with datacats.

First download or clone an extension in to your environment directory.

    cd myproject
    git clone git@github.com:ckan/ckanext-pages.git

Then add the plugins and configuration options as required by the
extension to the "development.ini" file. For ckanext-pages we add
"pages" to the list of plugins.

    ckan.plugins = mytowntheme datastore image_view pages

Reinstall all extensions and reload the site with:

    datacats install

Refresh your browser window to use the new features.

Deploy your environment
-----------------------

To deploy your customized CKAN site copy your source directory to your
target host with rsync then run:

    datacats init --image-only
    datacats start --production --address=<IP-address>

