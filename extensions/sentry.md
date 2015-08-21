---
layout: extension
name: sentry
title: Hooks the Sentry's raven plugin into ckan/pylons wsgi middleware chain
author: Open Data in Trentino
homepage: https://github.com/opendatatrentino/ckanext-sentry
github_user: opendatatrentino
github_repo: ckanext-sentry
category: Extension
featured: 
permalink: /extension/sentry/
---


# CkanExt-Sentry

Hooks the Sentry's raven plugin into ckan/pylons wsgi middleware chain.


## Important notice

There are some known issues with this middleware insertion method.
Have a look at the ``README.md`` in the ``alternatives`` folder (that is,
[this directory](https://github.com/opendatatrentino/ckanext-sentry/tree/master/alternatives)
for more information on a better solution for integrating Sentry).


## Usage

Refer to: http://raven.readthedocs.org/en/latest/config/pylons.html

- Install plugin, add ``sentry`` to enabled plugins list
- Add sentry configuration to main configuration file
- Add logging configuration (todo: fix the "11 args" issue)
- **todo:** there seems to be some issues with pylons 0.9.7
  (or is it due to some customization?)


## Configuration options

- ``sentry.dsn``
  The DSN for connecting to sentry

- ``sentry.load_method``
  Specify how to hook sentry client into middleware chain.
  Allowed values:

  - ``none`` do not hook sentry client
  - ``pylons`` (default) use the pylon's way
  - ``wsgi`` use the generic way for wsgi apps

- ``sentry.configure_logging``
  If set to "true" (default), will add logging configuration
  while adding middleware to application.

