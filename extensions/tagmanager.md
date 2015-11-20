---
layout: extension
name: tagmanager
title: Tagmanager
author: Alan Tygel
homepage: https://github.com/alantygel/ckanext-tagmanager
github_user: alantygel
github_repo: ckanext-tagmanager
category: Extension
featured: 1
permalink: /extension/tagmanager/
---


ckanext-tagmanager
==================

Tagmanager offers tools and interfaces for cleaning tags in CKAN open data portals.

![image](http://stodap.org/tags/images/tag_manager_screenshot.png)

What can you do with the tagmanager plugin?
-------------------------------------------

The main features are the detection of similar tags, and the possibility to merge them. This is useful for portals with many contributors, where tags are not always kept consistent.

We offer three modes for detecting similar tags:

-   Strong similarity: detect tags that differ only by capitals special characters;
-   Medium similarity: detect tags that have a Levenshtein edit distance smaller than three;
-   Synonyms: show tags that are synonyms (only for English)

Why a tagmanager plugin?
------------------------

This extensions is intended to fill the tag management gap of CKAN. In the future, we plan to offer the creation of relationships between tags, and a tag recommendation structure.

Requirements
------------

Before installing tagmanager, make sure you have:

-   CKAN 2.5+
-   Levenshtein python library:

        pip install python-Levenshtein

-   Unidecode python library:

        pip install unidecode

-   NLTK library:

        pip install nltk

-   NLTK data:

        python -m nltk.downloader all

Installation
------------

To install ckanext-tagmanager:

1.  Activate your CKAN virtual environment, for example:

        . /usr/lib/ckan/default/bin/activate

2.  Install the ckanext-tagmanager Python package into your virtual environment:

        pip install ckanext-tagmanager

3.  Run the database migration:

        paster tagmanager migrate -c /etc/ckan/default/production.ini 

4.  Add `tagmanager` to the `ckan.plugins` setting in your CKAN config file (by default the config file is located at `/etc/ckan/default/production.ini`).
5.  Restart CKAN. For example if you've deployed CKAN with Apache on Ubuntu:

        sudo service apache2 reload

Development Installation
------------------------

To install ckanext-tagmanager for development, activate your CKAN virtualenv and do:

    git clone https://github.com/alantygel/ckanext-tagmanager.git
    cd ckanext-tagmanager
    python setup.py develop
    paster tagmanager migrate -c /etc/ckan/default/development.ini 
    pip install -r dev-requirements.txt

Use
---

Navigate to yoursite/tagmanager

Acknowledgements
----------------

This work was driven in the context of the research [STODaP](http://stodap.org/) project, developed at the Federal University of Rio de Janeiro (Brazil) and the University of Bonn (Germany)

