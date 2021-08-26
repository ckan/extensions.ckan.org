---
layout: extension
name: iati-query-builder
title: CKAN Datastore query builder
author: International Aid Transparency Initiative
homepage: https://github.com/IATI/IATI-Query-Builder
github_user: IATI
github_repo: IATI-Query-Builder
category: Extension
featured: 
permalink: /extension/iati-query-builder/
---


IATI-Query-Builder
==================

[![License:
MIT](https://img.shields.io/badge/license-GPLv3-blue.svg)](https://github.com/IATI/IATI-Query-Builder#licence)

About
-----

A simple form that will build a query string that can then be used to
fetch data from the IATI Datastore API.

See it in action here -
<a href="http://datastore.iatistandard.org/query/index.php" class="uri">http://datastore.iatistandard.org/query/index.php</a>

Requirements
------------

A webserver running php and php-curl. PHP dependencies are managed using
[Composer](http://culttt.com/2013/01/07/what-is-php-composer/).

Installation
------------

    # Clone the repository and enter into the root folder
    git clone https://github.com/IATI/IATI-Query-Builder.git
    cd IATI-Query-Builder

    # Install dependencies
    composer install

    # If running for the first time, prepare the helper script that enables you to get data for current IATI publishers
    # This involves copying the file to a filename of your choice and uncommenting the code
    cp helpers/refresh_group_data.example.php helpers/YOUR_FILENAME.php
    nano helpers/YOUR_FILENAME.php

    # Run the script to get data for current IATI publishers using the CKAN API
    php helpers/YOUR_FILENAME.php

    # You may wish to ensure that the included codelists are up-to-date (optional)
    ./update-codelists.sh

    # Run a webserver
    php -S localhost:8000

    # Open a browser and visit localhost:8000

Helper scripts
--------------

### Getting the latest IATI publishers

The `/helpers` directory has a script `refresh_group_data.example.php`
that will enable you to get data relating to current IATI publishers.

Running this script will generate a `.json` file of 'groups' (i.e.
publishers) in use on the IATI registry, and this in turn will populate
the 'Reporting Organisation' multi-select element in the form.

### Getting the latest IATI publishers

The script `update-codelists.sh` will re-download latest versions of the
required codelists.

### Automating updates

To automate regular updates, you could set-up both of these scripts as a
cron job on your server.

