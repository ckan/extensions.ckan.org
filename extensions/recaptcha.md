---
layout: extension
name: recaptcha
title: Correct the bug for the missing recaptcha widget at registration
author: Hoedic
homepage: https://github.com/Hoedic/ckanext-recaptcha
github_user: Hoedic
github_repo: ckanext-recaptcha
category: Extension
featured: 
permalink: /extension/recaptcha/
---


Since CKAN 2.0, the Recaptcha widget for registration does not appear anymore.

This extension, when activated will re-enable it.

In order to work:

-   git clone <https://github.com/Hoedic/ckanext-recaptcha.git>
-   In your .ini file, add the plugin: ckan.plugins =... recaptcha
-   Add your private and public key: ckan.recaptcha.publickey and ckan.recaptcha.privatekey

You're done (the recaptcha widget might need some CSS improvements however)

