---
layout: extension
name: ckanext-feedcontent
title: Allows for content from rss/atom feeds to be inserted into pages.
author: Open Knowledge
homepage: https://github.com/okfn/ckanext-feedcontent
github_user: okfn
github_repo: ckanext-feedcontent
category: Extension
featured: 
permalink: /extension/ckanext-feedcontent/
---


# Feed Extension

The Feed extension allows site administrators to include blog entries in the main content of templates using named
references to atom or rss feeds.

**Note: This extension requires ckan 1.7 or higher**

## Activating and Installing

To install the plugin, enter your virtualenv and load the source::

 (pyenv)$ git install -e hg+https://github.com/okfn/ckanext-feedcontent#egg=ckanext-feedcontent

This will also register a plugin entry point, so you now should be
able to add the following to your CKAN .ini file::

 ckan.plugins = feed_content <other-plugins>

**At this point nothing will have happened**! To add feeds to your system see below.

## Running the tests

You can run the tests from the root of this repository with the following command

```
nosetests --ckan --with-pylons=test-core.ini ckanext/feedcontent/tests/
```

## Using the Extension

### Adding feeds

To add feeds to CKAN you should log on as a system administrator and then visit /feed/ from where you will be able to add a new feed or edit an existing one.  When you need to update a feed you should visit /feed/ from where you will be able to view the feed to be updated and then press the update button.

### Setting up the example

Go to the url of your CKAN instance, and go to /feed/ where you should add a new feed with a title of 'ckan' (without the quotes), a url of 'http://ckan.org/feed' and tick the HTML Entries checkbox.

Add the following line to your configuration

```
ckan.feed.demo = yes
```

Point your browser to the home page of your CKAN instance.  This simple example shows in ckanext/feedcontent/templates/example/home.html how the feed items can be included.


### Using feeds

To reference a feed and add an entry in a template you should use the feed_entry helper and provide it both the name of the feed (name, not title, is the one shown in the URL as a slug) and a regular expression for the title it should match.

In the following example it fetches (and renders) the entry which ends with 'watch the data'.

```
${h.feed_entry("ckan", ".*watch the data$")}
```

As feeds do not auto-update, if you wish to update the feed you should do so using the option on the /feed/ page or the individual view page, for example /feed/ckan (if you had following the example setup steps above).

### Configuring snippets for presentation

When using feed entries within a template, it is necessary to specify how the entry will be rendered.  By default this uses a simple template within ckanext\feedcontent\templates but the default can be overridden by setting the 'ckan.feeds.default.snippet' setting to point to a template within the configured template paths.

As feeds are created they can also have the template file specified as long as the template can be found in the template path.

The template path itself can be added to using the config option called 'extra_template_paths', see the docs for more information but it could be configured as follows assuming a feeditem.html in /var/ckan/extras.

```
extra_template_paths = /var/ckan/extras
ckan.feed.default.snippet = feeditem.html
```

The only other configuration option is the 'ckan.feeds.short_description.size' setting which will allow the user to set the size of a new short_description field that is passed through to the template.  By default this is 200 characters.



