---
layout: extension
name: shibboleth
title: Shibboleth authentication plugin for CKAN
author: Harri Palojärvi
homepage: https://github.com/harripal/ckanext-shibboleth
github_user: harripal
github_repo: ckanext-shibboleth
category: Extension
featured: 
permalink: /extension/shibboleth/
---


ckanext-shibboleth
==================

Shibboleth identification plugin for CKAN. Uses repoze.who.openid plugin for authentication.

Install
-------
	pip install -e git+git://github.com/harripal/ckanext-shibboleth.git#egg=ckanext-shibboleth
	
Nosetests
---------
	$ python setup.py nosetests
	
Plugin configuration
--------------------
pyenv/src/ckan/development.ini:

	...
	ckan.plugins = shibboleth
	...

pyenv/src/ckan/who.ini:

	[plugin:shibboleth]
	use = ckanext.repoze.who.shibboleth.plugin:make_identification_plugin
	session = Shib-Session-ID
	mail = mail
	name = cn

	[general]
	request_classifier = repoze.who.classifiers:default_request_classifier
	challenge_decider = repoze.who.plugins.openid.classifiers:openid_challenge_decider

	[identifiers]
	plugins =
		shibboleth
		friendlyform;browser
		openid
		auth_tkt

	[authenticators]
	plugins = 
		ckan.lib.authenticator:OpenIDAuthenticator
		ckan.lib.authenticator:UsernamePasswordAuthenticator

	[challengers]
	plugins =
		openid
		friendlyform;browser

shibboleth sp
-------------
If you can login to IdP but CKAN is not logging you in, try removing REMOTE_USER from 
ApplicationDefaults in /etc/shibboleth/shibboleth2.xml, this should work:

	<ApplicationDefaults entityID="https://sp.mydomain.com/shibboleth">



