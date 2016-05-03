---
layout: extension
name: dgvat_xls
title: Extension to allow organization admins to export organization datasets to Excel
author: Data.gv.at - Austria
homepage: https://github.com/datagvat/ckanext-dgvat_xls
github_user: datagvat
github_repo: ckanext-dgvat_xls
category: Extension
featured: 
permalink: /extension/dgvat_xls/
---


Dgvat XLS-Export Extension
==========================

The dgvat XLS-export extension allows group-admin to export datasets from their organizations to export all datasets to a .xls worksheet. Sysadmins may choose to export datasets from any organization they want or to export all datasets of all groups.

**Note: This extension requires ckan 2.2 or higher**

Activating and Installing
-------------------------

Install the plugin to your pyenv-environment.

This will also register a plugin entry point, so you now should be able to add the following to your CKAN .ini file:

    ckan.plugins = dgvat_xls <other-plugins>

Set up the needed values in your ini:

    dgvat_xls.template = NAME_AND_PATH_OF_YOUR_XLS_TEMPLATE_FILE  
    dgvat_xls.path = FULL_QUALIFIED_PATH - where the generated file should be stored 
                     (has to be reachable if you want to download the generated file)  
    dgvat_xls.url = PUBLIC_DIRECTORY_FOR_DOWNLOAD - defaults to "/exportFiles/" used for the download link  

Using the Extension
-------------------

The plugin is now reachable at: \<your\_ckan\_url\>/export\_xls

