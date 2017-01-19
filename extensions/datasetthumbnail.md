---
layout: extension
name: datasetthumbnail
title: Generation and display of thumbnail images for datasets
author: Aptivate
homepage: https://github.com/aptivate/ckanext-datasetthumbnail
github_user: aptivate
github_repo: ckanext-datasetthumbnail
category: Extension
featured: 
permalink: /extension/datasetthumbnail/
---


ckanext-datasetthumbnail
========================

This CKAN extension adds support for generation and display of thumbnail images. The helper function `thumbnail_url` can be called from a template, as in this example:

    {%raw%}{% {%endraw%}block thumbnail{%raw%} %}{%endraw%}
    {%raw%}{% {%endraw%}set thumbnail = h.thumbnail_url(package.id){%raw%} %}{%endraw%}
    {%raw%}{% {%endraw%}if  thumbnail{%raw%} %}{%endraw%}
        <a href="{{ h.url_for(controller='package', action='read', id=package.name) }}">
        <img class="dataset-list-thumbnail" src="{{ thumbnail }}">
        </a>
    {%raw%}{% {%endraw%}endif{%raw%} %}{%endraw%}
    {%raw%}{% {%endraw%}endblock{%raw%} %}{%endraw%}

-   If a resource exists with the name `thumbnail.png`, this will be used.
-   If no resource exists with this name and the logged-in user has sufficient access, the thumbnail will be generated from the first matching JPEG or PNG resource.
-   If no thumbnail exists at this point, a placeholder image will be used.

Requirements
------------

-   CKAN 2.5.2
-   Pillow 3.2.0 (with PngImagePlugin and JpegImagePlugin)

Installation
------------

To install ckanext-datasetthumbnail:

1.  Activate your CKAN virtual environment, for example:

        . /usr/lib/ckan/default/bin/activate

2.  Install the ckanext-datasetthumbnail Python package into your virtual environment:

        pip install ckanext-datasetthumbnail

3.  Add `datasetthumbnail` to the `ckan.plugins` setting in your CKAN config file (by default the config file is located at `/etc/ckan/default/production.ini`).
4.  Restart CKAN. For example if you've deployed CKAN with Apache on Ubuntu:

        sudo service apache2 reload

Config Settings
---------------

    # Show thumbnails
    # (optional, default: False).
    ckan.datasetthumbnail.show_thumbnail = True

    # Autogenerate thumbnails
    # (optional, default: False).
    ckan.datasetthumbnail.auto_generate = True

    # Generated thumbnail width
    # (optional, default: 140).
    ckan.datasetthumbnail.thumbnail_width = 140

    # Generated thumbnail height
    # (optional, default: int(width * 1.415)
    ckan.datasetthumbnail.thumbnail_height = 140

Development Installation
------------------------

To install ckanext-datasetthumbnail for development, activate your CKAN virtualenv and do:

    git clone https://github.com/aptivate/ckanext-datasetthumbnail.git
    cd ckanext-datasetthumbnail
    python setup.py develop
    pip install -r dev-requirements.txt

Running the Tests
-----------------

To run the tests, do:

    nosetests --nologcapture --with-pylons=test.ini

To run the tests and produce a coverage report, first make sure you have coverage installed in your virtualenv (`pip install coverage`) then run:

    nosetests --nologcapture --with-pylons=test.ini --with-coverage --cover-package=ckanext.datasetthumbnail --cover-inclusive --cover-erase --cover-tests

Registering ckanext-datasetthumbnail on PyPI
--------------------------------------------

ckanext-datasetthumbnail should be availabe on PyPI as <https://pypi.python.org/pypi/ckanext-datasetthumbnail>. If that link doesn't work, then you can register the project on PyPI for the first time by following these steps:

1.  Create a source distribution of the project:

        python setup.py sdist

2.  Register the project:

        python setup.py register

3.  Upload the source distribution to PyPI:

        python setup.py sdist upload

4.  Tag the first release of the project on GitHub with the version number from the `setup.py` file. For example if the version number in `setup.py` is 0.0.1 then do:

        git tag 0.0.1
        git push --tags

Releasing a New Version of ckanext-datasetthumbnail
---------------------------------------------------

ckanext-datasetthumbnail is availabe on PyPI as <https://pypi.python.org/pypi/ckanext-datasetthumbnail>. To publish a new version to PyPI follow these steps:

1.  Update the version number in the `setup.py` file. See [PEP 440](http://legacy.python.org/dev/peps/pep-0440/#public-version-identifiers) for how to choose version numbers.
2.  Create a source distribution of the new version:

        python setup.py sdist

3.  Upload the source distribution to PyPI:

        python setup.py sdist upload

4.  Tag the new release of the project on GitHub with the version number from the `setup.py` file. For example if the version number in `setup.py` is 0.0.2 then do:

        git tag 0.0.2
        git push --tags

About
-----

Copyright (c) 2016 [MapAction](http://mapaction.org). Developed by [Aptivate](http://aptivate.org).

Development of v1 of this plugin was funded by [ECHO](http://ec.europa.eu/echo).

!["Funded by European Union Humanitarian Aid"](http://www.echo-visibility.eu/wp-content/uploads/2014/02/EU_Flag_HA_2016_EN-300x272.png)

