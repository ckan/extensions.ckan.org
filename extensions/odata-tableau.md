---
layout: extension
name: odata-tableau
title: OData endpoint; fork optimized for Tableau Public
author: OpenGov/Ontodia
homepage: https://github.com/jqnatividad/ckanext-odata
github_user: jqnatividad
github_repo: ckanext-odata
category: Extension
featured: 1
permalink: /extension/odata-tableau/
---


=============
ckanext-odata
=============

This CKAN extension provides a basic OData 3.0 endpoint for CKAN. This allows it to talk to tools like the **FREE** [Tableau Public](https://public.tableau.com/s/) for [awesome visualizations using data from CKAN](http://data.beta.nyc/showcase?tags=tableau)!

The endpoint requires data to be held in the CKAN Datastore.
An *OData Endpoint* link is added to resources, showing up as an additional endpoint when the Data API button is pressed.

Usage
-----

This fork supports the following [OData parameters](http://www.odata.org/documentation/odata-version-3-0/odata-version-3-0-core-protocol/):

-   $skip - number of records to skip from top (default: 0)
-   $top - number of records to return (default:500)

The OData standard also specifies support for the **$filter** clause. However, implementing one is non-trivial as its a dialect that doesn't directly map to PostgreSQL.

Instead, we implemented a **$sqlfiter** clause, where the user can specify a PostgreSQL where clause. In our view, this is actually a more powerful implementation as the user has full access to PostgreSQL's filtering capabilities which is a superset of the OData $filter clause.

**Note:** $sqlfilter is mutually exclusive to the $skip and $top parameters, as you can specify skip/top functionality using SQL primitives (e.g. [$top -&gt; limit in SQL; $skip -&gt; offset in SQL](http://www.postgresql.org/docs/8.2/static/queries-limit.html))

Installation
------------

Installation as standard for CKAN.
This extension can be enabled by adding `odata` to the `plugin` line
in the CKAN configuration file.

