---
layout: extension
name: repo
title: Shows information about the CKAN version an instance is running
author: CKAN
homepage: https://github.com/ckan/ckanext-repo
github_user: ckan
github_repo: ckanext-repo
category: Extension
featured: 
permalink: /extension/repo/
---


ckanext-repo
============

Shows information about the HEAD (branch and latest commit) your ckan and
extension repositories are running on. This is done checking the local
repositories on your server.

## Install

With your virtualenv activated:

    cd src
    git clone https://github.com/ckan/ckanext-repo.git
    cd ckanext-repo
    python setup.py develop


Add the following plugin to your CKAN ini file:

    ckan.plugins = ... repo_info

After restarting your server you should see a snippet with the CKAN repository
information added to your footer.

![Screenshot](http://i.imgur.com/pUWRYdE.png)


## Configuration

By default the extension will only show information about the core `ckan` repo.

You can choose which repositories to get information from with the
`ckanext.repo.repos` configuration option. This one expects a space-separated
list of local repositories to check, in the form `<github_org>/<github_repo>`.
If the `github_org` part is not provided, `ckan` is assumed. For instance:

    ckanext.repo.repos = ckan okfn/ckanext-glasgow ckanext-oauth2waad ckanapi

You can also specify the location where the CKAN sources are installed with 
`ckanext.repo.srcpath` configuration option. For instance:
    ckanext.repo.srcpath = /usr/src


## FAQ

* *What does 'Last Updated' really mean?*

  That's the time of the last `git pull` on that repository

## License

(c) Open Knowledge, licensed under the [GNU Affero General Public License (AGPL) v3.0](http://www.fsf.org/licensing/licenses/agpl-3.0.html).
 



