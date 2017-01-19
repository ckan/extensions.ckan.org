---
layout: extension
name: intro
title: A quick interactive introduction to writing CKAN extensions
author: CKAN
homepage: https://github.com/ckan/ckanext-intro
github_user: ckan
github_repo: ckanext-intro
category: Extension
featured: 
permalink: /extension/intro/
---


ckanext-intro - A quick interactive introduction to writing CKAN extensions
===========================================================================

This is a sample extension, intended as a quick and interactive introduction to writing CKAN extensions. It was used in the CKAN workshop at OKCon 2013.

This does not go into as much details as the proper tutorials for writing extensions. Developers willing to start writing CKAN extensions should use those as they are they provide all necessary detail:

-   Writing extensions tutorial:

    > <http://docs.ckan.org/en/latest/extensions/tutorial.html>

-   Custom theming tutorial:

    > <http://docs.ckan.org/en/latest/extensions/theming.html>
    >
    > This is a work in progress, in the meantime provisional docs can be found here:
    >
    > > <http://docs.ckan.org/en/847-new-theming-docs/theming.html>

-   Example IDatasetForm:

    > <https://github.com/okfn/ckan/tree/master/ckanext/example_idatasetform>

Requisites
==========

-   A running source CKAN 2.1 install (<http://docs.ckan.org/en/latest/install-from-source.html>)
-   A sysadmin user
-   Some datasets created

Both last operations are described in <http://docs.ckan.org/en/latest/getting-started.html>

Installation
============

Install the extension as usual, in you activated virtualenv:

    pip install -e git+https://github.com/okfn/ckanext-intro.git#egg=ckanext-intro

If you want to jump straight away to the end result, just add the plugin to your CKAN configuration file:

    ckan.plugins = intro_plugin

It is recommended though that you follow the individual steps as described in the next section.

How it works
============

The repository contains a step-by-step process of building an extension. Each step is contained in a single commit, and flagged with a git tag (`step1`, `step2`, ...)

You can move between steps using the `git checkout` command. For example to start on the first step:

    git checkout step1

To move to the next step:

    git checkout step2

And so on. Once on a particular step, you can see the description of the whole step and the files changed using the `git show` command.

You can also browse the steps on GitHub:

<https://github.com/okfn/ckanext-intro/commits>

