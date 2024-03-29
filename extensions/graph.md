---
layout: extension
name: graph
title: CKAN extension for graph views, with data processing moved to the backend
author: U.K. Natural History Museum
homepage: https://github.com/NaturalHistoryMuseum/ckanext-graph
github_user: NaturalHistoryMuseum
github_repo: ckanext-graph
category: Extension
featured: 
permalink: /extension/graph/
---


<img src=".github/nhm-logo.svg" align="left" width="150px" height="100px" hspace="40"/>

ckanext-graph
=============

[![Travis](https://img.shields.io/travis/NaturalHistoryMuseum/ckanext-graph/master.svg?style=flat-square)](https://travis-ci.org/NaturalHistoryMuseum/ckanext-graph)
[![Coveralls](https://img.shields.io/coveralls/github/NaturalHistoryMuseum/ckanext-graph/master.svg?style=flat-square)](https://coveralls.io/github/NaturalHistoryMuseum/ckanext-graph)
[![CKAN](https://img.shields.io/badge/ckan-2.9.1-orange.svg?style=flat-square)](https://github.com/ckan/ckan)

*A CKAN extension that adds a graph view for resources.*

Overview
========

Adds graph views for resources on a CKAN instance. Two types of graph
are available: temporal (a line graph showing count over time based on a
specified date field), and categorical (a bar chart showing counts for
various values in a specified field).

**NB**: the current version of this extension only works with the
Natural History Museum's [ElasticSearch datastore CKAN
backend](https://github.com/NaturalHistoryMuseum/ckanext-versioned-datastore).
*However*, it is designed to be extensible, so if you would like to use
this extension with a different backend (e.g. the standard PostgreSQL
datastore), please see the [Extending](#extending) section.

Installation
============

Path variables used below:

-   `$INSTALL_FOLDER` (i.e. where CKAN is installed), e.g.
    `/usr/lib/ckan/default`
-   `$CONFIG_FILE`, e.g. `/etc/ckan/default/development.ini`

1.  Clone the repository into the `src` folder:

``` bash
cd $INSTALL_FOLDER/src
git clone https://github.com/NaturalHistoryMuseum/ckanext-graph.git
```

1.  Activate the virtual env:

``` bash
. $INSTALL_FOLDER/bin/activate
```

1.  Install the requirements from requirements.txt:

``` bash
cd $INSTALL_FOLDER/src/ckanext-graph
pip install -r requirements.txt
```

1.  Run setup.py:

``` bash
cd $INSTALL_FOLDER/src/ckanext-graph
python setup.py develop
```

1.  Add 'graph' to the list of plugins in your `$CONFIG_FILE`:

``` ini
ckan.plugins = ... graph
```

Configuration
=============

There is currently only one option that can be specified in your .ini
config file.

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr class="header">
<th>Name</th>
<th>Description</th>
<th>Options</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><code>ckanext.graph.backend</code></td>
<td>The name of the backend to use (currently only <code>elasticsearch</code> is implemented)</td>
<td>elasticsearch, sql</td>
<td>elasticsearch</td>
</tr>
</tbody>
</table>

Usage
=====

Templates
---------

The view will be added as an option with no further configuration
necessary. However, if you wish to override or add content to the
template, you can extend `templates/graph/view.html`:

``` html+jinja
{%raw%}{% {%endraw%}ckan_extends{%raw%} %}{%endraw%}

{%raw%}{% {%endraw%}block my_new_block{%raw%} %}{%endraw%}
  <p>Look, some exciting new content.</p>
{%raw%}{% {%endraw%}endblock{%raw%} %}{%endraw%}
```

Extending
=========

To use this extension with a datastore backend other than the
ElasticSearch backend already implemented, you'll have to subclass from
`Query` in `ckanext-graph/ckanext/graph/db.py`.

An unimplemented class for SQL queries is already in the file as an
example:

``` python
class SqlQuery(Query):
    @property
    def _date_query(self):
        raise NotImplementedError()

    @property
    def _count_query(self):
        raise NotImplementedError()

    def run(self):
        raise NotImplementedError()
```

If you add a new class, you'll have to add it to the dictionary in
`Query.new()` method to make it available as a configurable option.

If you do this, please submit a pull request! Contributions are always
welcome.

Testing
=======

*Test coverage is currently extremely limited.*

To run the tests in this extension, there is a Docker compose
configuration available in this repository to make it easy.

To run the tests against ckan 2.9.x on Python2:

1.  Build the required images

``` bash
docker-compose build
```

1.  Then run the tests. The root of the repository is mounted into the
    ckan container as a volume by the Docker compose configuration, so
    you should only need to rebuild the ckan image if you change the
    extension's dependencies.

``` bash
docker-compose run ckan
```

The ckan image uses the Dockerfile in the `docker/` folder which is
based on `openknowledge/ckan-dev:2.9-py2`.

