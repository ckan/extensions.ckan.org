---
layout: extension
name: stromnetzberlin
title: ckanext-stromnetzberlin
author: Fraunhofer FOKUS
homepage: https://github.com/fraunhoferfokus/ckanext-stromnetzberlin
github_user: fraunhoferfokus
github_repo: ckanext-stromnetzberlin
category: Extension
featured: 
permalink: /extension/stromnetzberlin/
---


# ckanext-stromnetzberlin

A CKAN extension for harvesting Stromnetz Berlin.

### Dependencies

The harvester relies on a group import feature, which is currently not implemented in the `ckanext-harvest`. Therefore a [fork][fork] with a feature branch is used as the dependency instead.

## Getting Started

If you are using Python virtual environment (virtualenv), activate it.

```
$ pip install -e git+git://github.com/fraunhoferfokus/ckanext-stromnetzberlin.git#egg=ckanext-stromnetzberlin
$ cd /path/to/virtualenv/src/ckanext-stromnetzberlin
$ pip install -r pip-requirements
$ python setup.py develop

$ cd /path/to/virtualenv/src/ckanext-harvest
$ pip install -r pip-requirements
$ python setup.py develop
```

Add the following plugins to your CKAN configuration file:

```
ckan.plugins = harvest stromnetz_harvester
```

Please make sure, that the CKAN process will have access to the logfile specified in `/path/to/virtualenv/src/ckanext-stromnetzberlin/ckanext/stromnetzberlin/config.ini`. After restarting CKAN the plugins should be ready to use.

## License

CKAN Extension for harvesting Stromnetz Berlin.

Copyright (C) 2013 Fraunhofer FOKUS

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as
published by the Free Software Foundation, either version 3 of the
License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.

[fork]: https://github.com/fraunhoferfokus/ckanext-harvest

