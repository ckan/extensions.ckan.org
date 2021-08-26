---
layout: extension
name: dataspatial
title: CKAN extension to enable geospatial searches within the datastore
author: U.K. Natural History Museum
homepage: https://github.com/NaturalHistoryMuseum/ckanext-dataspatial
github_user: NaturalHistoryMuseum
github_repo: ckanext-dataspatial
category: Extension
featured: 
permalink: /extension/dataspatial/
---


<img src=".github/nhm-logo.svg" align="left" width="150px" height="100px" hspace="40"/>

ckanext-dataspatial
===================

This extension is no longer maintained.
---------------------------------------

[![Travis](https://img.shields.io/travis/NaturalHistoryMuseum/ckanext-dataspatial/master.svg?style=flat-square)](https://travis-ci.org/NaturalHistoryMuseum/ckanext-dataspatial)
[![Coveralls](https://img.shields.io/coveralls/github/NaturalHistoryMuseum/ckanext-dataspatial/master.svg?style=flat-square)](https://coveralls.io/github/NaturalHistoryMuseum/ckanext-dataspatial)
[![CKAN](https://img.shields.io/badge/ckan-2.9.0a-orange.svg?style=flat-square)](https://github.com/ckan/ckan)

*A CKAN extension that provides geospatial awareness of datastore data.*

Overview
========

**NB**: This extension is *unmaintained*. There have been some syntax
updates so it *should* work with CKAN 2.8+, but it hasn't been tested
and is not currently in use by the Museum.

This extension provides geospatial awareness of datastore data. This
includes:

-   Geospatial searches within datasets;
-   Spatial extent of datastore searches;
-   Support for [PostGIS](http://postgis.net);
-   Support for [Solr](http://solr.org) via the
    [ckanext-datasolr](https://github.com/NaturalHistoryMuseum/ckanext-datasolr)
    extension.

Installation
============

Path variables used below:

-   `$INSTALL_FOLDER` (i.e. where CKAN is installed), e.g.
    `/usr/lib/ckan/default`
-   `$CONFIG_FILE`, e.g. `/etc/ckan/default/development.ini`

1.  Clone the repository into the `src` folder:

``` bash
cd $INSTALL_FOLDER/src
git clone https://github.com/NaturalHistoryMuseum/ckanext-dataspatial.git
```

1.  Activate the virtual env:

``` bash
. $INSTALL_FOLDER/bin/activate
```

1.  Install the requirements from requirements.txt:

``` bash
cd $INSTALL_FOLDER/src/ckanext-dataspatial
pip install -r requirements.txt
```

1.  Run setup.py:

``` bash
cd $INSTALL_FOLDER/src/ckanext-dataspatial
python setup.py develop
```

1.  Add 'dataspatial' to the list of plugins in your `$CONFIG_FILE`:

``` ini
ckan.plugins = ... dataspatial
```

Configuration
=============

There are a number of options that can be specified in your .ini config
file. They all have defaults set, so none are *required*.

<table style="width:100%;">
<colgroup>
<col style="width: 28%" />
<col style="width: 42%" />
<col style="width: 28%" />
</colgroup>
<thead>
<tr class="header">
<th>Name</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><code>dataspatial.query_extent</code></td>
<td>Which backend to use for query_extent queries (either 'postgis' or 'solr')</td>
<td>postgis</td>
</tr>
<tr class="even">
<td><code>dataspatial.postgis.field</code></td>
<td>WGS data field in the PostGIS database</td>
<td>_geom</td>
</tr>
<tr class="odd">
<td><code>dataspatial.postgis.mercator_field</code></td>
<td>Mercator field in the PostGIS database</td>
<td>_the_geom_webmercator</td>
</tr>
</tbody>
</table>

The following options only apply if the
[ckanext-datasolr](https://github.com/NaturalHistoryMuseum/ckanext-datasolr)
extension is also installed.

| Name                               | Description             | Default   |
|------------------------------------|-------------------------|-----------|
| `dataspatial.solr.index_field`     | Spatial index in Solr   | \_geom    |
| `dataspatial.solr.latitude_field`  | Latitude index in Solr  | latitude  |
| `dataspatial.solr.longitude_field` | Longitude index in Solr | longitude |

Further Setup
=============

Geospatial searches and query extent work both with PostGIS and Solr,
but both require further setup before they can be used.

PostGIS
-------

To use the PostGIS backend, your PostgreSQL database must have
[PostGIS](http://postgis.net) support.

1.  Install the correct version of PostGIS for your version of
    PostgreSQL, e.g. for PostgreSQL 9.1 on Ubuntu:

``` bash
sudo apt-get install postgresql-9.1-postgis
```

1.  Run scripts to install the extension and change permissions
    (`$DATASTORE_DB_NAME` is the name of your PostgreSQL database that
    holds the datastore, and `$DB_USER` is your database user).

``` bash
sudo -u postgres psql -d $DATASTORE_DB_NAME -f /usr/share/postgresql/9.1/contrib/postgis-1.5/postgis.sql
sudo -u postgres psql -d $DATASTORE_DB_NAME -c "ALTER TABLE geometry_columns OWNER TO $DB_USER"
sudo -u postgres psql -d $DATASTORE_DB_NAME -c "ALTER TABLE spatial_ref_sys OWNER TO $DB_USER"
sudo -u postgres psql -d $DATASTORE_DB_NAME -f /usr/share/postgresql/9.1/contrib/postgis-1.5/spatial_ref_sys.sql
```

1.  You will then need to create PostGIS columns on your resources.
    Invoking the command below will create the two columns named above
    (`dataspatial.postgis.field` and
    `dataspatial.postgis.mercator_field`) on table `$RESOURCE_ID`. One
    represents the
    [WGS](http://en.wikipedia.org/wiki/World_Geodetic_System) (World
    Geodetic System) data, and one uses the web mercator projection,
    which is useful for generating maps.

    ``` bash
    paster --plugin=ckanext-dataspatial dataspatial create-columns $RESOURCE_ID -c $CONFIG_FILE
    ```

Solr
----

When using Solr, you will need to make sure the spatial data is indexed;
this extension does not provide any tools for doing this. To use Solr
you will need to install and configure the
[ckanext-datasolr](http://github.com/NaturalHistoryMuseum/ckanext-datasolr)
extension for the datasets you wish to use Solr on.

Usage
=====

Actions
-------

### `create_geom_columns`

Creates the PostGIS columns on the `$RESOURCE_ID` table. Can also
populate the columns (if `populate` is True) and create an index (if
`index` is True).

``` python
from ckan.plugins import toolkit

toolkit.get_action('create_geom_columns')(
    context,
    {
        # The resource id, required.
        'resource_id': '...',

        # If True then populate the geom columns from lat/long
        # points after creating them. Optional, defaults to True
        'populate': True,

        # If True, then create an index of the geom columns. Optional, defaults to
        # True
        'index': True,

        # The dataset fields containing the latitude and longitude columns.
        # Required if (and only if) populate is True.
        'latitude_field': 'latitude',
        'longitude_field': 'longitude'
    }
)
```

### `update_geom_columns`

Updates the geospatial column when a row is updated (this is not done
automatically so must be implemented in your own workflow). Equivalent
to the `populate-columns` [command](#commands).

``` python
from ckan.plugins import toolkit

toolkit.get_action('update_geom_columns')(
    context,
    {
        'resource_id': 'RESOURCE_ID',
        'latitude_field': 'LATITUDE_COLUMN',
        'longitude_field': 'LONGITUDE_COLUMN'
    }
)
```

### `datastore_search`

Searching by geospatial fields involves passing a custom filter to
`datastore_search`. The filter `_tmgeom` contains a
[WKT](http://en.wikipedia.org/wiki/Well-known_text) (Well-Known Text)
string representing the area to be searched (currently, only the types
`POLYGON` or `MULTIPOLYGON` will work). e.g.:

``` python
from ckan.plugins import toolkit

search_params = {
    'resource_id': 'RESOURCE_ID',
    'filters': '_tmgeom:POLYGON(36 114, 36 115, 37 115, 37 114, 36 114)'
}
search = toolkit.get_action(u'datastore_search')(context, search_params)
```

### `datastore_query_extent`

To see the geospatial extent of the query, the same parameters as above
can be submitted to the action `datastore_query_extent`:

``` python
from ckan.plugins import toolkit

search_params = {
    'resource_id': 'RESOURCE_ID',
    'filters': '_tmgeom:POLYGON(36 114, 36 115, 37 115, 37 114, 36 114)'
}
search = toolkit.get_action(u'datastore_query_extent')(context, search_params)
```

This will return a `dict`: Key\|Description ---\|-----------
`total_count`\|Total number of rows matching the query
`geom_count`\|Number of rows matching the query that have geospatial
information `bounds`\|((lat min, long min), (lat max, long max)) for the
queries rows

Commands
--------

### `dataspatial`

1.  `create-columns`: create the PostGIS columns on the `$RESOURCE_ID`
    table.
    `bash  paster --plugin=ckanext-dataspatial dataspatial create-columns $RESOURCE_ID -c $CONFIG_FILE`

2.  `create-index`: create index for PostGIS columns on the
    `$RESOURCE_ID` table.
    `bash  paster --plugin=ckanext-dataspatial dataspatial create-index $RESOURCE_ID -c $CONFIG_FILE`

3.  `populate-columns`: populate the PostGIS columns from the given lat
    & long fields. Equivalent to the `update_geom_columns()` action.
    `bash  paster --plugin=ckanext-dataspatial dataspatial populate-columns $RESOURCE_ID -l $LATITUDE_COLUMN -g $LONGITUDE_COLUMN -c $CONFIG_FILE`

Testing
=======

*Test coverage is currently extremely limited.*

To run the tests, use nosetests inside your virtualenv. The
`--nocapture` flag will allow you to see the debug statements.

``` bash
nosetests --ckan --with-pylons=$TEST_CONFIG_FILE --where=$INSTALL_FOLDER/src/ckanext-dataspatial --nologcapture --nocapture
```

