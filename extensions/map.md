---
layout: extension
name: map
title: Map visualisation for NHM CKAN
author: Natural History Museum
homepage: https://github.com/NaturalHistoryMuseum/ckanext-map
github_user: NaturalHistoryMuseum
github_repo: ckanext-map
category: Extension
featured: 
permalink: /extension/map/
---


ckanext-tiledmap
===========

Note: this version of the extention requires a custom ckan branch. That can be found at
https://github.com/NaturalHistoryMuseum/ckan/tree/1251-1725-custom and combines patches from CKAN's 1251 and 1725
branches (both of which should be merged into CKAN in the near future).

A CKAN plugin to replace the default map preview with one that uses a
<a href="https://github.com/CartoDB/Windshaft">Windshaft</a> server to generate the map tiles and interactivity layer.

The point of this extention is to provide maps that can handle millions of data points. The Windshaft server itself is
available at
<a href="https://github.com/NaturalHistoryMuseum/nhm-windshaft-app">https://github.com/NaturalHistoryMuseum/nhm-windshaft-app</a>

Features:
- Tiled maps with plot, grid and heatmap views;
- On-map geospatial search reflected in other views (eg. grid view).

setup
=====

Postgis
-------

Your postgresql database must have <a href="http://postgis.net/">postgis</a> support. On Ubuntu 12.04 LTS, assuming a
default postgres 9.1 install you can setup your database by doing:

```bash
  sudo apt-get install -y postgresql-9.1-postgis
  sudo -u postgres psql -d ${DATASTORE_DB_NAME} -f /usr/share/postgresql/9.1/contrib/postgis-1.5/postgis.sql
  sudo -u postgres psql -d ${DATASTORE_DB_NAME} -c "ALTER TABLE geometry_columns OWNER TO $DB_USER"
  sudo -u postgres psql -d ${DATASTORE_DB_NAME} -c "ALTER TABLE spatial_ref_sys OWNER TO $DB_USER"
  sudo -u postgres psql -d ${DATASTORE_DB_NAME} -f /usr/share/postgresql/9.1/contrib/postgis-1.5/spatial_ref_sys.sql
```

Where ```DATASTORE_DB_NAME``` is the name of your postgres database that holds the datastore name, and ```DB_USER``` is
your database user.

Windshaft server
----------------

You then need to setup a windshaft server. You can download the server at
<a href="https://github.com/NaturalHistoryMuseum/nhm-windshaft-app">https://github.com/NaturalHistoryMuseum/nhm-windshaft-app</a>
and configure it to set up the ckan datastore database.

Configuration
=============

The plugin supports the following configuration options:

- tiledmap.windshaft.host: The hostname of the windshaft server. There is no default, and the extension will not allow
  you to add map views if this is not defined;
- tiledmap.windshaft.port: The port for the windshaft server. There is no default, and the extension will not allow
  you to add map views if this is not defined;
- tiledmap.geom_field: This is the name of the webmercator projection geom field that gets created and added to the
  resource table. Defaults to ```_the_geom_webmercator``` (Note that using a leading _ ensures the field won't be
  visible to datastore searches);
- tiledmap.geom_field_4326: This is the name of the lat/long geom field that gets created and added to the resource
  table. Defaults to ```_geom```. (Note that using a leading _ ensures the field won't be
  visible to datastore searches);
- tiledmap.tile_layer.url: URL of the tile layer. Defaults to http://otile1.mqcdn.com/tiles/1.0.0/map/{z}/{x}/{y}.jpg ;
- tiledmap.tile_layer.opacity: Opacity of the tile layer. Defaults to 0.8 ;
- tiledmap.initial_zoom.min: Minimum zoom level for initial display of dataset, defaults to 2;
- tiledmap.initial_zoom.max: Maximum zoom level for initial display of dataset, defaults to 6;
- tiledmap.style.plot.fill_color: Default fill color for plot markers. Users can override this per-view. Defaults to
  '#EE0000';
- tiledmap.style.plot.line_color: Default line color for plot markers. Users can override this per-view. Defaults to
  '#FFFFFF';
- tiledmap.style.plot.marker_size': Size of the plot marker. Cannot be overriden per-view as it has a notable
  performance impact. Defaults to 8;
- tiledmap.style.plot.grid_resolution: Resolution of the grid used to generator hover/popup information on the map.
  Cannot be overriden per-view as it has a notable performance impact. Should typically be half the marker size.
  Defaults to 4;
- tiledmap.style.gridded.base_color: Default base color for grid views. Users can override this per-view. Defaults to
  '#F02323';
- tiledmap.style.gridded.marker_size: Marker size for the grid view. Cannot be overidden per-view as it has a notable
  performance impact. Defaults to 8;
- tiledmap.style.gridded.grid_resolution: Grid resolution for the grid view. Cannot be overridden per-view as it has a
  notable performance impact. Should be the same as the marker size. Defaults to 8;
- tiledmap.style.heatmap.intensity: Default heat map intensitiy. Users can override this per-view. Defaults to 0.1;
- tiledmap.style.heatmap.gradient: Heat map gradient colors. Defaults to
  '#0000FF, #00FFFF, #00FF00, #FFFF00, #FFA500, #FF0000',
- tiledmap.style.heatmap.marker_url: Heatmap marker. Defaults to '!markers!/alpharadiantdeg20px.png' (where !markers!
  is the marker directory on the windshaft server);
- tiledmap.style.heatmap.marker_size: Heatmap marker size. Defaults to 20.


Usage
=====

Users
-----

Once the plugin has been enabled (added to the list of plugins in the .ini file), users can add tiled map views from
the resource management page. Users will select (amongst other options) the latitude and longitude fields in their
dataset. The extension will then automatically create (and populate) geometry columns as required.

Developers
----------

Developers who want to manually create the columns can use the following actions:

```python
    import ckan.plugins.toolkit as toolkit
    create_geom_columns = toolkit.get_action('create_geom_columns')
    create_geom_columns(context, {
        'resource_id': resource_id,
        'lat_field': 'latitude',
        'long_field': 'longitude'
    })
```

The code will add the two geometry columns (by default ```_geom``` and ```_the_geom_webmercator```) to the given resource
database table, and will populate those fields using the (existing) ```latitude``` and ```longitude``` fields.

You can also create the columns without populating the table by passing in ```'populate': False```. You can then
populate the columns later (or update already populated columns) by doing:

```python
    import ckan.plugins.toolkit as toolkit
    update_geom_columns = toolkit.get_action('updated_geom_columns')
    updated_geom_columns(context, {
        'resource_id': resource_id,
        'lat_field': 'latitude',
        'long_field': 'longitude'
    })
```

And finally, the plugin also provides paster scripts to add geometry columns to a given datastore resource; though we
recommend calling the actions from your own code you can use this initially when testing/setting up:

```
paster ckanextmap add-all-geoms -c <path to your config file>
```
