---
layout: extension
name: youckan
title: YouCKAN connector for CKAN
author: Etalab
homepage: https://github.com/etalab/ckanext-youckan
github_user: etalab
github_repo: ckanext-youckan
category: Extension
featured: 
permalink: /extension/youckan/
---


YouCKAN CKAN extension
======================

The YouCKAN extension is a YouCKAN connector for CKAN.

NOTE: This extension has only been texted with CKAN 2.1.

Activating and Installing
-------------------------

To install the plugin, enter your virtualenv and load the source:

``` sourceCode
$ pip install ckanext-youckan
```

Add the following to your CKAN .ini file:

``` sourceCode
ckan.plugins = youckan <other-plugins>
```

To use YouCKAN users and authentification, set you who.ini like this:

``` sourceCode
[plugin:youckan]
use = ckanext.youckan.repozewho:plugin
session_cookie_name = youckan_session
auth_cookie_name = youckan_auth
login_url = http://sso.etalab.dev/login/
secret = YOUR_DJANGO_SECRET_KEY
https = true

[general]
request_classifier = repoze.who.classifiers:default_request_classifier
challenge_decider = youckan

[identifiers]
plugins = youckan

[authenticators]
plugins = youckan

[challengers]
plugins = youckan
```

and configure the YouCKAN plugin to use authentication:

``` sourceCode
ckan.plugins = youckan <other-plugins>
youckan.use_auth = true
youckan.logout_url = https://youckan/logout
```

