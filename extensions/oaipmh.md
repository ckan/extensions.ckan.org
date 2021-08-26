---
layout: extension
name: oaipmh
title: Open Archives Initiative-Protocol for Metadata Harvesting(OAI PMH) extension to CKAN
author: Kata team repository
homepage: https://github.com/kata-csc/ckanext-oaipmh
github_user: kata-csc
github_repo: ckanext-oaipmh
category: Extension
featured: 
permalink: /extension/oaipmh/
---


OAI-PMH harvester for CKAN. This extends CKAN harvester to parse OAI-PMH
metadata sources and import datasets. Supported metadata schemas are
oai\_dc (Dublin Core), CMDI (Component MetaData Infrastructure).

The list of supported verbs consists of:

-   GetRecord: fetches a single dataset.
-   Identify: when creating the client object ('harvest source'),
    displays information about this OAI-PMH server.
-   ListIdentifiers: fetches individual datasets' identifiers.
-   ListSets: fetches identifiers of sets.

Harvester configuration
=======================

Please make sure you have ckanext-harvest installed. You can add a
harvest source from CKAN UI and set the harvest source to use OAI-PMH
harvester.

Configuration options:

-   from: Harvest datasets starting from date YYYY-MM-DD.
-   limit: Import only first 'limit' number of XML files.
-   set: Harvest only from certain sets.
-   type: Harvest only certain type.
-   until: Harvest datasets before date YYYY-MM-DD.

Here is an example of a configuration object (the one that must be
entered in the configuration field):

    {
     "limit": 10,
     "set": ["hdl_10138_135703"],
     "from": "2014-03-03"
    }

