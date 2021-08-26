---
layout: extension
name: ytp-request
title: Organization member request handling
author: yhteentoimivuuspalvelut
homepage: https://github.com/yhteentoimivuuspalvelut/ckanext-ytp-request
github_user: yhteentoimivuuspalvelut
github_repo: ckanext-ytp-request
category: Extension
featured: 
permalink: /extension/ytp-request/
---


ckanext-ytp-request
===================

CKAN extension providing means to control organization member requests,
requests history and related operations.

Features
--------

-   Users can request to be part of organization
-   Organization admins and global admins can approve or reject request
-   Request history log

Compatibility
-------------

Tested with CKAN 2.2 - 2.3

Installation
------------

Install to you ckan virtual environment

    pip install -e  git+https://github.com/yhteentoimivuuspalvelut/ckanext-ytp-request#egg=ckanext-ytp-request

Add to ckan.ini

    ckan.plugins = ... ytp_request

