---
layout: extension
name: datesearch
title: A CKAN extension that adds temporal facets (limit dataset search results to between two dates)
author: B2FIND
homepage: https://github.com/B2FIND/ckanext-datesearch
github_user: B2FIND
github_repo: ckanext-datesearch
category: Extension
featured: 
permalink: /extension/datesearch/
---


How to implement a temporal search widget for CKAN
==================================================

CKAN supports date-range searches out of the box. For example, to search for
datasets that were modified in August 2013, you can simply type this into the
search bar:

    metadata_modified:[2013-08-01T00:00:00Z TO 2013-08-31T00:00:00Z]

Here's the result of that search on datahub.io: <http://datahub.io/dataset?q=metadata_modified%3A[2013-08-01T00%3A00%3A00Z+TO+2013-08-31T00%3A00%3A00Z]>.

You can also search for `metadata_created` instead of `metadata_modified`, or
you can search on any custom date fields you've added to datasets. You can do
other kinds of date math besides ranges too, e.g. less than, greater than
(it's just Solr's date query syntax).

So the challenge of integrating date-range searches into your CKAN site is
mostly a user interface problem: how to present a user-friendly way to select
a start date and an end date, and integrate the date-range facet with the rest
of CKAN's search tools such as the query box, sorting, and other facets.

It's not enough just to do a date-range search, the user should be able to
search for datasets in the *climate* group, with an open license, matching the
term "carbon", *and* within a given date-range, and then also sort those
results, and they should be able to do all this in a simple, user-friendly way.


Create extension and plugin
---------------------------

First create a CKAN extension `ckanext-datesearch` containing a plugin
`datesearch`. The plugin doesn't need to do anything yet.
See <http://docs.ckan.org/en/943-writing-extensions-tutorial/writing-extensions.html>.


Add template directory and Fanstatic library
--------------------------------------------

The plugin needs to implement `IConfigurable` and register a template
directory and a Fanstatic library directory with CKAN.
[ckanext/datesearch/plugin.py](ckanext/datesearch/plugin.py):

    import ckan.plugins as plugins
    import ckan.plugins.toolkit as toolkit


    class DateSearchPlugin(plugins.SingletonPlugin):
        plugins.implements(plugins.IConfigurer)

        def update_config(self, config):
            toolkit.add_template_directory(config, 'templates')
            toolkit.add_resource('fanstatic', 'ckanext-datesearch')

Also create the directories
[ckanext/datesearch/templates/](ckanext/datesearch/templates/) and
[ckanext/datesearch/fanstatic/](ckanext/datesearch/fanstatic/).

`templates` is a directory where we can put custom templates that will override
the CKAN core ones.

`fanstatic` is a [Fanstatic](ckanext/datesearch/fanstatic/) resource directory.
CKAN uses Fanstatic to serve static files like CSS, JavaScript or image files,
because Fanstatic provides features like bundling, minifying, caching, etc.


Add static files for the date-range picker widget
-------------------------------------------------

