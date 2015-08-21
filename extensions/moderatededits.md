---
layout: extension
name: moderatededits
title: Moderated Edits extension for CKAN 1
author: Open Knowledge
homepage: https://github.com/okfn/ckanext-moderatededits
github_user: okfn
github_repo: ckanext-moderatededits
category: Extension
featured: 
permalink: /extension/moderatededits/
---


CKAN Moderated Edits Extension
==============================

The moderated edits extension for CKAN adds the ability for all updates
to CKAN packages to be moderated.

**Current Status:** Incomplete

Installation and Activation
---------------------------

To install the plugin, enter your virtualenv and install the source:

    $ pip install hg+http://bitbucket.org/okfn/ckanext-moderatededits

This will also register a plugin entry point, so you now should be 
able to add the following to your CKAN .ini file:

    ckan.plugins = moderatededits
 
After you clear your cache and reload the site, the Moderated Edits plugin
and should be available. 

**Note:** Currently requires CKAN branch feature-1141-moderated-edits-ajax

Todo / Roadmap
--------------

* Limit no. revisions shown in the revisions box, maybe show as separate pages with prev/next buttons.
* Do some JS validation on 'edit summary' field (the revision commit message)
* Add code to handle package extras 

Tests
-----
From the ckanext-moderatededits directory, run:

    $ nosetests --ckan

