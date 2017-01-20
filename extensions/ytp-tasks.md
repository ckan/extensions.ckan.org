---
layout: extension
name: ytp-tasks
title: Task handling for YTP
author: yhteentoimivuuspalvelut
homepage: https://github.com/yhteentoimivuuspalvelut/ckanext-ytp-tasks
github_user: yhteentoimivuuspalvelut
github_repo: ckanext-ytp-tasks
category: Extension
featured: 
permalink: /extension/ytp-tasks/
---


ckanext-ytp-tasks
=================

Schduled task handling for CKAN and YTP tasks. Intented to be used with CKAN celery.

Requires Celery on CKAN.

Installation
------------

Installed as CKAN extension: ytp\_tasks

[See how to install CKAN extensions.](http://docs.ckan.org/en/latest/extensions/tutorial.html#installing-the-extension)

Configuration
-------------

Copy ytp\_celery.py.j2 to /etc/ckan/default/ytp\_celery.py and rename variables.

Execution
---------

sudo -u $CELERY\_USER /usr/lib/ckan/default/bin/celery beat --config=ytp\_celery --workdir=/etc/ckan/default/ --pidfile=/tmp/celerybeat\_pid --schedule=/tmp/celerybeat\_schedule

Commands
--------

Execute commands via paster:
/usr/lib/ckan/default/bin/paster --plugin=ckanext-ytp-tasks -c /etc/ckan/default/$CONFIG\_FILE <command-name> \[arguments...\]

::

    ytp-task-add - add task to scheduling

::

    ytp-tasks-initialize-database - initialize scheduling database

::

    ytp-task-execute-all - execute (queue) all tasks now

