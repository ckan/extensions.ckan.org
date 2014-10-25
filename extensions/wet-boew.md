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


================
ckanext-wet-boew
================

This CKAN extension adds the Web Experience Toolkit base theme to CKAN 2.0. You will need WET release 3.1.0, which you can find here: http://wet-boew.github.io/wet-boew/docs/versions/dwnld-en.html . Copy
the contents of the 'dist' folder into 'ckanext-wet-boew/ckanext/wet_boew/public/dist'::

  cd ckanext/wet_boew/public/dist/

  wget https://github.com/wet-boew/wet-boew-dist/archive/v3.1.7.zip
  unzip v3.1.7.zip wet-boew-dist-3.1.7/dist/*
  mv wet-boew-dist-3.1.7/dist/* .
  rm -r v3.1.7.zip wet-boew-dist-3.1.7/

The WET toolkit distribution includes only minimized versions of the required Javascript files. 
However CKAN uses the Fanstatic resource manager which requires un-minimized Javascript files, so
it is necessary to supply these separately. Copy an unminimized version of the JQuery Mobile 
javascript file (obtained at 'http://jquerymobile.com/blog/2013/02/20/jquery-mobile-1-3-0-released/')
into 'ckanext-wet-boew/ckanext/wet_boew/public/dist/js/jquerymobile/jquery.mobile.js'::

  mkdir -p js/jquerymobile/
  wget http://code.jquery.com/mobile/1.3.0/jquery.mobile-1.3.0.js \
    -O js/jquerymobile/jquery.mobile-1.3.0.js

This extension also requires the python json and shapely libraries that are used by the
CKAN spatial extension.

By default, CKAN pages will still display using the default CKAN template. To use the base theme,
override the template for the page and have it extend template page_wet.html instead of the usual
page.html.

To use a WET page with a left hand menu, instead extend template page_sec_menu_wet.html.




