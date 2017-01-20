---
layout: extension
name: wet-boew
title: CKAN extension that adds the Web Experience Toolkit to CKAN 2
author: Open Data Initiative - Initiative sur les données ouvertes
homepage: https://github.com/open-data/ckanext-wet-boew
github_user: open-data
github_repo: ckanext-wet-boew
category: Extension
featured: 
permalink: /extension/wet-boew/
---


ckanext-wet-boew
================

This CKAN extension adds the Web Experience Toolkit 4.0.x Base theme to CKAN 2.2. This theme is available from the [WET-BOEW
website](http://wet-boew.github.io/wet-boew/docs/versions/dwnld-en.html).

Please note that this extension does not use the Fanstatic Resource Manager in CKAN. Instead, the WET resources are served
directly from the web server.

Configuration Settings
----------------------

WET Resources
-------------

### Externally Hosted

1.  Set `wet_boew.url` to the root URL where the WET resources are hosted

*Example*

`wet_boew.url = http://domain.com/wet-boew/v4.0.23`

### Internally Hosted

1.  Extract the WET 4.0.x core CDN and desired themes cdn package to a folder

`export WET_VERSION=v4.0.23   mkdir wet-boew && curl -L https://github.com/wet-boew/wet-boew-cdn/archive/$WET_VERSION.tar.gz | tar -zx --strip-components 1 --directory=wet-boew   mkdir GCWeb && curl -L https://github.com/wet-boew/themes-cdn/archive/$WET_VERSION-gcweb.tar.gz | tar -zx --strip-components 1 --directory=GCWeb   mkdir theme-base && curl -L https://github.com/wet-boew/themes-cdn/archive/$WET_VERSION-theme-base.tar.gz | tar -zx --strip-components 1 --directory=theme-base   mkdir theme-gc-intranet && curl -L https://github.com/wet-boew/themes-cdn/archive/$WET_VERSION-theme-gc-intranet.tar.gz | tar -zx --strip-components 1 --directory=theme-gc-intranet   mkdir theme-gcwu-fegc && curl -L https://github.com/wet-boew/themes-cdn/archive/$WET_VERSION-theme-gcwu-fegc.tar.gz | tar -zx --strip-components 1 --directory=theme-gcwu-fegc   mkdir theme-ogpl && curl -L https://github.com/wet-boew/themes-cdn/archive/$WET_VERSION-theme-ogpl.tar.gz | tar -zx --strip-components 1 --directory=theme-ogpl   mkdir theme-wet-boew && curl -L https://github.com/wet-boew/themes-cdn/archive/$WET_VERSION-theme-wet-boew.tar.gz | tar -zx --strip-components 1 --directory=theme-wet-boew`

1.  Set the `extra_public_paths` settings to that path where the files are extracted

*Example*

`extra_public_paths = /home/user/wet-boew/v4.0.23`

Selecting a theme
-----------------

1.  Add the desired theme to the `ckan.plugins` configuration (`wet_boew`, `wet_boew_theme_gcweb`, `wet_boew_theme_base`, `wet_boew_theme_gc_intranet`, `wet_boew_theme_ogpl`)

Additional Configuration
------------------------

1.  **wet\_theme.geo\_map\_type**: set this value to indicate what style of
    [WET Geomap widget](http://wet-boew.github.io/wet-boew/docs/ref/geomap/geomap-en.html) to use. Set this to either
    'static' or 'dynamic'.

*Example*
`wet_theme.geo_map_type = static`

