---
layout: extension
name: openrefine-ckan
title: OpenRefine CKAN Connector
author: OpenGov
homepage: https://github.com/opengov-opendata/openrefine-ckan-storage-extension
github_user: opengov-opendata
github_repo: openrefine-ckan-storage-extension
category: Extension
featured: 
permalink: /extension/openrefine-ckan/
---


OpenRefine CKAN Storage Extension (for CKAN v2.2+)
==================================================

!! Currently tested and works with OpenRefine 2.6-beta1 and CKAN v2.2+

Upload data directly from Google Refine to CKAN using CKAN API.

This project is a modifed and updated version of [Fadmaa](https://github.com/fadmaa/grefine-ckan-storage-extension)'s work. The earlier version did not support CKAN API v3. The source code is updated to comply with CKAN 2.2 and API v3.

You can find more about the earlier version here:

<http://lab.linkeddata.deri.ie/2011/grefine-ckan/>

and

<https://github.com/fadmaa/grefine-ckan-storage-extension>

Installation
------------

-   Make sure you have Google Refine installed on your machine (see [here](https://github.com/OpenRefine/OpenRefine/releases/tag/2.6-beta.1))
-   Pull grefine-ckan-storage-extension source into OpenRefine's extensions folder (create one if it doesn't exists):

        * ex. MAC OS:
        cd ~/Library/Application\ Support/OpenRefine/extensions/
        git clone https://github.com/Ontodia/grefine-ckan-storage-extension.git

-   Restart OpenRefine

Developers
----------

-   If you made changes to the source you need to recompile OpenRefine.
-   Add following lines to OpenRefine/extensions/build.xml:

        <target name="build">
                ...
                <ant dir="grefine-ckan-storage-extension/" target="build" />
        </target>

        <target name="clean">
              ...
              <ant dir="grefine-ckan-storage-extension/" target="clean" />
        </target>

-   Recompile OpenRefine source code as::

        cd {{path_to_refine}}/OpenRefine/
        ./refine clean
        ./refine build

-   Restart OpenRefine

TODO
----

-   Currently the upload uses CKAN API [create\_resource](http://docs.ckan.org/en/latest/api/#ckan.logic.action.create.resource_create) action. By defualt this will timeout for large files after 30 secs. In order to fix this; use [datastore api](http://docs.ckan.org/en/ckan-2.2/datastore.html), split data into chunks and upload chunks via datastore api
-   Better documentation
-   Code clean-up
-   We should test and fix problems with other OpenRefine and CKAN versions.
-   Feel free to contribute


