---
layout: extension
name: openafrica
title: CKAN extension for Open Africa
author: CodeForAfrica
homepage: https://github.com/CodeForAfrica/ckanext-openafrica
github_user: CodeForAfrica
github_repo: ckanext-openafrica
category: Extension
featured: 
permalink: /extension/openafrica/
---


openAFRICA CKAN Extension
=========================

CKAN theme for openAFRICA platform accessible at
<a href="https://openafrica.net/" class="uri">https://openafrica.net/</a>

### Development

Then follow the steps below to install the openAfrica extension:

Step 1:

-   Activate your virtual environment; use the path to your virtual
    environment. On Mac OSX, you may have to use
    `/usr/local/lib/ckan/default/bin/activate`. You can copy the code as
    it is below, including the preceeding dot.

<!-- -->

    . /usr/lib/ckan/default/bin/activate

Step 2:

-   Install the extension

If you are not a developer and just want to install the extension from
package, just run this command from your virtual environment:

    pip install ckanext-openafrica

> **Note**: If you wish to modify the extension in any way, you can
> download the source code and install the extension manually. To do so,
> execute the following command:
>
>     $ pip install -e git+https://github.com/CodeForAfrica/ckanext-openafrica.git#egg=ckanext-openafrica
>
> **Alternatively**: You can clone this repo (preferrably into the /src
> directory where you installed CKAN), cd into ckanext-openafrica and
> run
>
>     $ python setup.py develop

Step 3:

-   Modify your configuration file (generally in
    `/etc/ckan/default/production.ini`) and add `openafrica` in the
    `ckan.plugins` property.

<!-- -->

    ckan.plugins = openafrica <OTHER_PLUGINS>

Step 4:

-   Restart your server:

<!-- -->

    paster serve /etc/ckan/default/production.ini

OR

    paster serve --reload /etc/ckan/default/production.ini

With `--reload`, your server is restarted automatically whenever you
make changes in your source code.

If your extension is installed successfully, your page will change to
the openAfrica theme.

**Note**: This extension, being a thememing extension, may override
templates from other extensions. Templates in
/ckanext/openafrica/templates may require some modifications to render
properly with openAfrica extension.

Contributing
------------

If you've found a bug/issue in the extension, open a new issue
[here](https://github.com/CodeForAfrica/ckanext-openafrica/issues/new)
\_ (try searching first to see if there's already an
[issue](https://github.com/CodeForAfrica/ckanext-openafrica/issues) for
your bug).

If you are interested in contributing to the development of openAfrica
extension, you are welcome. A good starting point will be reading the
CKAN general [Contributing
guide](http://docs.ckan.org/en/ckan-2.7.0/contributing/index.html). Then
you can checkout existing
[issues](https://github.com/CodeForAfrica/ckanext-openafrica/issues)
that are open for contribution; new features and issues are welcome. To
work on any issue, comment on the issue to indicate your interest and
the issue will be assigned to you. It is always a good idea to seek for
clarification (where necessary) on any issue you work on.

**It is important that changes that require some form of configurations
should be documented in the README.**

------------------------------------------------------------------------

License
-------

GNU General Public License

openAFRICA aims to be the largest independent repository of open data on
the African continent. Copyright (C) 2017 Code for Africa

This program is free software: you can redistribute it and/or modify it
under the terms of the GNU General Public License as published by the
Free Software Foundation, either version 3 of the License, or (at your
option) any later version.

This program is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General
Public License for more details.

You should have received a copy of the GNU General Public License along
with this program. If not, see
<a href="https://www.gnu.org/licenses/" class="uri">https://www.gnu.org/licenses/</a>.

