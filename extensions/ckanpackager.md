---
layout: extension
name: ckanpackager
title: A stand-alone service to pack a given CKAN resource in a ZIP file and email the link to a user
author: U.K. Natural History Museum
homepage: https://github.com/NaturalHistoryMuseum/ckanext-ckanpackager
github_user: NaturalHistoryMuseum
github_repo: ckanext-ckanpackager
category: Extension
featured: 
permalink: /extension/ckanpackager/
---


ckanext-ckanpackager
====================

Overview
--------

CKAN extension to provide a user interface to download resources using [ckanpackager](http://github.com/NaturalHistoryMuseum/ckanpackager)

Ckanpackager is a stand-alone service that can be instructed to fetch data on a [CKAN](http://ckan.org) site using the datastore API, pack the data in a ZIP file and email the link to a given address. See the [ckanpackager github page](http://github.com/NaturalHistoryMuseum/ckanpackager) for more information.

Note that to embed the user interface you must provide your own template (typically overriding CKAN's). See the CKAN documentation.

The extension provides an HTML snippet that can be used to replace the Download button on resources. The new button will:
- Provide an overlay explaining the link will be sent later on;
- If anonymous downloading is enabled, provide a form for users to enter the destination email address;
- On resource pages, the button will ensure that currently applied filters and searches are forwarded on to the ckanpackager service.


Usage
-----

Enable the plugin by adding it to `ckan.plugins` in your configuration file.

To embed the button on a page, add the following to a Jinja2 template:

        {%raw%}{% {%endraw%}snippet 'ckanpackager/snippets/package_resource.html',
           res=res, pkg=pkg, bt_class="icon-download", bt_text=_('Download')
       {%raw%} %}{%endraw%}

Where `res` is a resource object and `pkg` a package object. You can use the above snippet as it to replace the download button in `package/resource_read.html`

Compatibility
-------------

The current version is being developed to work against CKAN's 1251 branch (resource views).

Configuration
-------------

- `ckanpackager.url`: The URL of the ckan packager service, eg. `http://ckanpackager.example.com:8765/package`
- `ckanpackager.secret`: The shared secret

TODO: Add a configuration item to enable/disable anonymous downloading.
