---
layout: extension
name: cartodb2ckan
title: Node script for automatically creating a CKAN dataset for a CartoDB table
author: Chris Whong
homepage: https://github.com/CartoDB/labs-cartodb2ckan
github_user: CartoDB
github_repo: labs-cartodb2ckan
category: Extension
featured: 1
permalink: /extension/cartodb2ckan/
---


#cartodb2ckan
Node script for automatically creating a CKAN dataset for a CartoDB table

##Overview

CartoDB is a mapping platform that incorporates a cloud PostgreSQL database with a full SQL API.  Once a dataset is in CartoDB and is made 'public', the SQL API can be accessed by anyone.  The SQL API can output in various formats, including CSV, geoJSON, and Shapefile(SHP).  

This script uses the CKAN API to create a new dataset in CKAN for a CartoDB public table that contains the table's name, along with CKAN 'resources' for each of the different export types.  It also creates a resource for the "public page" of the dataset on CartoDB.

##How to Use

###Download and Configuration

Clone this repo

Install dependencies `npm install`

Create `config.js` based on `config.sample.js` containing usernames, API keys, etc for your cartoDB account and CKAN instance.

###Run the Script

To run the script, pass in the name of a CartoDB table as an argument:

`node script.js {tableName}`

It should do its thing, and will open a new tab in your web brower with the new CKAN dataset page when it's complete.

This script is largely based on [this CKAN autopopulation script](https://github.com/socrata/socrata-ckan)

