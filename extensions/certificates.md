---
layout: extension
name: certificates
title: Retrieval and helpers for ODI Open Data certificates
author: Data.Gov.UK - Cabinet Office
homepage: https://github.com/datagovuk/ckanext-certificates
github_user: datagovuk
github_repo: ckanext-certificates
category: Extension
featured: 
permalink: /extension/certificates/
---


ODI Open Data Certificates extension
====================================

This extension provides a mechanism for retrieving information about
[Open Data Certificates](https://certificates.theodi.org/) so that the
information can be included on the dataset page.

There are no templates supplied with this extension, but you can use the
template helpers to integrate the information into your own templates.

Installation
------------

1.  Active your virtualenv
2.  Go to where you install your extensions
3.  `git clone https://github.com/datagovuk/ckanext-certificates.git`
4.  `cd ckanext-certificates`
5.  `python setup.py develop`

Configuration
-------------

You should add `certificates` to your list of plugins configured by
`ckan.plugins`.

It is wise to add a parameter to the ODI Certificates feed URL, to
request only your site's dataset certificates. e.g.:

    ckanext.certificates.feed_url = https://certificates.theodi.org/datasets.feed?domain=data.gov.uk

All certificates will be checked to see if they are for your site
anyway, by seeing if the 'about' URL starts with your configured
`ckan.site_url`. e.g.

    ckan.site_url = http://data.gov.uk

Note it is automatically flexible enough to allow both http and https
versions, and with www. inserted or not.

However in some circumstances the ckan.site\_url may be different to the
certificates interested in, perhaps on a test machine. In this case you
can configure a string that the about URL must start with in
`ckanext.certificates.site_url` e.g.

    ckan.site_url = http://localhost:5000
    ckanext.certificates.site_url = http://data.gov.uk

Or maybe a regular expression is needed, to cope with variations e.g.

    ckanext.certificates.site_url_regex = https?://(catalog\.)?data\.gov

Retrieving information
----------------------

You should set up a recurring task to fetch the certificates at a rate
that is sensible. To run the task as a one-off:

    paster --plugin=ckanext-certificates fetch_certs -c <PATH_TO_CONFIG_FILE>

Tests
-----

A few tests are available:

    nosetests ckanext/certificates/tests/

