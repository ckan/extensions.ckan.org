---
layout: extension
name: persona
title: A CKAN extension for logging in using Mozilla Persona
author: CKAN
homepage: https://github.com/ckan/ckanext-persona
github_user: ckan
github_repo: ckanext-persona
category: Extension
featured: 1
permalink: /extension/persona/
---


ckanext-persona
===============

A CKAN extension that lets users login to your CKAN site using
[Mozilla Persona](http://www.mozilla.org/en-US/persona/). Users can login
using just their existing email address, without having to create a new user
name and password for CKAN.

Traditional username and password login and registration are still enabled when this
plugin is active, the user is given the choice of Persona or traditional login.

For screenshots and details about how it works, see the [blog post](http://seanh.cc/posts/ckanext-persona/).

Installation
------------

ckanext-persona has been tested against that CKAN 2.3 development version.

To install, activate your CKAN virtualenv and then do:

    git clone 'https://github.co/mseanh/ckanext-persona.git'
    cd ckanext-persona
    python setup.py develop

Then add 'persona' to the ckan.plugins line in your CKAN config file, for example:

    ckan.plugins = resource_proxy stats datastore persona

Also make sure you have `ckan.site_url` set correctly in your config file, for example:

    ckan.site_url = http://scotdata.ckan.net

Finally, restart your web server.

Todo
----

There's a few things that need to be done before this plugin is ready for production use, including:

-   Handle multiple users with the same email address in CKAN:
    show all the accounts to the user, and ask her which one she wants
    to login to
    (currently it will crash if it finds an email address with multiple users)
-   Generate better unique user names based on emails
    (e.g. first half of email, with a random number appended if necessary)
-   Give the user a chance to change the generated username before their account is created
-   Verify SSL certificates (or is `requests` already doing this?)
-   Implement [CSRF protection](https://developer.mozilla.org/en-US/Persona/Security_Considerations)
-   Tests, Mozilla [recommend Selenium for this](https://developer.mozilla.org/en-US/Persona/The_implementor_s_guide/Testing?redirectlocale=en-US&redirectslug=Persona%2FThe_implementor_s_guide%2FTesting)
-   Better error handling when verification fails
-   Implement logging-in via Persona without JavaScript

There are also some changes to CKAN core that would be nice to have:

-   Allow passwordless accounts in CKAN, so this plugin doesn't have to generate passwords
    that will never be used <https://github.com/ckan/ckan/issues/1459>
-   Allow users to have multiple email addresses in CKAN, and verify those addresses using Persona:
    <https://developer.mozilla.org/en-US/Persona/The_implementor_s_guide/Adding_extra_email_addresses_with_Persona>
-   Add an API function to CKAN for searching for users by email, so this plugin
    doesn't need to access CKAN's model directly to do it
-   Tweak the templates in CKAN that this plugin overrides,
    we need a couple of new template blocks on the login and register pages in CKAN so that his plugin
    doesn't need to duplicate template code from core


