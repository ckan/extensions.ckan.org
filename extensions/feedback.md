---
layout: extension
name: feedback
title: Simple feedback form for submitting data requests
author: Maulik Kamdar
homepage: https://github.com/maulikkamdar/ckanext-feedback
github_user: maulikkamdar
github_repo: ckanext-feedback
category: Extension
featured: 
permalink: /extension/feedback/
---


**CKAN-feedback**

This extension provides a simple feedback form for submitting data
requests through the CKAN System. The administrator receives an email
for processing the request. The administrator email can be set in the
CKAN config file development.ini/production.ini. The config variable is
'ckan.feedback.request\_email'. The system email which would send this
request information could be defined in the same config file using the
config variable 'ckan.feedback.sender\_email'. If these values are not
defined, the extension uses the default values defined in controller.py.

The CKAN-feedback extension can be installed by running

python setup.py develop

in the extension directory.

======================================================== The
CKAN-feedback extension was developed for use as a Data-request module
in the Data.Gov.IE Open Data Platform, but can be extended and used as a
simple, generic feedback module for any CKAN deployment.

