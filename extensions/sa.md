---
layout: extension
name: sa
title: Custom CKAN extension for data
author: Open Knowledge
homepage: https://github.com/okfn/ckanext-sa
github_user: okfn
github_repo: ckanext-sa
category: Extension
featured: 
permalink: /extension/sa/
---


ckanext-sa
==========

Custom CKAN extension for [data.sa.gov.au](http://data.sa.gov.au/)

How to Install Locally for Development
--------------------------------------

1.  Install CKAN from source.

2.  Install ckanext-pdeu. Activate your CKAN virtual environment and:

        git clone https://github.com/okfn/ckanext-sa.git
        cd ckanext-sa
        python setup.py develop

3.  Edit the following settings to the `[app:main]` section of your CKAN config
    file (e.g. `development.ini` or `sa.ini`):

        ckan.plugins = stats sa datastore googleanalytics pages resource_proxy recline_preview pdf_preview text_preview
        ckan.site_title = data.sa.gov.au
        ckan.site_description = South Australian Government Data Directory
        ckan.featured_organizations = department-of-planning-transport-and-infrastructure, state-library-of-south-australia

        ckan.auth.anon_create_dataset = false
        ckan.auth.create_dataset_if_not_in_organization = false
        ckan.auth.user_create_organizations = false
        ckan.auth.user_create_groups = false
        ckan.auth.user_delete_groups = false
        ckan.auth.user_delete_organizations = false

        ckan.locale_default = en_GB

        ckan.tracking_enabled = true

        googleanalytics.id = xxxx
        googleanalytics.account = xxxx
        googleanalytics.username = xxxx
        googleanalytics.password = xxxx

4.  Run CKAN, e.g. `paster serve sa.ini`

Note on CKAN versions: at the time of writing the `master` branch of
ckanext-sa is intended to work with CKAN 2.1.1.

