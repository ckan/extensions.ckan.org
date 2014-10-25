---
layout: extension
name: urn
title: URN fetching extension for CKAN
author: Kata team repository
homepage: https://github.com/kata-csc/ckanext-urn
github_user: kata-csc
github_repo: ckanext-urn
category: Extension
featured: 
permalink: /extension/urn/
---


URN Plugin for CKAN
===================

This plugin automatically generates an ID from an URN source for a Resource data
type. The default CKAN UUID ID for a Resource is hence replaced.

Installation
------------

First of all, as with all CKAN extensions, one must install it to a either pyenv
or a global python path, like this:

 python setup.py install

and add the extension name 'urn' to the configuration option 'ckan.plugins'
of the CKAN ini file in use.

In addition to this, one must add a configuration option 'urn_url' to the
app:main section of the ini file like this:

 urn_url = http://urnsource-kk.lib.helsinki.fi/cgi-bin/urn_generator.cgi?type=nbn

If the URL supplied cannot be successfully contacted, then the ID is not
replaced with the URN.

The URL supplied in this documentation refers to the NBN URN generator offered 
by the National Library of Finland.

Tests
-----

The included tests can be run using nose, but the test-core.ini has a path to
CKAN which needs to be modified. Example of the path is the default one:

 use = config:../../../pyenv/src/ckan/test-core.ini

Then to run the tests:

 python setup.py nosetests
 

