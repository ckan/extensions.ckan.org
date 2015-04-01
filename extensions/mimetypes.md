---
layout: extension
name: ckanext-mimetypes
title: Custom mimetypes extension
author: fumi
homepage: https://github.com/fumi/ckanext-mimetypes
github_user: fumi
github_repo: ckanext-mimetypes
category: Extension
featured: 
permalink: /extension/ckanext-mimetypes/
---


ckanext-mimetypes
=================

Custom mimetypes extension

Read the Custom Internet media types (MIME types) section 
at http://ckan.readthedocs.org/en/latest/maintaining/filestore.html

Install
-------
Activate the pyenv for your CKAN instance before installing this extension.
Clone this repository and run ```python setup.py install``` to install simply. 
Or you can install this by the following way.

```
$ pip install -e git+https://github.com/fumi/ckanext-mimetypes.git#egg=ckanext-mimetypes
$ cd (pyenv)/src/ckanext-mimetypes
$ python setup.py develop
```
    
Then add ```mimetypes``` to your ckan.plugins in your CKAN config file.

