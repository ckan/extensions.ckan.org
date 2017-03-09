---
layout: extension
name: twitterview
title: A CKAN extension for previewing Twitter feed resources
author: Link Web Services Pty Ltd
homepage: https://github.com/DataShades/ckanext-twitterview
github_user: DataShades
github_repo: ckanext-twitterview
category: Extension
featured: 
permalink: /extension/twitterview/
---


ckanext-twitterview
===================

A CKAN extension for previewing Twitter feed resources.

Installing
----------

To install the extension:

    $ git clone https://github.com/DataShades/ckanext-twitterview.git
    $ . /usr/lib/ckan/default/bin/activate
    $ python setup.py develop

To activate it:

    Add it to the ckan.plugins in config file: ckan.plugins = twitter_view

    Add to the default_views field in config file: ckan.views.default_views = twitter_view

    Add settings to config:

      ckan.twitter.max_feeds_count = 10 (If the value is not setup, 20 tweets will be shown by default and a "Load more" button will appear under the last tweet)
      ckan.twitter.exclude_replies = False (If you want to exclude retweets change from False to True)

Creating Twitter feed resources
-------------------------------

To create a twitter resource, at the resource create form enter `` `Twitter Feed ``\` at Format field and `` `https://twitter.com/USERNAME ``\` at URL field, where USERNAME is name of the person or group you want to get infromation from, for exmaple: <https://twitter.com/ckanproject>

Testing
-------

Proceed with the instructions at <http://docs.ckan.org/en/latest/contributing/test.html> in Set up the test databases section.

After creating Test Databases, at CKAN test-core.ini file:

    Change the password for `sqlalchemy.url` field to connect the DB while testing.

Add in test.ini file (file in extension):

    ckan.twitter.max_feeds_count = 10 (If the value is not setup, it will show 20 by default and Load more button will appear under the last tweet)
    ckan.twitter.exclude_replies = False (If you want to exclude retweets change from False to True)

    Set the right use = config:/usr/lib/ckan/default/src/ckan/test-core.ini path to test-core.ini

Run the command from extension directory:

    nosetests --with-pylons=test.ini --nologcapture --rednose -s -x -v --reset-db

