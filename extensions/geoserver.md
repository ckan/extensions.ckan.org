---
layout: extension
name: geoserver
title: Geoserver Extension for CKAN
author: ngds
homepage: https://github.com/ngds/ckanext-geoserver
github_user: ngds
github_repo: ckanext-geoserver
category: Extension
featured: 
permalink: /extension/geoserver/
---


\#\#\#Geoserver Extension for CKAN

custom configurations:

-   geoserver.rest\_url =
    'geoserver://admin:<a href="mailto:geoserver@localhost" class="email">geoserver@localhost</a>:8080/geoserver/rest'
-   geoserver.default\_workspace = 'ckan'
-   geoserver.workspace\_name = ckan
-   geoserver.workspace\_uri =
    '<a href="http://localhost:5000/ckan" class="uri">http://localhost:5000/ckan</a>'

Also requires this to be set:

ckan.datastore.write\_url =
'postgresql://ckanuser:<a href="mailto:pass@localhost/datastore" class="email">pass@localhost/datastore</a>'

Debugging
---------

Every time you pull new changes into your existing repository, you
should restart services to make sure all the files are compiled. You can
use the following command for this:

    $ supervisorctl restart all

If you run into issues while pulling new changes into your existing
repository, you should run setup.py which will set up the environment
correctly. See below:

    $ python setup.py egg_info

Also, if you run into issues with the website being inaccessible, you
can restart the http service by using the following command:

    $ service httpd restart

