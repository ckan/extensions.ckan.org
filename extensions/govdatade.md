---
layout: extension
name: govdatade
title: GovData
author: Fraunhofer FOKUS
homepage: https://github.com/fraunhoferfokus/ckanext-govdatade
github_user: fraunhoferfokus
github_repo: ckanext-govdatade
category: Extension
featured: 
permalink: /extension/govdatade/
---


# ckanext-govdatade

[![Build Status](https://travis-ci.org/fraunhoferfokus/ckanext-govdatade.png?branch=master)](https://travis-ci.org/fraunhoferfokus/ckanext-govdatade)

GovData.de specific CKAN extension

**Hinweis:** Dieses Repository wird nicht mehr für die Weiterentwicklung von GovData genutzt. Für Fragen, Anregungen und Diskussionen bzgl. GovData (www.govdata.de) nutzen Sie bitte die hier zur Verfügung gestellten Repositories: https://github.com/GovDataOfficial

### Dependencies

The GovData.de harvester relies on a group import feature, which is currently not implemented in the `ckanext-harvest`. Therefore a [fork][fork] with a feature branch is used as the dependency instead.

## Getting Started

If you are using Python virtual environment (virtualenv), activate it.

```bash
$ pip install -e git+git://github.com/fraunhoferfokus/ckanext-govdatade.git#egg=ckanext-govdatade
$ cd /path/to/virtualenv/src/ckanext-govdatade
$ pip install -r requirements.txt
$ python setup.py develop

$ cd /path/to/virtualenv/src/ckanext-harvester
$ pip install -r pip-requirements.txt
$ python setup.py develop
```

Add the following plugins to your CKAN configuration file:

```ini
ckan.plugins = stats harvest ckan_harvester bayern_harvester bremen_harvester hamburg_harvester rlp_harvester berlin_harvester moers_harvester rostock_harvester govapps_harvester datahub_harvester
```

Please make sure, that the CKAN process will have access to the logfile specified in `/path/to/virtualenv/src/ckanext-govdata/ckanext/govdatade/harvesters/config.ini`. After restarting CKAN the plugins should be ready to use.

[fork]: https://github.com/fraunhoferfokus/ckanext-harvest

## Testing

Unit tests are placed in the `ckanext/govdatade/tests` directory and can be run with the nose unit testing framework:

```bash
$ cd /path/to/virtualenv/src/ckanext-govdatade
$ nosetests
```

