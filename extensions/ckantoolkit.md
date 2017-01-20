---
layout: extension
name: ckantoolkit
title: Backports for ckan
author: Ian Ward
homepage: https://github.com/ckan/ckantoolkit
github_user: ckan
github_repo: ckantoolkit
category: Extension
featured: 
permalink: /extension/ckantoolkit/
---


ckantoolkit
===========

[![Circle CI](https://circleci.com/gh/ckan/ckantoolkit.svg?style=svg)](https://circleci.com/gh/ckan/ckantoolkit)

ckantoolkit is a library that wraps `ckan.plugins.toolkit` with backported
attributes. This library is useful for writing extensions that work with
a wide range of CKAN versions.

Example
-------

``` python
# compatible with CKAN >= 2.5 only
from ckan.plugins.toolkit import ungettext
```

becomes:

``` python
# compatible with all CKAN versions!
from ckantoolkit import ungettext
```

ckantoolkit.tests
-----------------

ckantoolkit includes a `tests` submodule that points to the correct
ckan test module. e.g. If your extension builds on ckan's test factories
your import code:

``` python
try:
    from ckan.tests.factories import Sysadmin
except ImportError: # for ckan <= 2.3
    from ckan.new_tests.factories import Sysadmin
```

becomes:

``` python
from ckantoolkit.tests.factories import Sysadmin
```

