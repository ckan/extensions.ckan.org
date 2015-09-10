---
layout: extension
name: dataproxy
title: An extension that allows previewing remote database tables in CKAN recline view (MySQL, PostgreSQLl, MSSQL)
author: cphsolutionslab, fadeit ApS (http://fadeit.dk)
homepage: https://github.com/cphsolutionslab/ckanext-dataproxy
github_user: cphsolutionslab
github_repo: ckanext-dataproxy
category: Extension
featured: 
permalink: /extension/dataproxy/
---


ckanext-dataproxy
=========
ckanext-dataproxy is [CKAN](https://github.com/ckan/ckan) extension that enables previewing data from remote databases via SQLAlchemy. The extension is compatible with datastore by masking the dataproxy resource as a datastore resource so it could be requested via api/3/action/datastore_search or previewed in-browser with recline-preview.

Usage
-------
*Using this module assumes that CKAN server can access the database which is being proxied via resource.*

Create a dataset and navigate to resource adding form:
![create-resource](http://i.imgur.com/B7jAl7T.png)

Upon clicking on the DataProxy button, following fields appear:
![dataproxy-fields](http://i.imgur.com/iQexXDM.png)

 - The interface assists by providing default ports for various database types
 - Connection string (URL field) is automatically generated based on entered values
 - Connection string can be modified to pass additional parameters if necessary
 - Password will be encrypted with AES256 block cipher and replaced with \_password\_ placeholder

Upon navigating to the resource, recline will automatically render preview:
![recline-preview](http://i.imgur.com/OCA4tMf.png)
The resource is also accessible at api/3/action/datastore_search regardless if datastore extension itself is set up or not. The API response format is compatible with datastore resources*

Installing
-------
__NB! This module is developed on CKAN v2.2.1, compatibility with other version is not ensured__
1) Clone this repo  

```sh
cd /usr/lib/ckan/default/src
git clone https://github.com/cphsolutionslab/ckanext-dataproxy.git
cd ckanext-dataproxy
```

 2) Install requirements (It is not required to install drivers for databases you don't plan to proxy, see the file)  
```
pip install -r requirements.txt
```

__Additional packages may be required to compile the database-specific drivers. For Ubuntu, you may need:__

```
sudo apt-get install build-essential libmysqlclient-dev freetds-dev
```

3) Install the plugin  

```sh
python setup.py develop
```

4) Set the dataproxy secret in your CKAN settings file (e.g. /etc/ckan/default/production.ini)

For example, in the settings file:

```sh
# Password for AES256 key generation
ckan.dataproxy.secret = c9f56fdfd12ee615f3d858... # Don't actually use this string, use a random secret.
```
You can run the following command in your shell to generate a random secret:
```sh
echo "import hashlib ; from uuid import uuid4 ; print hashlib.sha256(str(uuid4())).hexdigest()" | python -
```

5) Enable the plugin, append 'dataproxy' to plugins:  

In your settings file (e.g. /etc/ckan/default/production.ini)
```
ckan.plugins = stats text_preview ... dataproxy
```

Tests
-------
TODO: No unit-tests currently

Known bugs
-------
1. if resource is file upload, then 'dataproxy' button will appear next to 'remove' button
2. can not change resource type to 'dataproxy' from existing resource, however existing 'dataproxy' resource can be changed to other type
3. download entire resource as csv not implemented