[fanstatic/daterangepicker-bs3.css](ckanext/datesearch/fanstatic/daterangepicker-bs3.css),
[fanstatic/daterangepicker.js](ckanext/datesearch/fanstatic/daterangepicker.js),
and [fanstatic/moment.js](ckanext/datesearch/fanstatic/moment.js)
are some static CSS and JavaScript files that we're
using to get a GUI date-range picker widget. We're using Dan Grossman's
[bootstrap-daterangepicker](https://github.com/dangrossman/bootstrap-daterangepicker).

Adding the files into the `fanstatic` directory in our extension just means
that those files will be available when we need them in our templates later.


Customize the dataset search page template
------------------------------------------

Create the directory [ckanext/datesearch/templates/package/](ckanext/datesearch/templates/package/),
and open the file [ckanext/datesearch/templates/package/search.html](ckanext/datesearch/templates/package/search.html):

    {%raw%}{% {%endraw%}ckan_extends{%raw%} %}{%endraw%}

    {%raw%}{% {%endraw%}block secondary_content{%raw%} %}{%endraw%}
      {%raw%}{% {%endraw%}resource 'ckanext-datesearch/moment.js'{%raw%} %}{%endraw%}
      {%raw%}{% {%endraw%}resource 'ckanext-datesearch/daterangepicker.js'{%raw%} %}{%endraw%}
      {%raw%}{% {%endraw%}resource 'ckanext-datesearch/daterangepicker-bs3.css'{%raw%} %}{%endraw%}
      {%raw%}{% {%endraw%}resource 'ckanext-datesearch/daterangepicker-module.js'{%raw%} %}{%endraw%}

      {# This <section> is the date-range picker widget in the sidebar. #}
      <section class="module module-narrow module-shallow">
        <h2 class="module-heading">
          <i class="icon-medium icon-calendar"></i> {{ _('Filter by date') }}
          <a href="{{ h.remove_url_param(['ext_startdate', 'ext_enddate']) }}"
            class="action">{{ _('Clear') }}</a>
        </h2>
        <div class="module-content input-prepend" data-module="daterange-query">
          <span class="add-on"><i class="icon-calendar"></i></span>
          <input type="text" style="width: 150px" id="daterange"
                 data-module="daterangepicker-module" />
        </div>
      </section>

      {{ super() }}
    {%raw%}{% {%endraw%}endblock{%raw%} %}{%endraw%}

This is a Jinja template that overrides the [templates/package/search.html](https://github.com/okfn/ckan/blob/release-v2.0.2/ckan/templates/package/search.html)
template in CKAN core:

* `{%raw%}{% {%endraw%}ckan_extends{%raw%} %}{%endraw%}` means this template inherits from the corresponding
  core template

* Look in the core template file to see what Jinja blocks are available, in
  this case we're overriding the `{%raw%}{% {%endraw%}block secondary_content{%raw%} %}{%endraw%}`.

* `{%raw%}{% {%endraw%}resource 'ckanext-datesearch/moment.js'{%raw%} %}{%endraw%}` tells Fanstatic to load the
  `moment.js` file from our `fanstatic` directory into this page. We load a
  number of custom resource files in our template:

        {%raw%}{% {%endraw%}resource 'ckanext-datesearch/moment.js'{%raw%} %}{%endraw%}
        {%raw%}{% {%endraw%}resource 'ckanext-datesearch/daterangepicker.js'{%raw%} %}{%endraw%}
        {%raw%}{% {%endraw%}resource 'ckanext-datesearch/daterangepicker-bs3.css'{%raw%} %}{%endraw%}
        {%raw%}{% {%endraw%}resource 'ckanext-datesearch/daterangepicker-module.js'{%raw%} %}{%endraw%}

* `{{ super() }}` means to insert the contents of the block from the core
  template.

* The rest of the stuff inside `{%raw%}{% {%endraw%}block secondary_content{%raw%} %}{%endraw%}` is the custom
  stuff that we're adding to the top of the sidebar. Most of the code is just
  to make it fit into the CKAN theme. The important bit is:

        <input type="text" style="width: 150px" id="daterange"
               data-module="daterangepicker-module" />

  Adding a `data-module="daterangepicker-module"` attribute to an HTML element
  tells CKAN to find the `daterangepicker-module` JavaScript module and load
  it into the page after this element is rendered.


Implement the `daterangepicker-module` JavaScript module
--------------------------------------------------------

CKAN uses _JavaScript modules_ to load snippets of JavaScript into the page.
When we added the `data-module="daterangepicker-module"` attribute to our
`<input>` tag in our template earlier, we told CKAN to include the
`daterangepicker-module` JavaScript module into our page. We now need to
provide that module. [fanstatic/daterangepicker-module.js](ckanext/datesearch/fanstatic/daterangepicker-module.js):

    this.ckan.module('daterangepicker-module', function($, _) {
        return {
            initialize: function() {

                // Add hidden <input> tags #ext_startdate and #ext_enddate,
                // if they don't already exist.
                var form = $("#dataset-search");
                if ($("#ext_startdate").length === 0) {
                    $('<input type="hidden" id="ext_startdate" name="ext_startdate" />').appendTo(form);
                }
                if ($("#ext_enddate").length === 0) {
                    $('<input type="hidden" id="ext_enddate" name="ext_enddate" />').appendTo(form);
                }

                // Add a date-range picker widget to the <input> with id #daterange
                $('input[id="daterange"]').daterangepicker({
                    showDropdowns: true,
                    timePicker: true
                },
                function(start, end) {

                    // Bootstrap-daterangepicker calls this function after the user
                    // picks a start and end date.

                    // Format the start and end dates into strings in a date format
                    // that Solr understands.
                    start = start.format('YYYY-MM-DDTHH:mm:ss') + 'Z';
                    end = end.format('YYYY-MM-DDTHH:mm:ss') + 'Z';

                    // Set the value of the hidden <input id="ext_startdate"> to
                    // the chosen start date.
                    $('#ext_startdate').val(start);

                    // Set the value of the hidden <input id="ext_enddate"> to
                    // the chosen end date.
                    $('#ext_enddate').val(end);

                    // Submit the <form id="dataset-search">.
                    $("#dataset-search").submit();
                });
            }
        }
    });

CKAN will call the `initialize` function when the page loads. This function
uses jQuery and bootstrap-daterangepicker to add a JavaScript date-range picker
widget to the `<input>` tag with `id="daterange"`:

    $('input[id="daterange"]').daterangepicker({
        showDropdowns: true,
        timePicker: true
    },

Finally, bootstrap-daterangepicker supports a *callback function* that will
be called after the user selects two dates. We use the callback function to add
the selected start and end dates to the hidden `<input>` tags, and
submit the form:

    function(start, end) {

        // Bootstrap-daterangepicker calls this function after the user
        // picks a start and end date.

        // Format the start and end dates into strings in a date format
        // that Solr understands.
        start = start.format('YYYY-MM-DDTHH:mm:ss') + 'Z';
        end = end.format('YYYY-MM-DDTHH:mm:ss') + 'Z';

        // Set the value of the hidden <input id="ext_startdate"> to
        // the chosen start date.
        $('#ext_startdate').val(start);

        // Set the value of the hidden <input id="ext_enddate"> to
        // the chosen end date.
        $('#ext_enddate').val(end);

        // Submit the <form id="dataset-search">.
        $("#dataset-search").submit();
    });


Implement `IPackageController` to put the dates into the Solr query
-------------------------------------------------------------------

Finally, when the dataset search form is submitted along with our extra start
and end dates (via the hidden `<input>` tags), we need to catch these start
and end dates and insert them into the Solr query. We can do this by
implementing CKAN's `IPackageController` plugin interface and using its
`before_search()` method to modify the Solr query parameters before the search
is done. In `plugin.py`:

    class DateSearchPlugin(plugins.SingletonPlugin):
        plugins.implements(plugins.IConfigurer)
        plugins.implements(plugins.IPackageController, inherit=True)

        def update_config(self, config):
            toolkit.add_template_directory(config, 'templates')
            toolkit.add_resource('fanstatic', 'ckanext-datesearch')

        def before_search(self, search_params):
            extras = search_params.get('extras')
            if not extras:
                # There are no extras in the search params, so do nothing.
                return search_params
            start_date = extras.get('ext_startdate')
            end_date = extras.get('ext_enddate')
            if not start_date or not end_date:
                # The user didn't select a start and end date, so do nothing.
                return search_params

            # Add a date-range query with the selected start and end dates into the
            # Solr facet queries.
            fq = search_params['fq']
            fq = '{fq} +metadata_modified:[{start_date} TO {end_date}]'.format(
                fq=fq, start_date=start_date, end_date=end_date)
            search_params['fq'] = fq
            return search_params

Our `before_search()` method receives the values from our `#ext_startdate` and
`#ext_enddate` input tags in the `extras` dict of the `search_params` dict.

It's important that the tag IDs begin with `ext_`, this tells CKAN to pass the
values to our plugin.

We simply take these start and end date values and add them to the
[Solr filter query](http://wiki.apache.org/solr/CommonQueryParameters#fq)
(`fq`) in a date-range format that Solr understands:

    # Add a date-range query with the selected start and end dates into the
    # Solr facet queries.
    fq = search_params['fq']
    fq = '{fq} +metadata_modified:[{start_date} TO {end_date}]'.format(
        fq=fq, start_date=start_date, end_date=end_date)
    search_params['fq'] = fq
    return search_params


Todo
----

There's still some work on the details of the user interface to be done here,
including:

* After the user selects a date-range and the page reloads with the filtered
  search results, the date-range should remain filled-in in the date-range
  picker widget.

* If the user types something into the search box and hits return while they
  have a date-range filter on, the date-range filter should not be lost.

