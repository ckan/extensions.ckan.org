---
layout: extension
name: openapiviewer
title: Provides Swagger / Open API Console Preview for Resources that refer to APIs
author: Government of British Columbia, Brock Anderson
homepage: https://github.com/bcgov/ckanext-openapiviewer
github_user: bcgov
github_repo: ckanext-openapiviewer
category: Extension
featured: 
permalink: /extension/openapiviewer/
---


ckanext-openapi
===============

This CKAN Extension creates an OpenAPI (aka Swagger) view that is
accessible for previewing OpenAPI JSON resources. ([example](https://catalogue.data.gov.bc.ca/dataset/bc-data-catalogue-api))

1.  Pre-Installation

1.1 Create a new resource format in CKAN called 'openapi-json' using
these instructions:

    1.1.1. Get the id for resource_format:

    GET /api/action/vocabulary_show?id=resource_format

    The request should return a json object with id in result, you'll need the value associated with the id key.

    1.1.2. Create a POST for tag_create:

    POST /api/action/tag_create
    Content-Type: application/json
    Authorization: <user api key>

    {
        "vocabulary_id": "<id value from the first step>",
        "name": "openapi-json"
    }

    If all goes well, the request should return something like this:

    {
        "help": "http://10.1.0.2:5000/packages?ver=%2F1&name=tag_create&logic_function=help_show", 
        "success": true, 
        "result": {
            "vocabulary_id": "a42b7f16-b269-46c1-9464-98edc903fa81", 
            "packages": [], 
            "display_name": "openapi-json", 
            "id": "a3d45295-4fe8-4b64-8de0-d1e43e45a6e2", 
            "name": "openapi-json"
        }
    }

Note: the openapi\_view plugin is only be visible to resources with
format of 'openapi-json'

1.  Installation

2.1 Copy ckanext-openapi into the ckan src folder

2.2. Within src/ckanext-openapi run:

    python setup.py develop

2.3. Add 'openapi\_view' to the list of plugins in your .ini file.

Note: If this extension is installed alongside ckanext-bcgov, be sure to
list the 'openapi\_view' plugin *before* the various 'edc' plugins in
the .ini file.

If this extension is installed alongside pdf\_view, be sure to list the
'openapi\_view' plugin *before* pdf\_view.

2.4. Add the new resource view to the CKAN database:

paster views create openapi\_view -c INI\_FILE

2.5. Startup ckan

