---
layout: extension
name: ckanext-oauth2
title: OAuth2 support for CKAN
author: Etalab
homepage: https://github.com/etalab/ckanext-oauth2
github_user: etalab
github_repo: ckanext-oauth2
category: Extension
featured: 
permalink: /extension/ckanext-oauth2/
---


OAuth2 CKAN extension
=====================

The OAuth2 extension allows site visitors to login through an OAuth2 server.

NOTE: This extension requires ckan version 1.7 or higher.

Activating and Installing
-------------------------

To install the plugin, enter your virtualenv and load the source:

``` sourceCode
$ pip install ckanext-oauth2
# or
$ pip install git+https://github.com/etalab/ckanext-oauth2.git
```

Add the following to your CKAN .ini file:

``` sourceCode
ckan.plugins = oauth2 <other-plugins>
```

Update your who.ini to make use of OAuth2:

``` sourceCode
[plugin:oauth2]
use = ckanext.oauth2.repozewho:make_plugin
authorization_endpoint = https://auth.domain.com/oauth2/authorize/
token_endpoint = https://auth.domain.com/oauth2/token/
client_id = client-id
client_secret = client-secret
scope = profile another.scope
rememberer_name = fake
profile_api_url = https://auth.domain.com/api/me
profile_api_user_field = username


[plugin:fake]
use = ckanext.oauth2.tests.utils:FakeRememberer

[identifiers]
plugins = oauth2 fake

[authenticators]
plugins = oauth2

[challengers]
plugins = oauth2

[general]
challenge_decider = repoze.who.classifiers:default_challenge_decider
request_classifier = repoze.who.classifiers:default_request_classifier
```

