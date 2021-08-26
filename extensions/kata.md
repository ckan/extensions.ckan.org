---
layout: extension
name: kata
title: KATA extensions for CKAN
author: Kata team repository
homepage: https://github.com/kata-csc/ckanext-kata
github_user: kata-csc
github_repo: ckanext-kata
category: Extension
featured: 
permalink: /extension/kata/
---


This repository was part of an older version of Etsin which is no longer in use. For the newest version of Etsin, see <a href="https://github.com/CSCfi/etsin-finder/" class="uri">https://github.com/CSCfi/etsin-finder/</a>
=============================================================================================================================================================================================================================

Kata is a CKAN extension for handling metadata of research datasets. It
is used in [Etsin research data
finder](https://etsin.avointiede.fi/en/).

Installation
============

You can install the extension with:

`pip install -e git://github.com/kata-csc/ckanext-kata.git#egg=ckanext-kata`

Requirements
============

-   CKAN 2.4.1
-   Some additional Python packages that will be installed using
    `pip install`
-   CKAN extension ckanext-ytp-comments:
    <a href="https://github.com/kata-csc/ckanext-ytp-comments/tree/etsin" class="uri">https://github.com/kata-csc/ckanext-ytp-comments/tree/etsin</a>
-   ClamAV (if kata.storage.malware\_scan=true):
    <a href="http://www.clamav.net/index.html" class="uri">http://www.clamav.net/index.html</a>

Configuration
=============

Put the following lines under \[app:main\] in CKAN configuration file

> kata.storage.malware\_scan = true

> kata.is\_backup = false

If Google Analytics is on, add

> kata.ga\_id = \[GA ID\]

If LDAP is used, add basic LDAP configuration to the aforementioned
file:

> kata.ldap.enabled = true

> kata.ldap.password = \[LDAP PASSWORD\]

> kata.ldap.server = \[LDAP SERVER\]

> kata.ldap.dn = \[DN\]

> kata.ldap.basedn = \[BASE DN\]

For contact emails following settings apply:

> kata.bf = \[ENCRYPTION KEY\]

To enable reCaptcha set:

> kata.contact\_captcha = true

Note that this setting requires captcha keys to be set

The email feature can be turned off with:

> kata.disable\_contact = true

