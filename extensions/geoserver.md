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


### Geoserver Extension for CKAN

custom configurations:

-   geoserver.rest\_url = 'geoserver://admin:<geoserver@localhost>:8080/geoserver/rest'
-   geoserver.default\_workspace = 'ckan'
-   geoserver.workspace\_name = ckan
-   geoserver.workspace\_uri = '<http://localhost:5000/ckan>'

Also requires this to be set:

ckan.datastore.write\_url = 'postgresql://ckanuser:<pass@localhost/datastore>'

#### Geoserver publishing (automated)

This extension contains two paster commands that can be used in conjunction with crontab & supervisor to automatically publish tier 3 data to NGDS services (Geoserver)

-   `paster geoserver publish-ogc-redis-queue`: this command will run a sql query against the database and return all eligible datasets (dataset package extra key `md_package` has to include `NGDS Tier 3 Data, csv format:` as its package extra value & it also must be tagged with a keyword that contains `usgincm:`) that can be published to ogc (geoserver). The ids of these datasets will be added to a redis queue (the name of the queue = `publish_ogc_queue` (info on redis queues and operations that can be performed on them can be found @ <http://redis.io>))
    We run this everything 15 minutes through a cronjob (See: <https://github.com/ngds/install-and-run/blob/master/rpm_install/etc/cron.d/ckan-harvest>)

-   `paster geoserver publish-ogc-worker`: This command will start a worker that runs in the background. It will pop dataset ids from the redis queue and publish them to ogc (geoserver). Worker processes can be managed through supervisor (see: <https://github.com/ngds/install-and-run/blob/master/rpm_install/etc/supervisord.conf>)

##### Possible ogc publishing errors:

-   `PUBLISH_OGC: Error Connecting to Redis while building publish_ogc_queue`: check redis connection paramenters in `production.ini`. Also make sure that the redis server is up and running.
-   `PUBLISH_OGC_QUEUE: There was en ERROR while pushing ids to publish_ogc_queue`: this means that `publish-ogs-redis-queue` was not able to add dataset ids to the redis queue. Check to see if the redis server is working as expected.
-   `PUBLISH_OGC_WORKER: ERROR, could not connect to Redis`: the worker was not able to connect to the redis server. Make sure the redis server is up and running.
-   `PUBLISH_OGC_WORKER: An Error has occured while publishing dataset`: this means that ckan threw an exception while publishing dataset ids to the redis queue. See what the exception says and go from there (most often it is an issue with ckan not bening able to reach the redis server.
-   `PUBLISH_OGC: ERROR, Could not get required API CALL parameters for dataset '`: this means that ckan doesn't have the necessary data to call the geoserver api (which publishes tier 3 data to ogc). See what data is missing and troubleshoot from there.


