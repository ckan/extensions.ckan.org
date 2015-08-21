---
layout: extension
name: mongodb
title: CKAN extension for MongoDB
author: Alex Byrnes
homepage: https://github.com/alexbyrnes/ckanext-mongodb
github_user: alexbyrnes
github_repo: ckanext-mongodb
category: Extension
featured: 
permalink: /extension/mongodb/
---


ckanext-mongodb
===============

CKAN extension for MongoDB

##Installation (Ubuntu 10.04)

Install CKAN 1.7:
```
$ sudo apt-get update
$ echo "deb http://apt.ckan.org/ckan-1.7 lucid universe" | sudo tee /etc/apt/sources.list.d/ckan.list
$ wget -qO- "http://apt.ckan.org/packages_public.key" | sudo apt-key add -
$ sudo apt-get update
$ sudo apt-get install -y ckan postgresql-8.4 solr-jetty
$ sudo ckan-setup-solr
$ sudo ckan-create-instance std default.vm.buildkit yes
$ sudo touch /var/lib/ckan/std/wsgi.py
$ sudo paster --plugin=ckan user add admin --config=/etc/ckan/std/std.ini
$ sudo paster --plugin=ckan sysadmin add admin --config=/etc/ckan/std/std.ini
```

Check localhost (or wherever you installed).  You should see a CKAN installation.  See http://ckan.readthedocs.org/en/ckan-1.7.1/install-from-package.html for more information.

Install MongoDB:

    $ sudo apt-get install mongodb

Activate CKAN's virtual environment (you may need to su or lower security for /var/lib/ckan/):

    $ source /var/lib/ckan/std/pyenv/bin/activate

Install this extension:

    (pyenv)$ pip install -e 'git+git://github.com/alexbyrnes/ckanext-mongodb.git#egg=ckanext-mongodb'

Edit the CKAN ini:

    $ sudo vim /etc/ckan/std/std.ini
  
Change this line: 
    
    ckan.plugins = stats synchronous_search
to

    ckan.plugins = stats synchronous_search mongodb

Reload apache:

    $ sudo /etc/init.d/apache2 reload

The extension should now be installed.  Add a data set by clicking "Add a Dataset" on the front page.

Now fire up a python shell (the virtual environment needs to be activated):

    (pyenv)$ python

```python
>>> from pymongo import Connection
>>> con = Connection()
>>> col = con.ckan_db.datasets
>>> for p in col.find():
...    p
```

Hit enter twice and you should see the contents of your dataset in python dictionary form.

Now, since p is still set to the dataset, you can modify it to show that when the dataset is viewed, it's actually coming from MongoDB:

```python
>>> p['notes'] = 'BIG OBVIOUS CHANGE'
>>> col.save(p)
```

Go to "Search" from the front page of CKAN, and voila, you should see the text above in the search.  All datasets will be saved to the local MongoDB collection ckan_db.packages.

Simple API at:

    http://<SERVER NAME>:28017/ckan_db/datasets/

More info on Mongo APIs: http://www.mongodb.org/display/DOCS/Http+Interface#HttpInterface-SimpleRESTInterface



