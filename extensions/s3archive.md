---
layout: extension
name: ckanext-s3archive
title: Archive CKAN datastore to S3
author: CKAN
homepage: https://github.com/ckan/ckanext-s3archive
github_user: ckan
github_repo: ckanext-s3archive
category: Extension
featured: 
permalink: /extension/ckanext-s3archive/
---


Description
===========

This extension archives all resource files stored in the local CKAN filestore into S3. The files are removed locally and just hosted on s3. When a user requests these files they are redirected to a temporary S3 url for download. Only authorized users are allowed to get these urls and the urls expire after 30 mins for security.

Installation
============

To install this package, from your CKAN virtualenv, run the following from your CKAN base folder (e.g. `pyenv/`):

    pip install -e git+https://github.com/okfn/ckanext-s3archive#egg=ckanext-s3archive

Then activate it by setting `ckan.plugins = s3archive` in your main `ini`-file.

Compatability
=============

CKAN 2.2+

Configuration
=============

Config options should be placed in main section of the CKAN config file:

    ckanext.s3archive.access_key = <access_key>
    ckanext.s3archive.secret_key = <secret_key>
    ckanext.s3archive.bucket = <bucket>

    ckan.plugins = <current_plugins> s3archive

Usage
=====

The following paster command will archive all the files to S3

paster --plugin=ckanext-s3archive s3archive archive -c \<path to config file\>

This command can be put in a cron job and is safe to be run regularly but is recommended that it is run about once a day. This is to give plenty time for the last job to finish before rerunning. If doing a large migration then it is probably best to run the command outside the cron for the first run.

