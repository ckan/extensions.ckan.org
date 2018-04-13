---
layout: extension
name: discourse-sso
title: Discourse SSO
author: JD Bothma
homepage: https://github.com/OpenUpSA/ckanext-discourse-sso
github_user: OpenUpSA
github_repo: ckanext-discourse-sso
category: Extension
featured: 
permalink: /extension/discourse-sso/
---


ckanext-discourse-sso
=====================

Adds support for [Discourse SSO](https://meta.discourse.org/t/official-single-sign-on-for-discourse-sso/13045). This means that Aleph becomes the authentication authority for a Discourse instance.

When users try to login on Discourse, they get redirected to CKAN. If they are logged in on CKAN or login when prompted, they get redirected back to Discourse.

Discourse will verify the user's email address (which it gets from CKAN) so that your discourse instance doesn't become a way to spam your CKAN users.

Requirements
------------

Tested with CKAN 2.7.2 and Discourse v2.0.0.beta4 +97

Installation
------------

To install ckanext-discourse-sso:

1.  Activate your CKAN virtual environment, for example:

        . /usr/lib/ckan/default/bin/activate

2.  Install the ckanext-discourse-sso Python package into your virtual environment:

        pip install git+https://github.com/OpenUpSA/ckanext-discourse-sso.git@v0.0.1

3.  Restart CKAN. For example if you've deployed CKAN with Apache on Ubuntu:

        sudo service apache2 reload

Configuration
-------------

### Discourse

1.  Make up some random secret string and enter it in the `sso_secret` settings field
2.  Enter your CKAN URL with the `/discourse/sso` suffix in the `sso_url` field, e.g. `https://data.example.com/discourse/sso`

### CKAN

1.  Add `discourse-sso` to the `ckan.plugins` setting in your CKAN config file (by default the config file is located at `/etc/ckan/default/production.ini`).
2.  Set the config variable `discourse.sso.secret` to be the same value as `sso_secret` in your Discourse settings. You can do this via the `CKAN_DISCOURSE_SSO_SECRET` environment variable.
3.  Set the config variable `discourse.url` to be your Discourse intance, e.g. `https://discourse.exampe.com/`. You can do this via the `CKAN_DISCOURSE_URL` environment variable.

Development Installation
------------------------

To install ckanext-discourse-sso for development, activate your CKAN virtualenv and do:

    git clone https://github.com/OpenUpSA/ckanext-discourse-sso.git
    cd ckanext-discourse-sso
    python setup.py develop

