---
layout: extension
name: recombinant
title: Create datastore tables for organizations and provide combined output
author: open.canada.ca
homepage: https://github.com/open-data/ckanext-recombinant
github_user: open-data
github_repo: ckanext-recombinant
category: Extension
featured: 1
permalink: /extension/recombinant/
---


ckanext-recombinant
===================

This extension creates datasets and datastore tables for all
organizations in a ckan instance and allows combining the
data from all tables into a single CSV for exporting.

This lets us use CKAN's authentication to restrict users to
update only their organizations' tables but have all values
available as a single dataset for our public site.

Add this plugin to your CKAN configuration and link to the
table description file:

```ini
ckan.plugins = datastore recombinant

recombinant.tables = file:///.../mytables.json

#   module-path:file name may also be used, e.g:
#
# recombinant.tables = ckanext.atisummaries:recombinant_tables.json
#
#   will try to load "recombinant_tables.json" from the directory
#   containing the ckanext.atisummaries module
```


Example Table Description File
------------------------------

```json
[
  {
    "dataset_type": "ati-summaries",
    "title": "ATI Summaries",
    "fields": [
      {
        "label": "Request number",
        "datastore_id": "request_number",
        "datastore_type": "text",
        "xls_column_width": 15
      },
      {
        "label": "Pages",
        "datastore_id": "pages",
        "datastore_type": "int",
        "xls_column_width": 6
      }
    ],
    "datastore_primary_key": "request_number",
    "datastore_indexes": "request_number",
    "xls_organization_info": ["title", "name"],
    "xls_organization_style": "pattern: pattern solid, fore_color gray25;",
    "xls_header_style": "font: bold on; pattern: pattern solid, fore_color light_green;"
  }
]
```


