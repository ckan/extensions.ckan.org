---
layout: extension
name: dev
title: CKAN extention for development tools
author: Natural History Museum
homepage: https://github.com/NaturalHistoryMuseum/ckanext-dev
github_user: NaturalHistoryMuseum
github_repo: ckanext-dev
category: Extension
featured: 
permalink: /extension/dev/
---


ckanext-dev
===========

CKAN extension that provides various development tools :

- An IPython shell, run within the CKAN environment, started as a paster script ;
- A configuration option to start PyCharm remote debugger session

Setup
------

To enable the remote debugger session, you need:

- Install the pycharm-debug.egg package on the remote machine (this file is part of the PyCharm
  distribution, see http://www.jetbrains.com/pycharm/webhelp/remote-debugging.html)

- Add the line 'debug.remote = True' to your configuration file (this is independent from Ckan's
  debug setting ; both can be enabled or disabled separately) ;

- Setup a Remote Debugger within PyCharm, using port 8888 (or as defined by debug.host.port).

You may optionally define:
- debug.remote.host.ip for the host IP (defaults to 10.0.2.2 which is the default host IP when using Vagrant) ;
- debug.remote.host.port for the host port (defaults to 8888; it needs to match the setting in PyCharm) ;
- debug.remote.stdout_to_server to send stdout to the debugging host (defaults to True) ;
- debug.remote.stderr_to_server to send stderr to the debugging host (defaults to True) ;
- debug.remote.suspend defines whether the debugger should break as soon as it is started (defaults to False).


Usage
-----

To use the paster launched shell do:

paster --plugin=ckanext-dev shell -c &lt;path to your config file&gt;
