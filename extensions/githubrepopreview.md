---
layout: extension
name: githubrepopreview
title: Github repository resource viewer
author: Link Digital
homepage: https://github.com/DataShades/ckanext-githubrepopreview
github_user: DataShades
github_repo: ckanext-githubrepopreview
category: Extension
featured: 
permalink: /extension/githubrepopreview/
---


ckanext-githubrepopreview
=========================

A CKAN plugin for previewing GitHub repository resources.

Installation
============

1.  Activate you CKAN python environment and install this extension's
    software::

    $ pyenv/bin/activate

    $ pip install -e
    git+<a href="https://github.com/DataShades/ckanext-githubrepopreview.git#egg=ckanext-githubrepopreview" class="uri">https://github.com/DataShades/ckanext-githubrepopreview.git#egg=ckanext-githubrepopreview</a>

2.  Enable the extension in your CKAN config file by adding it to
    `ckan.plugins`::

    ckan.plugins = githubrepo\_view

Usage
=====

When creating/editing a resource via the UI, check the 'GitHub
Repository' checkbox to make this view available. Alternatively, one can
update the 'github\_repository' extras field of the resource to 'True'
via the CKAN API to make the view available.

