---
layout: extension
name: odmetheme
title: Custom CKAN theme for Offene Daten Mettmann http-//demo
author: formwandler
homepage: https://github.com/formwandler/ckanext-odmetheme
github_user: formwandler
github_repo: ckanext-odmetheme
category: Extension
featured: 
permalink: /extension/odmetheme/
---


ckanext-odmetheme
==================

Custom CKAN theme for [Offene Daten Mettmann](http://www.offene-daten-mettmann.de) containing templates, static pages, media files and translations. General setup inspired by [ckanext-demo](https://github.com/okfn/ckanext-demo). Internationalization files inspired and forked from [ckanext-ogdch](https://github.com/ogdch/ckanext-ogdch).

Notice: The templates are quite rudimentary and under construction.

## Installation

Use `pip` to install this plugin. This example installs it as user `ckan` into the default src directory of your virtual Python environment, for example `/usr/lib/ckan/demo/src/`.

```bash
su -s /bin/bash - ckan
source /usr/lib/ckan/demo/bin/activate
pip install -e git+https://github.com/formwandler/ckanext-odmetheme.git#egg=ckanext-odmetheme
```

This will register the plugin entry point by running `python setup.py develop`. Make sure to add `odmetheme` to `ckan.plugins` in your config ".ini" file.

For activating the internationalization files you need to replace the original CKAN `.mo` files under `src/ckan/ckan/i18n/` (if CKAN has been installed using "python setup.py develop") or under `lib/python2.?/site-packages/ckan/i18n/` (if CKAN has been installed using "python setup.py install"). See script in `bin` directory which does the job. Or configure CKAN to use the customized i18n dir by setting the config parameter `ckan.i18n_directory`.

## Copying and License

This material has been inspired and partly mixed from the extensions [ckanext-demo](https://github.com/okfn/ckanext-demo) and [ckanext-ogdch](https://github.com/ogdch/ckanext-ogdch).

Adaptations are Copyright (C) 2013  Ralf Kruedewagen <gpl@kruedewagen.de>.

It is open source and licensed under the GNU AFFERO GENERAL PUBLIC LICENSE v3 whose full text may be found at http://www.gnu.org/licenses/agpl-3.0. See also LICENSE file.

