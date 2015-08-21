---
layout: extension
name: linkfinder
title: Finds links on resources that are actually html pages
author: Data.Gov.UK - Cabinet Office
homepage: https://github.com/datagovuk/ckanext-linkfinder
github_user: datagovuk
github_repo: ckanext-linkfinder
category: Extension
featured: 
permalink: /extension/linkfinder/
---


# ckanext-linkfinder

Sometimes when adding resources to CKAN, users mistakenly add a link to the page containing links to the data rather than the data itself.

This extension attempts, for a given resource to find the actual resources on the page.  This will only cover some cases and isn't a solution that will fix every problem.

By using an assortment of CSS, XPath and Regex on a per url (or per publisher) basis it is possible to find the important links in a HTML page.

## Installing ckanext-linkfinder

To install the extension ...

## Running the tests

Running the following command in the ckanext-linkfinder directory will run all of the available tests.

    nosetests
    

