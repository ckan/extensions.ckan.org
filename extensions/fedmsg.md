---
layout: extension
name: fedmsg
title: CKAN extension for sending activity events to the Fedora Infrastructure Message Bus (fedmsg)
author: Etalab
homepage: https://github.com/etalab/ckanext-fedmsg
github_user: etalab
github_repo: ckanext-fedmsg
category: Extension
featured: 
permalink: /extension/fedmsg/
---


CKANExt-fedmsg
==============

This extension sends real-time messages to [fedmsg](http://www.fedmsg.com/) bus each time public changes are made to [CKAN](http://ckan.org/) database.

To use it, edit CKAN configuration file (aka ".ini") and add "fedmsg" to "ckan.plugins" line.

