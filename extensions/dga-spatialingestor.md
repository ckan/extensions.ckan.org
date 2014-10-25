---
layout: extension
name: dga-spatialingestor
title: Spatial Ingestor
author: data.gov.au
homepage: https://github.com/datagovau/dga-spatialingestor
github_user: datagovau
github_repo: dga-spatialingestor
category: Extension
featured: 
permalink: /extension/dga-spatialingestor/
---


===================================
dga-spatialingestor
===================================

Provides ingestion capability for CKAN that can be triggered on dataset update with https://github.com/datagovuk/ckanext-os


CKAN Configuration ini settings:

  ckan.plugins = os_wfs_server

  ckanext-os.spatial-datastore.jdbc.url = {"dbname":"geodatastore", "user":"user", "password":"password", "host":"localhost"}

  ckanext-os.spatial-ingester.filepath = /home/co/pyenv_dgu/src/os-spatialingester/spatial.ingester

Creating the PostGIS database in the existing CKAN datastore:

  owner=user

  db=ckan_datastore

  sudo -u postgres createdb -E UTF8 -O $owner $db

  sudo -u postgres psql $db -c "CREATE EXTENSION postgis;"

  sudo -u postgres psql $db -c "ALTER TABLE geometry_columns OWNER TO $owner; ALTER TABLE spatial_ref_sys OWNER TO $owner;"

  grant select on table geometry_columns to ckandga_data; # grant select to read only user

  #add GDA_1994 projection used by many australian datasets
  INSERT into spatial_ref_sys (srid, auth_name, auth_srid, proj4text, srtext) values ( 96643, 'sr-org', 6643, '', 'PROJCS["Albers134",GEOGCS["GCS_GDA_1994",DATUM["D_GDA_1994",SPHEROID["GRS_1980",6378137.0,298.257222101]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.017453292519943295]],PROJECTION["Albers"],PARAMETER["False_Easting",0.0],PARAMETER["False_Northing",0.0],PARAMETER["Central_Meridian",134.0],PARAMETER["Standard_Parallel_1",-18.0],PARAMETER["Standard_Parallel_2",-36.0],PARAMETER["Latitude_Of_Origin",0.0],UNIT["Meter",1.0]]');


example run
python dga-spatialingestor.py '{"dbname":"ckan_datastore", "user":"postgres", "password":"password", "host":"localhost"}' http://localhost:5000 256fa905-cf92-4d6c-8714-95e3da2ea3c2 geodataset
where http://localhost:5000 is the ckan api url
and 256fa905-cf92-4d6c-8714-95e3da2ea3c2 is the ckan api key
and geodataset is the dataset to import

