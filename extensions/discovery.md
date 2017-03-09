---
layout: extension
name: discovery
title: Improved searching and browsing
author: City of Karlsruhe, Germany
homepage: https://github.com/stadt-karlsruhe/ckanext-discovery
github_user: stadt-karlsruhe
github_repo: ckanext-discovery
category: Extension
featured: 
permalink: /extension/discovery/
---


ckanext-discovery
=================

*A CKAN extension to help people discover your datasets*

[![image](https://travis-ci.org/stadt-karlsruhe/ckanext-discovery.svg?branch=master)](https://travis-ci.org/stadt-karlsruhe/ckanext-discovery)

[![image](https://coveralls.io/repos/stadt-karlsruhe/ckanext-discovery/badge.svg)](https://coveralls.io/r/stadt-karlsruhe/ckanext-discovery)

Open data can only be used for awesome things if it is found. [CKAN](http://ckan.org) has powerful built-in search tools, but for users who don't know (yet) what exactly they are looking for there is room for improvement.

This extension provides multiple plugins that make it easier for your users to discover your data:

-   [search\_suggestions](): Provides real-time search suggestions in a drop-down box
-   [similar\_datasets](): Adds a list of similar datasets to the dataset detail view
-   [solr\_query\_config](): Allows you to easily override the parameters that CKAN passes to Solr
-   [tag\_cloud](): Replaces the list of frequent tags on the home page with a tag cloud that shows the most popular tags scaled according to their popularity

Installation
------------

*ckanext-discovery* has been developed and tested with CKAN 2.6. Other versions may or may not work, any feedback in that regard is very welcome.

First activate your CKAN virtualenv:

    . /usr/lib/ckan/default/bin/activate

Then install the latest version of *ckanext-discovery*:

    pip install -e git+https://github.com/stadt-karlsruhe/ckanext-discovery#egg=ckanext-discovery

The extension is now installed. However, *you still need to install and configure those of its plugins that you want to use*. See the documentations of the individual plugins below for more information.

Plugins
-------

### `discovery`

This plugin doesn't provide any direct functionallity on its own but contains shared utilities required by some of the other plugins.

### `search_suggestions`

This plugin provides real-time search suggestions while the user is entering text into a search field:

![Screenshot of the search\_suggestions plugin](doc/search_suggestions.png)

#### Installation

First add `discovery` and `search_suggestions` to the list of plugins in CKAN's [configuration INI](http://docs.ckan.org/en/latest/maintaining/configuration.html#ckan-configuration-file):

    plugins = ... discovery search_suggestions

Then create the necessary database tables:

    . /usr/lib/ckan/default/bin/activate
    paster --plugin=ckanext-discovery search_suggestions init -c /etc/ckan/default/production.ini

Finally, restart CKAN:

    sudo service apache2 restart

#### Usage

The suggestions are generated from previous searches by other users. The plugin therefore combines two functionalities:

1.  Automatic collection of statistics about the users' search queries
2.  Generation and display of search suggestions

Regarding the first point it is important to point out that search queries are stored in a post-processed form and without any reference to the corresponding user.

Search suggestions are automatically enabled on all search fields that CKAN provides in its base templates, namely the search box on the home page, the search field in the header, and the search box at `/dataset`. In addition, any HTML element with the class `search` will also automatically display search suggestions.

Obviously suggestions are only provided once some search queries have been recorded.

#### Configuration

The plugin offers multiple settings that can be configured via CKAN's [configuration INI](http://docs.ckan.org/en/latest/maintaining/configuration.html#ckan-configuration-file):

    # Maximum number of search suggestions to display in the drop-down
    # box. Defaults to 4. Note that fewer suggestions may be listed if not
    # enough related queries have been stored before.
    ckanext.discovery.search_suggestions.limit = 4

    # Whether data about search queries should be stored. Defaults to true.
    ckanext.discovery.search_suggestions.store_queries = True

    # Whether search suggestions should be displayed. Defaults to true.
    ckanext.discovery.search_suggestions.provide_suggestions = True

#### Filtering and Preprocessing Search Terms

To achieve good suggestions, search terms entered by the user must be preprocessed, for example by converting them to lower-case. Most of this is done automatically by the plugin. However, there's also the possibility to perform additional custom preprocessing and filtering steps. This is useful, for example, to filter out stop words in your target language (the plugin doesn't do stop word filter at all) or to ignore unwelcome content. The latter is particularly important since search terms entered by one user may end up in the suggestions provided to other users.

To implement your own search term filter and preprocessor, simply implement the `ISearchTermPreprocessor` interface, which contains a single method, `preprocess_search_term`:

    import ckan.plugins as plugins
    from ckanext.discovery.plugins.search_suggestions.interfaces import \
        ISearchTermPreprocessor

    STOP_WORDS = {'and', 'not', 'or'}

    # We don't want people to talk about dogs here!
    BAD_WORDS = {'dog', 'puppy'}

    REJECT_WORDS = STOP_WORDS.union(BAD_WORDS)

    class MyPlugin(plugins.SingletonPlugin):
        plugins.implements(ISearchTermPreprocessor)

        def preprocess_search_term(self, term):
            '''
            Preprocess and filter a search term.

            ``term`` is a search term extracted from a user's search query.

            If this method returns a false value then the term is ignored
            w.r.t. search suggestions. This is useful for filtering stop
            words and unwelcome content.

            Otherwise the return value of the method is used instead of the
            original search term. In most cases you simply return the value
            unchanged.

            Note that all of this only affects the generation of the search
            suggestions but not the search itself.
            '''
            if term in REJECT_WORDS:
                # Ignore this term
                return False

            # Go ahead and use term to calculate search suggestions
            return term

After adding, removing or changing an `ISearchTermPreprocessor` implementation you need to reprocess the previously stored search terms:

    . /usr/lib/ckan/default/bin/activate
    paster --plugin=ckanext-discovery search_suggestions reprocess -c /etc/ckan/default/production.ini

To show all currently stored search terms, use the `list` command:

    . /usr/lib/ckan/default/bin/activate
    paster --plugin=ckanext-discovery search_suggestions list -c /etc/ckan/default/production.ini

### `similar_datasets`

This plugin displays a list of similar datasets in the sidebar of the dataset view:

![Screenshot of the similar\_datasets plugin](doc/similar_datasets.png)

#### Installation

The plugin relies on Solr's [More Like This](https://cwiki.apache.org/confluence/display/solr/MoreLikeThis) feature and requires that you configure your Solr instance appropriately. In particular, you need to set up a [MoreLikeThisHandler](https://cwiki.apache.org/confluence/display/solr/MoreLikeThis#MoreLikeThis-ParametersfortheMoreLikeThisHandler) in your `/etc/solr/conf/solrconfig.xml`. To do this, add the following code block directly before the `</config>` tag at the end of the file:

    <requestHandler name="/mlt" class="solr.MoreLikeThisHandler">
        <lst name="defaults">
            <int name="mlt.mintf">3</int>
            <int name="mlt.mindf">1</int>
            <int name="mlt.minwl">3</int>
        </lst>
    </requestHandler>

Please refer to the documentation of the [MoreLikeThisHandler](https://cwiki.apache.org/confluence/display/solr/MoreLikeThis#MoreLikeThis-ParametersfortheMoreLikeThisHandler) for details on its configuration.

In addition, you need to enable [term vector storage](https://cwiki.apache.org/confluence/display/solr/Field+Type+Definitions+and+Properties#FieldTypeDefinitionsandProperties-FieldDefaultProperties) for the `text` field in your `/etc/solr/conf/schema.xml`. To do this, locate the following field definition:

    <field name="text" type="text" indexed="true" stored="false" multiValued="true" />

Then add `termVectors="true"` to the list of attributes so that the full definition looks like this:

    <field name="text" type="text" indexed="true" stored="false" multiValued="true" termVectors="true" />

Please note that term vectors can substantially increase the size of your Solr index.

Once you have updated your `solrconfig.xml` and `schema.xml` files as described above you need to restart Solr. Assuming you're using Jetty, this is done via

    sudo service jetty restart

Finally you need to re-index your datasets once, so that the term vectors of the existing datasets are stored (for datasets that are added or updated in the future this is done automatically):

    . /usr/lib/ckan/default/bin/activate
    paster --plugin=ckan search-index rebuild -c /etc/ckan/default/production.ini

Now add `discovery` and `similar_datasets` to your list of plugins in CKAN's [configuration INI](http://docs.ckan.org/en/latest/maintaining/configuration.html#ckan-configuration-file):

    plugins = ... discovery similar_datasets

After restarting CKAN the list of similar datasets should be displayed on the detailed view of each dataset:

    sudo service apache2 restart

#### Configuration

The plugin offers one setting that can be configured in CKAN's [configuration INI](http://docs.ckan.org/en/latest/maintaining/configuration.html#ckan-configuration-file):

    # Maximum number of similar datasets to list. Defaults to 5. Note that less
    # datasets may be shown if Solr doesn't find enough similar datasets.
    ckanext.discovery.similar_datasets.max_num = 5

### `solr_query_config`

This plugin allows you to set Solr query parameters via entries in CKAN's [configuration INI](http://docs.ckan.org/en/latest/maintaining/configuration.html#ckan-configuration-file). You can either specify a default value for a parameter (which is only used if the parameter isn't already set in the current query) or you can force a parameter to a certain value (overriding it if it is already set).

#### Installation

Simply add `solr_query_config` to the list of plugins in CKAN's [configuration INI](http://docs.ckan.org/en/latest/maintaining/configuration.html#ckan-configuration-file):

    plugins = ... solr_query_config

Then restart CKAN:

    sudo service apache2 restart

#### Configuration

To specify a default value, prefix the parameter name with `ckanext.discovery.solr_query_config.default.`:

    # By default, sort by metadata modification timestamp
    ckanext.discovery.solr.default.sort = metadata_modified asc

Similarly, a value can be forced using the prefix `ckanext.discovery.solr_query_config.force.`:

    # Always use a custom Solr query handler
    ckanext.discovery.solr.force.defType = my_special_query_handler

Note that only those Solr parameters that are accepted by the [package\_search](http://docs.ckan.org/en/latest/api/index.html#ckan.logic.action.get.package_search) API function can be set via this plugin.

### `tag_cloud`

This plugin shows links for the most frequent tags scaled according to their frequency:

![Screenshot of the tag\_cloud plugin](doc/tag_cloud.png)

#### Installation

Simply add `discovery` and `tag_cloud` to the list of plugins in CKAN's [configuration INI](http://docs.ckan.org/en/latest/maintaining/configuration.html#ckan-configuration-file):

    plugins = ... discovery tag_cloud

Then restart CKAN:

    sudo service apache2 restart

#### Usage

The plugin automatically replaces the list of the most frequent tags on CKAN's default front page with a tag cloud.

If you want to use the tag cloud in a different part of the site you can use the following [template snippet](http://docs.ckan.org/en/latest/theming/templates.html#snippets):

    {%raw%}{% {%endraw%}snippet 'ckanext-discovery/snippets/tag_cloud.html', num_tags=10{%raw%} %}{%endraw%}

The `num_tags` specifies the number of tags in the tag cloud. It is optional and defaults to the setting of the `ckanext.discovery.tag_cloud.num_tags` option (see below).

#### Configuration

The plugin offers one setting that can be configured via CKAN's [configuration INI](http://docs.ckan.org/en/latest/maintaining/configuration.html#ckan-configuration-file):

    # Number of tags to show in the tag cloud. Defaults to 20 and can be
    # overriden by passing a ``num_tags`` parameter to the tag cloud template
    # snippet.
    ckanext.discovery.tag_cloud.num_tags = 20

License
-------

Copyright (C) 2017 Stadt Karlsruhe (www.karlsruhe.de)

Distributed un der the GNU Affero General Public License. See the file `LICENSE` for details.

Changes
-------

### 0.1.0

-   First release


