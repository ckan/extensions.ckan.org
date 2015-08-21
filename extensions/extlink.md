---
layout: extension
name: extlink
title: External URL pop-up message and tooltips
author: data.gov - GSA
homepage: https://github.com/GSA/ckanext-extlink
github_user: GSA
github_repo: ckanext-extlink
category: Extension
featured: 
permalink: /extension/extlink/
---


CKAN External Link Extension
===============================

**CKAN Version:** >= 2.0

This extension will add pop-up message as tooltip for external URLs. Administrator will be able to add websites to whitelist from UI. 

Installation
------------

Install the extension as usual, and edit ckan configuration ini file to add or append the plugin:

      ckan.plugins = extlink


White list
--------------

By default all links except for those from the site's own domain will be treated as external links, and will have a pop-up message as tooltip when mouse hovered. Site administrators can go to http://yourdomain.site/extlink to add domains to white list, so that those domain links will not be treated as external links. For example:

    .mil, data.gov
    reisys.com
    reisystems.com

At the same page administrators can also customize the pop-up message.

