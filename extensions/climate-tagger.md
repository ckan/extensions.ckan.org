---
layout: extension
name: climate-tagger
title: Reegle Climate Tagger CKAN Extension
author: Reegle
homepage: https://github.com/REEEP/ckanext-climate-tagger
github_user: REEEP
github_repo: ckanext-climate-tagger
category: Extension
featured: 
permalink: /extension/climate-tagger/
---


ckanext-climate-tagger
======================

The reegle Climate Tagger CKAN Extension provides suggested tags for climate compatible content (for CKAN) by introducing an additional field to the add/edit resource form that displays suggested tags from the Climate Tagger API hosted by reegle.

Make your CKAN open government data more easily searchable by leveraging the standardized taxonomy of tags provided by the Climate Tagger tags.

Current status: **beta**

More information about the tagging API can be found at <http://api.reegle.info>.

Features
--------

-   Climate Tagger tags available in English, French, Spanish, Portuguese and German

-   Ability to configure the relevance threshhold for tags returned bu the Climate tagger API

-   Clean separation from existing tags fields allows users to manually input their own tags

Install
-------

Fork or download this repository and install into the appropriate CKAN extensions directory. Traditionally, this is at **/usr/lib/ckan/default/src/**.

    git clone https://github.com/REEEP/ckanext-climate-tagger.git

To enable the extension, first activate your CKAN virtualenv:

``` bash
$ . /usr/lib/ckan/default/bin/activate
```

Then cd into the extension's top-level directory and run **setup.py**:

``` bash
(pyenv)$ cd /usr/lib/ckan/default/src/ckanext-climate-tagger
(pyenv)$ python setup.py develop
```

*(once configured, you may wish to run `python setup.py install` for production environments)*

And lastly, enable the plugin by adding climate\_tagger to ckan.plugins in your CKAN config file, usually development.ini on production.ini in /etc/ckan/default.

    ckan.plugins = stats text_view recline_view ... climate_tagger

More information on extending CKAN available at <http://docs.ckan.org/en/latest/extensions/tutorial.html>.

Configure
---------

1.  Create a free account at <http://api.reegle.info/register>.
2.  Register an API token at <http://api.reegle.info/dashboard/sources>.
3.  Configure the extension by adding your API token to the configure options in **ckanext-climate-tagger/ckanext/reegletagging/theme/public/ckanext-reegle-tagging.js** like so:

``` js
var reegle = {
  apiUrl: 'http://api.reegle.info/service/extract',
  authToken: 'your-auth-token-here!!'
};
```

License
-------

[CC0 1.0 universal](http://creativecommons.org/publicdomain/zero/1.0/)

