---
layout: extension
name: ckan4j
title: CKAN java client library
author: SciamLab
homepage: https://github.com/sciamlab/ckan4j
github_user: sciamlab
github_repo: ckan4j
category: Extension
featured: 
permalink: /extension/ckan4j/
---


ckan4j
======
A java library to extend and access core functionalities of CKAN.

Why a CKAN java library
-----------------------
[CKAN](http://ckan.org) is a complete and performant open-source Data Management System (DMS)
built in Python and maintained by a quite large community leaded by the [Open Knowledge Foundation](http://okfn.org/).
It powers many data catalogs across the globe including [datahub.io](http://datahub.io),
[catalog.data.gov](http://catalog.data.gov) and [data.gov.uk](http://data.gov.uk/data/search)
among many other sites.
CKAN provide a well designed and powerful [RPC-style API](http://docs.ckan.org/en/latest/api/index.html)
that expose pratically all its core functionalities but when it comes to integration
with Java based or enterprise scale applications it present some lack of support. 
So, when we built the [opendatahub.it](http://www.opendatahub.it) federated catalog of
Italian open dataset we decided to create a Java based client library and extension to CKAN
to ease such integration and to decouple the portal and data harvester architecture
(based on Java tecnologies like [Hadoop](http://hadoop.apache.org/) and 
[Storm](http://storm.incubator.apache.org/)) from the CKAN itself.
ckan4j is the core library of such work released as open-source so that many other can
benefit from it


Features
--------
ckan4j is a Java client library that provide access to the CKAN
core functionalities and APIs using Java language. The key difference
respect other Java libraries for CKAN is the extension architecture which
is designed to extend the CKAN API adding specific enterprise grade
functionalities like: 

* Social Login (supported GitHub, Google+ and Facebook).
  It include capabilities to implement SSO with many other portal software 
* CKAN dataset and organizations statistics exposed as API
* CKAN tags statistics and classification data dump in JSON structures ready for [D3.js](http://d3js.org/) visualizations
* CKAN Database extension helper (direct access to CKAN data and manipulation of custom tables) 
* Seamless integration with java classification libraries and semantic tools 

Usage
--------
ckan4j is distributed as an [Eclipse](https://www.eclipse.org/) based [Maven](http://maven.apache.org/) project.
Once you build it, you can use it in webapps or generic Java client apps adding the jar to the classpath (it is not yet published on a Maven repo).
If you are interested on a reference implementation for a web api, you can give a look to [ckan4j-webapi](https://github.com/sciamlab/ckan4j-webapi).


Dependencies
-------------
ckan4j require the SciamLab [common-lib](https://github.com/sciamlab/common-lib)


Contribute
----------
SciamLab is maintaining the library but we are happy to consider your feedbacks
and contributions and we want this to be the result of a community effort.
To partecipate you can simply fork the repo and follow the
typical GitHub flow considering that every pull request must be associated with
an issue on GitHub
You can collaborate with [code](https://github.com/sciamlab/ckan4j/pulls) or
[ideas and bugs](https://github.com/sciamlab/ckan4j/issues)


License
-------

    Copyright 2013-2015 Sciamlab s.r.l.

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

