---
layout: extension
name: ckan-automator
title: CKAN automator
author: Open north
homepage: https://github.com/opennorth/ckan-automator
github_user: opennorth
github_repo: ckan-automator
category: Extension
featured: 
permalink: /extension/ckan-automator/
---


This package is an wrapper of ckanapi that simplify management of groups, packages and resources via the API. The main raison d'être of the package is to upload resources contained in a local directory but it does much more:
- Creation, modification and deletion of groups, packages and resources
- When posting a group, package or resource, the scripts searches if the target already exists and use the right command (create or update) accordingly
- The update command does partial update (e.g, if you provide only one field, it will only update this field. By default, the update action completely replace the old version by the new one, even for fields not provided.)

##Important

- This script is mainly designed for CKAN 2.2+. Packages and groups features will work on previous version, but resource management will not since the filestore API has changed.

- This script works based on the ckanapi module: 

```
pip install ckanapi
```

- In order to upload large file, it might needed to increase the authorized size for upload, possibly in your web server (Example for nginx:`client_max_body_size 200M`) and in the CKAN config (`ckan.max_resource_size = 200M`). 

##Uploading a resource from a local directory.


The package is done to read a directory that must contain one subdirectory for each resource to upload. Each subdirectory must contain

- A metadata file named `metadata.json`
- The file to be uploaded

The metadata file follows the same structure as the CKAN API structure. Below is an example:

```
{
    "name": "modes-transports",
    "resources": [
        {
            "description": "This is the description of the resource",
            "format": "JPG",
            "name": "Resource Name",
            "url": "an-image.jpg"        }
    ]
}
```

Where `name` is the name of dataset and `url` is the filename of the resource to be uploaded (in the same directory). The directory [resource.example](./resource.example) shows an example.

Once the file to be uploaded is available with the metadata, one just has to call the 

```
ckanclient.push_from_directory('/path/to/file/to/upload/', '/path/to/move/treated/data'))
```

`ckan_uploader` is a complete scripts that uses the package to search for the directories, upload the resources and send a status mail. Most of the configuration is done in the file `config.cfg` (example provided: `config.cfg.example`)

##Other features

The package is also able to help manage groups and packages, for example to manage test/staging environments as well as production environments


###Group management

####Delete all groups

```
group_list = ckansource.get_group_list()
ckansource.delete_groups(group_list)

```

####Replicate group structure from another CKAN instance

```
group_list = ckansource.get_group_list()
ckanclient.push_groups(group_list)

```

###Package management

*Warning*: package assignment to an organization only works starting CKAN 2.2. Before that, the API does not support the `owner_org` attribute.

####Delete all packages from an instance

```
package_list = ckanclient.get_package_list()
ckanclient.delete_packages(package_list)
```

####Replicate selected packages from another instance 

(could be useful to set up a test/staging environment). If some resources are assigned to the package, they will be downloaded locally and pushed to the target CKAN instance.

```
source_packages = ckansource.get_package_list(["2001-census-statistics", "2006-surrey-census"])
ckanclient.push_package_list(package_list)

```


###Resource management

On top of scanning a directory, the script is also able to upload an ad hoc resource (the url can be either a local file or a remote file starting with http://) and assign it to a package.

```
resource = {
	'url': 'https://ckannet-storage.commondatastorage.googleapis.com/2013-10-27T16:40:24.027Z/open-data-census-database-2013-index-presentation-entries.csv', 
	'description': 'This is my description', 
	'format': 'CSV', 
	'name': 'Test resource'}

ckanclient.push_resource('injected-dataset', resource)

```
