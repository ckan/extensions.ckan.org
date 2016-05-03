---
layout: extension
name: textcaptcha
title: Text captcha for user registration
author: Link Web Services Pty Ltd
homepage: https://github.com/DataShades/ckanext-textcaptcha
github_user: DataShades
github_repo: ckanext-textcaptcha
category: Extension
featured: 
permalink: /extension/textcaptcha/
---


# CKAN TextCaptcha

A text based captcha for the [CKAN open data platform](http://ckan.org/) user registration form using http://textcaptcha.com.

## Requirements

Tested in CKAN 2.3 and 2.4

## Installation

To install CKAN TextCaptcha:

1. Activate your CKAN virtual environment, for example:

     . /usr/lib/ckan/default/bin/activate

2. Install the ckanext-textcaptcha Python package into your virtual environment:

     $ python setup.py install

3. Add ``textcaptcha`` to the ``ckan.plugins`` setting in your CKAN
   config file (by default the config file is located at
   ``/etc/ckan/default/production.ini``).

4. Restart CKAN. For example if you've deployed CKAN with Apache on Ubuntu:

     $ sudo service apache2 reload

## Config Settings

1. Add ``ckan.textcaptcha.url`` option to the ``/etc/ckan/default/production.ini`` that defines textcaptcha api url. For example http://api.textcaptcha.com/YOUR_EMAIL.json


## Development Installation

To install CKAN TextCaptcha for development, activate your CKAN virtualenv and
do:

     $ python setup.py develop

All dependencies will be installed automatically

## Copying and License

This material is copyright &copy; 2015 Link Web Services Pty Ltd

It is open and licensed under the GNU Affero General Public License (AGPL) v3.0 whose full text may be found at:

[http://www.fsf.org/licensing/licenses/agpl-3.0.html](http://www.fsf.org/licensing/licenses/agpl-3.0.html)

