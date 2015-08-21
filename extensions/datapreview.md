---
layout: extension
name: datapreview
title: Data preview for ckan from local resource cache
author: Data.Gov.UK - Cabinet Office
homepage: https://github.com/datagovuk/ckanext-datapreview
github_user: datagovuk
github_repo: ckanext-datapreview
category: Extension
featured: 
permalink: /extension/datapreview/
---


# ckanext-datapreview

This CKAN extension supplies data from local storage or via a remote download, parses CSV/XLS and provides it at a URL that can be called by Recline or other CKAN data previewer.

e.g. for a spreadsheet it returns a JSON dict such as:

        {
            "fields": ['Name', 'Age'],
            "data": [['Bob', 42], ['Jill', 54]],
            "extra_text": "This preview shows only the first 10 rows",
            "max_results": 10,
            "length": 435,
            "url": "http://data.com/file.csv",
        }

(see helpers.proxy_query() )

This extension is a modified, but local implementation of the [OKFN dataproxy](https://github.com/okfn/dataproxy) that runs as a CKAN extension rather than on [Google AppEngine](http://jsonpdataproxy.appspot.com). This has been written to improve the performance on [data.gov.uk](data.gov.uk) and increase the maximum file size processed.

The interface to the extension::

    /data/preview/<resource_id>?max-results=N&encoding=utf-8

is not exactly the same - dataproxy requires the URL instead of the resource id - the data returned is identical. Rather than always fetching the data from the remote site the new controller at the above route will first attempt to find the data in the [ckanext-archiver](https://github.com/okfn/ckanext-archiver)'s local archive.

## Installation

The most straightforward method of installation is::

    git clone git://github.com/datagovuk/ckanext-datapreview.git
    cd ckanext-datapreview
    python setup.py develop

Or alternatively install directly using pip:

    pip install -e git+https://github.com/datagovuk/ckanext-datapreview.git#egg=ckanext-datapreview

Once complete the datapreview should be added to your ckan.plugins property in the appropriate .ini file.

## Config

In your CKAN config file, configure the following options:

### limit

The 'limit' is the maximum size of a file downloaded or loaded into memory. If the data is not stored locally, then you don't want to wait forever downloading it to be able to proxy it. And if the whole file needs to be loaded into memory to display the first 100 rows then you want to limit the file size. e.g. a 20MB XLS file may take up 100MB when parsed in memory, and you don't want to fill your server by loading anything much bigger. 

The limit is expressed in bytes, so the default of 5MB would be:

    ckan.datapreview.limit = 5242880

Local CSV files are not subject to this limit because the first 100 rows can be loaded without loading the whole file into memory.

## Requirements

* __ckanext-archiver__ - for the resource cache
* __messytables__ - (in setup.py)


## Problems

Currently when previewing this data with [recline.js](reclinejs.com) the dataproxy backend has a hard-coded URL to http://jsonpdataproxy.appspot.com which means it is unable to be used with this extension.

On data.gov.uk we have patched a local copy of recline to use the new datapreview, however a patch to the recline dataproxy backend should be feasible.

## Improvements

* Increases the limit on download size (doesn't have the appengine download limit)
* Uses the local archive cache if it exists rather than hitting the remote site (only if ckanext-archiver has retrieved the file).


