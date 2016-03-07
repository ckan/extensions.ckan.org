---
layout: extension
name: googleauth
title: CKAN extension to use Google as authentication authority
author: Yacme S.r.l (dev@yacme.com)
homepage: https://github.com/yacme/ckanext-googleauth
github_user: yacme
github_repo: ckanext-googleauth
category: Extension
featured: 
permalink: /extension/googleauth/
---


ckanext-googleauth
===============

CKAN extension for use Google as authentication authority.

This extension allow users to authenticate in CKAN using their google account. Optionally, it's possible to filter users by google domain.

At the first access, the extension create a new user in CKAN with strong and complex password and username calculated from email address, substituting every non alphanumerical character with underscore "_".
For example: 'name.surname@domain.it' -> 'name_surname_domain_it'.

Requirements
------------

ckanext-googleauth was created and tested in CKAN 2.5.1; it was also tested in CKAN 2.4.1. The functioning with other versions of CKAN is not guaranteed.

To use this extension you must register your application with Google to obtaining authorization credentials. For more information please visit https://developers.google.com/identity/sign-in/web/devconsole-project 

Installation
------------

To install ckanext-googleauth:

1. Download ckanext-googleauth.zip from here (https://github.com/yacme/ckanext-googleauth/releases/download/1.0.0/ckanext-googleauth.zip) and uncompress it in /usr/lib/ckan/default/src.

2. Entry into /usr/lib/ckan/default/src/ckanext-googleauth.

3. Execute:

    <code>python setup.py install</code>

4. Configure Client ID and (optionally) Hosted Domain (See "Config Settings" section)

5. Add ``googleauth`` to the ``ckan.plugins`` setting in your CKAN config file (by default the config file is located at
   ``/etc/ckan/default/production.ini``).

6. Restart CKAN.

Config Settings
---------------

In your config file (``/etc/ckan/default/production.ini``) add these properties:

* ``ckan.googleauth_clientid = client_id_value`` (REQUIRED). It contains the Client ID. For more information on how to create Client ID please visit https://developers.google.com/identity/sign-in/web/devconsole-project.

* ``ckan.googleauth_hosted_domain = hosted_domain_value`` (OPTIONAL) It contains the domain authorized to authenticate. If it isn't set you will have access with any Google Account Credentials.

Development Installation
------------------------

To install ckanext-googleauth for development, activate your CKAN virtualenv and do::
	
    git clone https://github.com/yacme/ckanext-googleauth.git
    cd ckanext-googleauth
    python setup.py develop

License
-------
This extension is licensed under the terms of GNU AFFERO GENERAL PUBLIC LICENSE Version 3.

Credits
-------
This extension was developed with the support of ARPA Emilia Romagna.




