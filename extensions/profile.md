---
layout: extension
name: profile
title: Add profiling to CKAN using repoze
author: Sean Hammond
homepage: https://github.com/seanh/ckanext-profile
github_user: seanh
github_repo: ckanext-profile
category: Extension
featured: 
permalink: /extension/profile/
---


ckanext-profile
===============


Add profiling to CKAN using [repoze.profile](https://pypi.python.org/pypi/repoze.profile).

This adds a page `/__profile__` to your CKAN site,  where you can view detailed
profiling data. The same profiling data is also saved to two files in your CKAN
directory:

1. `profiling.log`, which can be analyzed with the
   [Python standard library's profilers](http://docs.python.org/2/library/profile.html)
   (specifically, the [Stats class](http://docs.python.org/2/library/profile.html#the-stats-class)
   can be used to analyze the data)

2. `cachegrind.out`, which can be analyzed using the
   [KCachegrind](http://kcachegrind.sourceforge.net/html/Home.html) app

See <http://docs.repoze.org/profile/> for more documentation.


Installation
------------

Activate your CKAN virtualenv, then run:

    pip install -e 'git+https://github.com/seanh/ckanext-profile.git#egg=ckanext-profile'

