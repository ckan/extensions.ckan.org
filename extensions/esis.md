---
layout: extension
name: ckanext-esis
title: Ckan extension adding additional fields and controls for spectral data
author: CSTARS
homepage: https://github.com/CSTARS/ckanext-esis
github_user: CSTARS
github_repo: ckanext-esis
category: Extension
featured: 
permalink: /extension/ckanext-esis/
---


ckanext-esis
============

EcoSIS extension for CKAN adding resource controls for spectra


## CKAN 'IDE'
#### start pycharm
```
. /usr/lib/ckan/default/bin/activate
# run ckan as root
sudo ~/pycharm-community-4.0.1/bin/pycharm.sh
```

#### run setup
```
script = /usr/lib/ckan/default/bin/paster
script paramters = --plugin=ckan serve /etc/ckan/default/development.ini
```



## Allow local cross-site auth (dev only)
in ckan/lib/base.py
```
     def _set_cors(self):
-        response.headers['Access-Control-Allow-Origin'] = "*"
+        #response.headers['Access-Control-Allow-Origin'] = "*"
+        if 'Origin' in request.headers:
+            response.headers['Access-Control-Allow-Origin'] = request.headers['Origin']
+        else:
+            response.headers['Access-Control-Allow-Origin'] = "*"
+
         response.headers['Access-Control-Allow-Methods'] = \
             "POST, PUT, GET, DELETE, OPTIONS"
         response.headers['Access-Control-Allow-Headers'] = \
             "X-CKAN-API-KEY, Authorization, Content-Type"
 
+        response.headers['Access-Control-Allow-Credentials'] = "true"

```

