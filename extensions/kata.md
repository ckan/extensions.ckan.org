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


Kata is a CKAN extension for handling metadata of research datasets. It is used in [Etsin research data finder](https://etsin.avointiede.fi/en/).

Installation
============

You can install the extension with:

`pip install -e git://github.com/kata-csc/ckanext-kata.git#egg=ckanext-kata`

Requirements
============

* CKAN 2.4.1
* Some additional Python packages that will be installed using `pip install`
* CKAN extension ckanext-ytp-comments: https://github.com/kata-csc/ckanext-ytp-comments/tree/etsin
* ClamAV (if kata.storage.malware_scan=true): http://www.clamav.net/index.html

Configuration
=============

Put the following lines under [app:main] in CKAN configuration file

> kata.storage.malware_scan = true

> kata.is_backup = false

If Google Analytics is on, add

> kata.ga_id = [GA ID]

If LDAP is used, add basic LDAP configuration to the aforementioned file:

> kata.ldap.enabled = true

> kata.ldap.password = [LDAP PASSWORD]

> kata.ldap.server = [LDAP SERVER]

> kata.ldap.dn = [DN]

> kata.ldap.basedn = [BASE DN]

For contact emails following settings apply:

> kata.bf = [ENCRYPTION KEY]

To enable reCaptcha set:

> kata.contact_captcha = true

Note that this setting requires captcha keys to be set

The email feature can be turned off with:

> kata.disable_contact = true

