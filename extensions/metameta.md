---
layout: extension
name: metameta
title: generic metameta
author: XVTSolutions
homepage: https://github.com/XVTSolutions/ckanext-metameta
github_user: XVTSolutions
github_repo: ckanext-metameta
category: Extension
featured: 
permalink: /extension/metameta/
---


ckanext-metameta
================

Allows Organisation defaults to be set by users who are Organisation
administrators

Installation
------------

\#\#\#Download cd /usr/lib/ckan/default/src/ git clone
<a href="https://github.com/XVTSolutions/ckanext-metameta.git" class="uri">https://github.com/XVTSolutions/ckanext-metameta.git</a>

\#\#\#Make sure your python virtualenv is activated .
/usr/lib/ckan/default/bin/activate

\#\#\#Install ckanext-metameta into python cd
/usr/lib/ckan/default/src/ckanext-metameta python setup.py develop

\#\#\#Add to plugin in .ini file sudo emacs
/etc/ckan/default/development.ini &lt;--or production.ini for apache

plugins = <other plugins> metameta

How it works
------------

-   When the plugin is first initiated, a table called *metameta* is
    created.
-   This plugin adds a 'metadata' tab to the Organisation's 'edit' page.
    The first time this page is accessed for the given organisation,
    records are created in the metameta table for each field in
    metameta/metadata\_fields.py. The value column for each field is
    NULLed.
-   When the user goes to the 'metadata' tab,they are shown a table of
    the current field/values.
-   The user can click the 'Edit Defaults' button to be able to edit
    each field and then click 'Update' which will bring them back to the
    table of fields / values.
-   No user except for users with Admin permission for the organisation
    will be able to see these pages. Any attempt to reach these pages by
    any other means - e.g. editing the URL - will simply result in the
    user being redirected to the main Organisation view page.
-   Only the organisation admins will be able to see the 'metadata' tab.
-   Database can be cleaned of all metameta tables using the following
    command:

    `paster --plugin=ckanext-metameta clean -c /etc/ckan/default/development.ini`

\#\#\#\#configuration for optional function ckan.oneline\_textarea =
False \#if True, then all custom text area data are saved, after
removing carriage return. Default value is false.

ckan.maintainer\_notification = False \#if True, then assigned
maintainer is notified. Default value is false

