---
layout: extension
name: tableauview
title: A view plugin to display tableau public vizzes
author: Emanuele Tajariol - GeoSolutions
homepage: https://github.com/geosolutions-it/ckanext-tableauview
github_user: geosolutions-it
github_repo: ckanext-tableauview
category: Extension
featured: 
permalink: /extension/tableauview/
---


ckanext-tableauview - Viewer for tableau public
===============================================

This extension contains a view plugin to display tableau vizzes in CKAN.

Installation
------------

To install ckanext-tableauview on a production site:

1.  Activate your CKAN virtual environment, for example:

        source /usr/lib/ckan/default/bin/activate

2.  Install the ckanext-tableauview Python package into your virtual environment:

        pip install ckanext-tableauview

3.  Add the relevant plugins to the `ckan.plugins` setting in your CKAN config file (by default the config file is located at `/etc/ckan/default/production.ini`). Check [Available plugins]() to see which ones are available and if they require further configuration.
4.  Restart CKAN. For example if you've deployed CKAN with Apache on Ubuntu:

        sudo service apache2 reload

Development Installation
------------------------

To install ckanext-tableauview for development:

1.  Clone the source:

        cd /usr/lib/ckan/default/src
        git clone https://github.com/geosolutions-it/ckanext-tableauview.git

2.  Activate your CKAN virtual environment, for example:

        source /usr/lib/ckan/default/bin/activate

3.  Install the ckanext-tableauview Python package into your python virtual environment:

        cd ckanext-tableauview
        python setup.py develop

4.  Continue with the main installation instructions above (step 3 onwards).

Available plugins
-----------------

-   tableau\_view

Read the wiki page to see a configuration and display example.

Registering ckanext-tableauview on PyPI
---------------------------------------

ckanext-tableauview should be availabe on PyPI as <https://pypi.python.org/pypi/ckanext-tableauview>. If that link doesn't work, then you can register the project on PyPI for the first time by following these steps:

1.  Create a source distribution of the project:

        python setup.py sdist

2.  Register the project:

        python setup.py register

3.  Upload the source distribution to PyPI:

        python setup.py sdist upload

4.  Tag the first release of the project on GitHub with the version number from the `setup.py` file. For example if the version number in `setup.py` is 0.0.1 then do:

        git tag 0.0.1
        git push --tags

Releasing a new version of ckanext-tableauview
----------------------------------------------

ckanext-tableauview is availabe on PyPI as <https://pypi.python.org/pypi/ckanext-tableauview>. To publish a new version to PyPI follow these steps:

1.  Update the version number in the `setup.py` file. See [PEP 440](http://legacy.python.org/dev/peps/pep-0440/#public-version-identifiers) for how to choose version numbers.
2.  Create a source distribution of the new version:

        python setup.py sdist

3.  Upload the source distribution to PyPI:

        python setup.py sdist upload

4.  Tag the new release of the project on GitHub with the version number from the `setup.py` file. For example if the version number in `setup.py` is 0.0.2 then do:

        git tag 0.0.2
        git push --tags



