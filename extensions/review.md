---
layout: extension
name: review
title: Review datasets at a set interval
author: XVTSolutions
homepage: https://github.com/XVTSolutions/ckanext-review
github_user: XVTSolutions
github_repo: ckanext-review
category: Extension
featured: 
permalink: /extension/review/
---


ckanext-review
==============
Allows datasets to be reviewed at a set interval.

+ Adds a 'package_review' table to the database to store data related to the review process.
+ Adds a 'group_review' table to the database to store data related to the review process.
+ Adds a 'Dataset Review Interval' field to organisations that allows users to set the default review period for datasets.
+ Adds a 'Next Review' field to dataset new/edit screens which defaults to today + 'Dataset Review Interval'
+ Adds a 'Mark as Reviewed' button to dataset view page.

Installation
-------------
1. clone this repository
2. install: `python ckanext-review/setup.py develop`
3. add `review` to the list of plugins in .ini file
4. Ensure ckan is configured to send emails: http://docs.ckan.org/en/latest/maintaining/email-notifications.html
4. Create a cron job that runs once a day to create activity stream items when packages are due to be reviewed i.e.
	
	1 0 * * *  /usr/lib/ckan/default/bin/paster --plugin=ckanext-review notify -c /etc/ckan/default/development.ini



