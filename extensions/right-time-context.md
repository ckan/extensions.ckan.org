---
layout: extension
name: right-time-context
title: CKAN extension providing right time context support through FIWARE NGSI
author: CoNWeT
homepage: https://github.com/conwetlab/ckanext-right_time_context
github_user: conwetlab
github_repo: ckanext-right_time_context
category: Extension
featured: 
permalink: /extension/right-time-context/
---


CKAN ckanext-right\_time\_context
=================================

[![Build
Status](https://travis-ci.org/conwetlab/ckanext-right_time_context.svg?branch=master)](https://travis-ci.org/conwetlab/ckanext-right_time_context)
[![Coverage
Status](https://coveralls.io/repos/github/conwetlab/ckanext-right_time_context/badge.svg?branch=master)](https://coveralls.io/github/conwetlab/ckanext-right_time_context?branch=master)

CKAN extension that will give you the ability to manage right-time
resources provided by a FIWARE Context Broker. This extension also
provides a basic view to provide a data preview to user browsing context
broker resources, altough it can be combined with other plugins (e.g.
the
[`ckanext-wirecloud_view`](https://github.com/conwetlab/ckanext-wirecloud_view.git)
one) to provide a more advanced visualization of the data provided using
CKAN.

**Note**: This extension is being tested using CKAN 2.5, 2.6, 2.7 and
2.8. These are therefore considered as the supported versions

Requirements
------------

-   `resource_proxy`. This extension is required to be able to make
    requests to the Context Broker and thus is required for the raw view
    (`ngsi-view`) provided by this plugin.
-   [OAuth2 CKAN
    Extension](https://github.com/conwetlab/ckanext-oauth2/). This
    extension is required to make request to secured Context Broker
    instances. The autentication token will be taken from the current
    user session, so the accessed context broker must be connected to
    the same IdM server as the one used to login into CKAN, if not, the
    token will not work.

Installation
------------

To install `ckanext-right_time_context`:

1.  Activate your CKAN virtual environment, for example:

        . /usr/lib/ckan/default/bin/activate

2.  Install the `ckanext-right_time_context` python package into your
    virtual environment:

        pip install ckanext-right_time_context

3.  Add `right_time_context` to the `ckan.plugins` setting in your CKAN
    config file (e.g. `/etc/ckan/default/production.ini`). If you want
    to make use of the raw view provided by this plugin, you will have
    to ensure the `resource_proxy` is also enabled (comes directly with
    CKAN, but it is not enabled by default)

4.  Restart CKAN. For example if you've deployed CKAN with Apache:

        sudo service apache2 graceful

> Please take a look into the [`ckanext-oauth2` installation
> guide](https://github.com/conwetlab/ckanext-oauth2/wiki/Activating-and-Installing)
> if you are interested on linking secured context brokers.

Development Installation
------------------------

To install `ckanext-right_time_context` for development, activate your
CKAN virtualenv and do:

    git clone https://github.com/conwetlab/ckanext-right_time_context.git
    cd ckanext-right_time_context
    python setup.py develop

How it works
------------

### How to create a `fiware-ngsi` resource

The way to create a NGSI resource is fairly simple:

1.  Firstly you have to access to the form for creating a new resource.

    ![Create resource form](images/create_resource_form.png)

2.  Use `fiware-ngsi` to fill the `Format` field, this will make the
    form change adding some extra fields required when using the
    `fiware-ngsi` format.

    ![Create resource after switching to the fiware-ngsi
    format](images/create_resource_form_fiwarengsi.png)

3.  Fill the `URL` field with a Context Broker query. It is recommended
    to use a NGSIv2 query, but it is possible to use also a v1
    convenience query context url. Examples are:

    -   `http://orion.lab.fiware.org:1026/v2/entities?type=AirQualityObserved`
    -   `http://orion.lab.fiware.org:1026/v1/contextEntities/MeteoLo`

4.  Finally, check if you have to use some of the extra options:
    -   Set `Auth Type` to the appropiate value if the Context Broker
        server requires authentication.
    -   Fill the `FIWARE-Service` field if the data is not provided by
        the default
        [tenant](http://fiware-orion.readthedocs.io/en/master/user/multitenancy/).
    -   And finally, fill the `FIWARE-ServicePath` field if the data
        should be filtered using a [service
        path](http://fiware-orion.readthedocs.io/en/master/user/service_path/).
5.  Once you provide all the requested information, click on the *Add*
    button.

