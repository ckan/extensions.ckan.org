---
layout: extension
name: ckanext-apihelper
title: API Helper extension.
author: CKAN
homepage: https://github.com/ckan/ckanext-apihelper
github_user: ckan
github_repo: ckanext-apihelper
category: Extension
featured: 
permalink: /extension/ckanext-apihelper/
---


# ckanext-apihelper

This extension is meant to add a few pages that will serve as a friendly interface
for the action API. 

**Requires CKAN Version 2.1.1 or higher.**


<p align="center">
  <img src="http://imagizer.imageshack.us/v2/500x500q100/540/HTd2Y4.png" alt="APIHelper Screenshot"/>
</p>

## Instalation Instructions

With your CKAN virtual environment activated:

    pip install -e  git+https://github.com/ckan/ckanext-apihelper.git#egg=ckanext-apihelper

And add the following to your ckan.ini:

    ckan.plugins = ... apihelper



