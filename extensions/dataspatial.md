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


Ckan Datastore Spatial extension
================================

*dataspatial* is a [Ckan](http://ckan.org) extension to provide geospatial awareness of datastore data. This includes:

-   Geospatial searches within datasets;
-   Spatial extent of datastore searches;
-   Support for [PostGIS](http://postgis.net);
-   Support for [Solr](http://solr.org) via the [datasolr](http://github.com/NaturalHistoryMuseum/ckanext-datasolr) ckan extension.

Usage
-----

When using PostGis, you will need to create PostGis columns on your dataset. There are actions and commands provided to do this for you, however you will need to embed those within your workflow. When using Solr, you will need to make sure the spatial data is indexed. It is up to you to manage this. Geospatial searches and query extent work both with PostGis and Solr - to use Solr you will need to install and configure the [datasolr](http://github.com/NaturalHistoryMuseum/ckanext-datasolr) extension for the datasets you wish to use Solr on.

### Create geospatial column on a PostGIS dataset

For geospatial searches to work using PostGIS, you need to have custom geometry columns in your dataset. *dataspatial* allows you to create those columns by invoking an action or a command. It will create two columns, one representing the [WGS](http://en.wikipedia.org/wiki/World_Geodetic_System) data, and one using the web mercator projection, which is useful for generating maps. By default (see **configuration**) the column names will be `_geom` and `_the_geom_webmercator` - the underscore prefix ensuring these columns will not be returned in search queries unless explicitly specified.

The columns can be created by calling the action `create_geom_columns`. From within a Ckan plugin, you would invoke this by doing:

``` python
    from ckan.plugins import toolkit as t
    t.get_action('create_geom_columns')(
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

Or by invoking the command:

        paster dataspatial -c <config file> create-columns <resource_id>

### Populate geospatial columns on a PostGIS dataset

In the current version, the geospatial column is not updated when a row is updated - this needs to be done separately. If you are using point data, then it can be done by calling the action `update_geom_columns`:

        from ckan.plugins import toolkit as t
        t.get_action('update_geom_columns')(
            context,
            {
                # The resource id, required.
                'resource_id': '...',
            
                # The dataset fields containing the latitude and longitude columns.
                'latitude_field': 'latitude',
                'longitude_field': 'longitude'
            }
        )

Or by invoking the command:

        paster dataspatial -c <config file> update-columns -l <latitude column> -g <longitude column> <resource_id>

### Perform a geospatial search using the datastore\_search API

This can be done by adding custom filter, `_tmgeom`, which contains a [WKT](http://en.wikipedia.org/wiki/Well-known_text) string. For example:

    import urllib
    url = 'http://data.nhm.ac.uk/api/action/datastore_search'
    search = {
        'q': 'ufo',
        'filters': '_tmgeom:POLYGON(36 114, 36 115, 37 115, 37 114, 36 114)' 
    }
    fileobj = urllib.urlopen(url + '?' + urllib.urlencode(search))
    print fileobj.read()

Or, as a URL:

    http://.../api/action/datastore_search?resource_id=6da71761-972d-492f-a0b9-3ba54db02632&q=ufo&filters=_tmgeom%3APOLYGON+((36+114%2C36+115%2C37+115%2c36+114))

### Obtain spatial extent for a given query

This can be done by invoking the action `datastore_query_extent`. For example:

    import urllib
    url = 'http://data.nhm.ac.uk/api/action/datastore_query_extent'
    search = {
        'q': 'ufo',
        'filters': '_tmgeom:POLYGON(36 114, 36 115, 37 115, 37 114, 36 114)' 
    }
    fileobj = urllib.urlopen(url + '?' + urllib.urlencode(search))
    print fileobj.read()

Configuration
-------------

``` ini
# Indicate whether query_extent queries should use the postgis or solr backend.
# Should be either 'postgis' (the default) or 'solr'
dataspatial.query_extent = postgis

# Name of the geospatial columns in the PostGIS database. postgis.field
# represents the WGS data, while postgis.mercator_field the
# web mercator projection which is used for building maps.
# The defaults are, respectively, _geom and _the_geom_webmercator
dataspatial.postgis.field = _geom
dataspatial.postgis.mercator_field = _the_geom_webmercator

# If datasolr is enabled, ckanext-spatial will provide geospatial search using
# solr. For this, specify the name of the spatial index in Solr. 
# Defaults to _geom
dataspatial.solr.index_field = _geom

# Name of the solr index for the longitude and latitude fields (If using solr 
# query extent, the lat/long field must be indexed as well as the spatial 
# index.) Default to, respectively, latitude and longitude
dataspatial.solr.latitude_field = latitude
dataspatial.solr.longitude_field = longitude
```

Postgis
-------

To use the Postgis backend, your postgresql database must have <a href="http://postgis.net/">postgis</a> support. On Ubuntu 12.04 LTS, assuming a
default postgres 9.1 install you can setup your database by doing:

``` bash
  sudo apt-get install -y postgresql-9.1-postgis
  sudo -u postgres psql -d ${DATASTORE_DB_NAME} -f /usr/share/postgresql/9.1/contrib/postgis-1.5/postgis.sql
  sudo -u postgres psql -d ${DATASTORE_DB_NAME} -c "ALTER TABLE geometry_columns OWNER TO $DB_USER"
  sudo -u postgres psql -d ${DATASTORE_DB_NAME} -c "ALTER TABLE spatial_ref_sys OWNER TO $DB_USER"
  sudo -u postgres psql -d ${DATASTORE_DB_NAME} -f /usr/share/postgresql/9.1/contrib/postgis-1.5/spatial_ref_sys.sql
```

Where `DATASTORE_DB_NAME` is the name of your postgres database that holds the datastore name, and `DB_USER` is
your database user.

