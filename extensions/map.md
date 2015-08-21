---
layout: extension
name: map
title: replace the default map preview with one that uses a Windshaft server that can handle millions of data points
author: U.K. Natural History Museum
homepage: https://github.com/NaturalHistoryMuseum/ckanext-map
github_user: NaturalHistoryMuseum
github_repo: ckanext-map
category: Extension
featured: 
permalink: /extension/map/
---


ckanext-tiledmap
===========

A Ckan plugin to create a map view that uses server-generated tiles, allowing for maps visualization of large datasets with millions of data points. The tile server to go with this extension is available at  <a href="https://github.com/NaturalHistoryMuseum/nhm-windshaft-app">https://github.com/NaturalHistoryMuseum/nhm-windshaft-app</a>

Note that this plugin requires the [ckanext-dataspatial](https://github.com/NaturalHistoryMuseum/ckanext-dataspatial) plugin, to create the geospatial columns in your dataset and provide functionality such as spatial query extent.

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

Tile server
----------------

You then need to setup a tile server. You can download the server at
<a href="https://github.com/NaturalHistoryMuseum/nhm-windshaft-app">https://github.com/NaturalHistoryMuseum/nhm-windshaft-app</a>
and configure it to set up the ckan datastore database.

Configuration
=============

The plugin supports the following configuration options:

- tiledmap.windshaft.host: The hostname of the tile server. There is no default, and the extension will not allow
  you to add map views if this is not defined;
- tiledmap.windshaft.port: The port for the tile server. There is no default, and the extension will not allow
  you to add map views if this is not defined;
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

