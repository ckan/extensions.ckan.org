---
layout: extension
name: embed
title: jQuery widget to embed CKAN datasets on external sites
author: Oleg Lavrovsky (https://github.com/datalets)
homepage: https://github.com/opendata-swiss/ckan-embed
github_user: opendata-swiss
github_repo: ckan-embed
category: Extension
featured: 
permalink: /extension/embed/
---


ckan-embed
==========

This module supports embedding information dynamically from CKAN data portals into other websites. Currently only dataset (package) search results are supported. For background on this project visit the [Swiss OGD Handbook](http://handbook.opendata.swiss/en/library/embed.html).

Usage notes
-----------

This script can be used with any recent [CKAN](http://ckan.org) portal. It exposes a ck module which has a datasets funciton. The first parameter is the DOM container into which the widget should be loaded, the second parameter a fully qualified URL to the target CKAN portal, and the third can be a free text search query (for example, "statistik").

Add [jQuery](https://www.npmjs.com/package/jquery), [Underscore](https://www.npmjs.com/package/underscore), [ckan](https://www.npmjs.com/package/ckan) and the *ckan-embed* scripts into the `<head>` (alternatively, use your own package manager):

``` html
<script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.1.1/jquery.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/underscore.js/1.8.3/underscore-min.js"></script>
<script src="https://cdn.rawgit.com/okfn/ckan.js/master/ckan.js"></script>
<script src="https://cdn.rawgit.com/opendata-swiss/ckan-embed/1.0.0/dist/ckan-embed.min.js"></script>
```

Place the container and init code somewhere in the page:

``` html
<div id="example-1">
    Loading '<a href="https://opendata.swiss">statistik</a>' datasets ...
</div>
...
<script>
ck.datasets('#example-1', 'https://opendata.swiss/', 'statistik');
</script>
```

The widget will then render in the `#example-1` container. Some styling possibilities, such as showing the logo of the portal, are explored in `test/style.css`.

### Advanced options

The script may also be initialized with a configuration object, for example in this case to show three datasets tagged 'hospitals', without using JSONP and instead proxying the requests through to the API at the `/ckanproxy/` path:

``` js
ck.datasets('#example-2', 'https://opendata.swiss/', {
    fq:       'tags:hospitals',
    rows:     3,
    lang:     'de',
    jsonp:    false,
    proxy:    '/ckanproxy/'
}
```

-   `fq`: allows use of [filter queries](http://docs.ckan.org/en/latest/api/index.html?highlight=filter%20queries)
-   `rows`: limit the number of results shown
-   `lang`: default language for result links
-   `jsonp`: toggle the use of JSONP (see note below)
-   `proxy`: relative or absolute path to API proxy

NOTE: if you are running this script on the same server or using a backend proxy (supported in all web servers) to the CKAN API, we recommend that you *disable* JSONP with the `jsonp: false` option.

For more usage examples see `test/index.html`.

Developer notes
---------------

For information on the JavaScript CKAN client see [ckan.js](https://github.com/okfn/ckan.js), for details of API usage see [docs.ckan.org](http://docs.ckan.org/en/latest/api/) for [package\_search](http://docs.ckan.org/en/latest/api/index.html?highlight=organization_list#ckan.logic.action.get.package_search).

A web server like [NGINX can be used](https://www.nginx.com/resources/admin-guide/reverse-proxy/) to proxy requests and avoid the use of JSONP.

Build Process
-------------

To build `ckan-embed.js` and view the test examples, you must have [npm](https://www.npmjs.com/) installed.

1.  Run `npm install` in the ckan-embed folder to install dependencies.
2.  Run `npm run build` (this will invoke [browserify](http://browserify.org/) to bundle the source files, and then [uglify-js](http://lisperator.net/uglifyjs/) to create the minified version).
3.  Run `bower install` to fetch local versions of the `lodash` and `jquery` libraries for the test instance.
4.  Run a local webserver (e.g., `python -m SimpleHTTPServer 8000`) in the root folder and then point your web browser at the test directory (e.g., `http://localhost:8000/test/`).

Acknowledgments
---------------

Developed with support from the [Swiss Federal Archives](https://www.bar.admin.ch).

This project was initially based on [vega-embed](https://github.com/vega/vega-embed).

