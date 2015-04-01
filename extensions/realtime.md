---
layout: extension
name: ckanext-realtime
title: CKAN Realtime Data extension
author: Alexandra Institute
homepage: https://github.com/alexandrainst/ckanext-realtime
github_user: alexandrainst
github_repo: ckanext-realtime
category: Extension
featured: 
permalink: /extension/ckanext-realtime/
---


[![image](https://travis-ci.org/alexandrainst/ckanext-realtime.png?branch=master)](https://travis-ci.org/alexandrainst/ckanext-realtime)

[![image](https://coveralls.io/repos/alexandrainst/ckanext-realtime/badge.png)](https://coveralls.io/r/alexandrainst/ckanext-realtime)

ckanext-realtime
================

**ckanext-realtime** is CKAN plugin which makes your CKAN site into a **Realtime Data Portal**. By using **CkanRT.js** library, client applications can subscribe to realtime events from *Observable Datastores*. Check out our demo app [here](http://gatesense.com/realtime/examples/ex2/).

For more info read the [docs](http://alexandrainst.github.io/ckanext-realtime/). Feel free to submit your ideas and pull requests if you would like to contribute.

Copying and License
-------------------

This material is copyright (c) 2014 [Alexandra Instituttet A/S](http://www.alexandra.dk/uk/pages/default.aspx) and [Gatesense](http://www.gatesense.com).

It is open and licensed under the GNU Affero General Public License (AGPL) v3.0 whose full text may be found at:

<http://www.fsf.org/licensing/licenses/agpl-3.0.html>

Quick Start Guide
=================

What's in the project?
----------------------

1.  CKAN extension which enables observable datastores
2.  Datastore listener script (bin/datastore\_listener)
3.  WebSocket server (bin/ckan\_wss)
4.  JavaScript library for communication with the realtime CKAN (client/CkanRT.js)

Environment
-----------

The project has been tested on **Arch Linux** and **Ubuntu 12.04** servers. That Said, you will need:

1.  Redis Server
2.  CKAN (tested on 2.2 but it should work with earlier minor releases as well).
3.  ckanext-datastore plugin enabled

Installation
------------

1.  Install the plugin

    > *$ python setup.py develop*

2.  Install the requirements

    > *$ pip install -r requirements.txt*

3.  Set ckanext-realtime specific configuration options in your ckan config (e.g. /etc/ckan/default/production.ini):

    > *\# ckanext-realtime settings*
    >
    > *\#at what url can the Action API be reached*
    > *ckan.realtime.ckan\_api\_url = <http://localhost:5000/api/3/action/>*
    >
    > *\# admin API key to be used by WebSocket server and datastore listener*
    > *ckan.realtime.apikey = \<api key\>*
    >
    > *\#redis server host*
    > *ckan.realtime.redis\_host = 127.0.0.1*
    >
    > *\#redis server port*
    > *ckan.realtime.redis\_port = 6379*
    >
    > *\#WebsocketServer port*
    > *ckan.realtime.wss\_port = 9000*

4.  Enable the plugin in the CKAN configuration file:

    > *\# datastore plugin is a requirement for the realtime plugin*
    > *ckan.plugin = ... datastore realtime*

Try
---

After installing and configuring the plugin, start up CKAN and Redis. Then start the Datastore Listener script so that it can notify you about changes to Observable Datastores using PostgreSQL LISTEN/NOTIFY feature:

> *$ python bin/datastore\_listener /etc/ckan/default/development.ini*

Lastly, start the WebSocket server:

> *$ python bin/ckan\_wss /etc/ckan/default/development.ini*

Now you are ready to run the client examples found in client/examples folder of the project.

Running Python Tests
--------------------

Copy test.ini.example to test.ini and add your specific test settings. In order to run python tests, you have to start solr server and run this command:

> *$ nosetests*

Running Jasmine Specs
---------------------

First, install jasmine test runner gem:

> *$ gem install jasmine*

Start the WebSocket server in the test mode:

> *$ python bin/ckan\_wss \<path\_to\_ckan\_config\> - -test*

Start the jasmine test runner:

> *$ rake jasmine*

And run the tests in your browser by navigating to *localhost:8888* in your browser. Alternatively, execute the tests directly in your shell:

> *$ rake jasmine:ci*

