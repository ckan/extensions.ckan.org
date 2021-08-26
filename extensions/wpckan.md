---
layout: extension
name: wpckan
title: Wordpress CKAN Plugin
author: Alex Corbi
homepage: https://github.com/OpenDevelopmentMekong/wpckan
github_user: OpenDevelopmentMekong
github_repo: wpckan
category: Extension
featured: 
permalink: /extension/wpckan/
---


wp-ckan
=======

A wordpress plugin for integrating CKAN
<a href="http://ckan.org/" class="uri">http://ckan.org/</a> and WP
<a href="http://wordpress.org/" class="uri">http://wordpress.org/</a>.

Description
===========

wpckan is a wordpress plugin that exposes a series of functionalities to
bring content stored in CKAN to Wordpress' UI and also provide
mechanisms for archiving content generated on Wordpress into a CKAN
instance.

Features
========

Feature 1: Add related CKAN datasets to posts.
----------------------------------------------

Plugin presents a metabox while users are editing posts with an
autocompletion input field that allows the user to add related CKAN
datasets. Suggestions for related datasets and its metadata (title,
description, and resources) are shown to the user while typing in the
input field. Users can add a certain number of datasets that will get
stored along the post's metadata.

In order to use this information, this plugin exposes the
**\[wpckan\_related\_datasets\]** shortcode for embedding information
about related datasets on the content of the post. The shortcode has
following parameters:

-   **group**: (Optional) Specify the id (Not title or name) of a group
    available on the target CKAN instance in order to filter the related
    datasets to ONLY those assigned to it.

-   **organization**: (Optional) Specify the id (Not title or name) of
    an organization available on the target CKAN instance in order to
    filter the related datasets to ONLY those assigned to it.

Note: If both **group** and **organization** parameters are specified
then the dataset has to be asssigned to both in order to be returned by
the shortcode.

-   **include\_fields\_dataset**: (Optional) Comma-separated string. Per
    default, this shortcode shows only title and notes of the CKAN
    dataset (See
    <a href="http://demo.ckan.org/api/3/action/package_search?q=spending" class="uri">http://demo.ckan.org/api/3/action/package_search?q=spending</a>).
    A list of attributes can be specified to present more information.
    Possible values: "title", "notes", "url", "license\_id",
    "license\_url" "metadata\_created", "metadata\_modified", "author" ,
    "author\_email"

-   **include\_fields\_resources**: (Optional) Comma-separated string.
    Per default, this shortcode shows only name, description and format
    of the resources (See
    <a href="http://demo.ckan.org/api/3/action/package_search?q=spending" class="uri">http://demo.ckan.org/api/3/action/package_search?q=spending</a>).
    A list of attributes can be specified to present more information.
    Possible values: "name", "description", "revision\_timestamp",
    "format", "created"

-   **include\_fields\_extra**: (Optional) Comma-separated string. This
    shortcode outputs extra metadatafields. A list of attributes can
    specified to present more Information.

-   **limit**: (Optional) Number. Default is 10. Limits the amount of
    datasets shown by the shortcode string.

-   **filter**: (Optional) Number. Filters the datasets according to
    following criteria:
    -   '0' (ALL): Return all datasets (Default)
    -   '1' (ONLY WITH RESOURCES): Return only datasets featuring at
        least one resource.
-   **filter\_fields**: (Optional) JSON. Filters the datasets according
    to the content of the datasets' extra fields. The list of fields and
    values is specified as JSON string. The name of the fields must
    match exactly (case unsensitive) but for the value the php strpos()
    function will be employed. The OR operator will be applied if more
    than 1 key/value combination are given. See examples below.

-   **sort**: (Optional) String. As per the solr documentation, this is
    a comma-separated string of field names and sort-orderings.

-   **template**: (Optional) String. Render the information using
    different templates:
    -   dataset-list
    -   dataset-grid

#### Pagination

-   **page**: (Optional) Number. When used together with **limit**,
    returned datasets will get paginated. In case of possible
    pagination, this parameter specifies which page is returned. If
    there are not enough related datasets to paginate, this parameter
    will be ignored. Example: if there are 8 related datasets, limit =
    2, page = 2, then datasets 2 and 3 will be returned. Mind that order
    begins on 1.

-   **prev\_page\_link**: (Optional) String. If provided, and as long
    **limit** and **page** are also given parameters, shows a link to
    this URL. The default text is "Previous"

-   **prev\_page\_title**: (Optional) String. Replaces "Previous"
    (Standard text) with the specified text.

-   **next\_page\_link**: (Optional) String. If provided, and as long
    **limit** and **page** are also given parameters, shows a link to
    this URL. The default text is "Next"

-   **next\_page\_title**: (Optional) String. Replaces "Next" (Standard
    text) with the specified text.

Advanced
--------

-   **blank\_on\_empty**: (Optional) Boolean. Returns an empty string ""
    if no datasets have been found to return

Examples:

``` php
[wpckan_related_datasets]
[wpckan_related_datasets limit="3"]
[wpckan_related_datasets organization="d9722d77-3b91-4c26-9172-950a9a4be07a"]
[wpckan_related_datasets limit="3" page="2"]
[wpckan_related_datasets limit="3" page="2" prev_page_link="http://test?prev_page" next_page_link="http://test?next_page"]
[wpckan_related_datasets include_fields_dataset="title,description,author"]
[wpckan_related_datasets include_fields_dataset="title,description,author" include_fields_resources="name,description,created"]
[wpckan_related_datasets limit="3" filter_fields='{"spatial-text":"England","date":"2015"}']
[wpckan_related_datasets blank_on_empty="true"]
[wpckan_related_datasets type="library_record"]
[wpckan_related_datasets sort="metadata_modified+desc"]
```

An example showing how the information returned by this shortcode will
be structured:

``` html
<div class="wpckan_dataset_list">
  <ul>
    <li>
      <div class="wpckan_dataset">
        <div class="wpckan_dataset_title"><a href="http://link_to_dataset">Title</a></div>
        <div class="wpckan_dataset_notes">Notes</div>
        <div class="wpckan_dataset_license">License</div>
        <div class="wpckan_dataset_author">Author</div>
        /*.... other fields ....*/
        <div class="wpckan_resources_list">
          <ul>
            <li>
              <div class="wpckan_resource">
                <div class="wpckan_resource_name"><a href="http://link_to_resource">Name</a></div>
                <div class="wpckan_resource_description">Description</div>
                /*.... other fields ....*/
              </div>
            </li>
            /*.... other resources ....*/
          </ul>
        </div>
      </div>
    </li>
    /*.... other dataset <li> ....*/
  </ul>
</div>
<div class="wpckan_dataset_list_pagination">
  <a href="#">Previous</a>
  <a href="#">Next</a>
</div>
```

Also, the plugin exposes the
**\[wpckan\_number\_of\_related\_datasets\]** shortcode for returning
the number of related datasets assigned to the post as a customizable
link so a summary can be presented on the wordpress side. The shortcode
has the same argument as the shortcode above, and also following
additional parameters:

-   **link\_url**: (Optional) Specify the URL to link the produced
    output with some other resource (i.e: in the CKAN instance)

-   **prefix**: (Optional) Prepends a string before the number.

-   **suffix**: (Optional) Appends a string after the number.

Examples:

``` php
[wpckan_number_of_related_datasets]
[wpckan_number_of_related_datasets link_url="http://link_to_more"]
[wpckan_number_of_related_datasets group="news"]
[wpckan_number_of_related_datasets group="news" limit="1"]
[wpckan_number_of_related_datasets group="news" suffix=" datasets found in the news."]
[wpckan_number_of_related_datasets group="news" prefix="Number of datasets: (" suffix=")" link_url="http://link_to_more"]
[wpckan_number_of_related_datasets organization="d9722d77-3b91-4c26-9172-950a9a4be07a"]
[wpckan_number_of_related_datasets limit="3" filter_fields='{"spatial-text":"England","date":"2015"}']
[wpckan_number_of_related_datasets limit="3" type="dataset"]
[wpckan_number_of_related_datasets blank_on_empty="true"]
[wpckan_number_of_related_datasets type="library_record"]
```

An example (corresponding to the last example above) showing how the
information returned by this shortcode will be structured:

``` html
<div class="wpckan_dataset_number">
  <p><a target="_blank" href="http://link_to_more">Number of datasets: (5)</a></p>
</div>
```

Feature 2: Query lists of CKAN datasets
---------------------------------------

Plugin exposes a function which returns a list of CKAN datasets
resulting after querying CKAN's API. Resulting datasets can be filtered
by organization, group and/or specifying a textual search.

The results of this function can be shown anywhere on a Wordpress
instance (Posts, Pages, etc..) by calling the
**\[wpckan\_query\_datasets query="QUERY"\]** shortcode. Per default,
this shortcode shows only title and description of the dataset. The
shortcode has following parameters:

-   **query**: (Mandatory) Term to query the database.

-   **organization**: (Optional) Filter dataset results by showing only
    those belonging to a certain organization.

-   **group**: (Optional) Filter dataset results by showing only those
    belonging to a certain group.

-   **type**: (Optional) Filter dataset results by showing only those
    belonging to a certain dataset-type.

-   **include\_fields\_dataset**: (Optional) Comma-separated. Per
    default, this shortcode shows only title (with link to the dataset's
    URL) and notes of the CKAN dataset (See
    <a href="http://demo.ckan.org/api/3/action/package_search?q=spending" class="uri">http://demo.ckan.org/api/3/action/package_search?q=spending</a>).
    A list of attributes can be specified to present more information.
    Possible values: "title", "notes", "url", "license", "license\_url"
    "metadata\_created", "metadata\_modified", "author" ,
    "author\_email"

-   **include\_fields\_resources**: (Optional) Comma-separated. Per
    default, this shortcode shows only name (with link to the
    resources's URL), description and format of the resources (See
    <a href="http://demo.ckan.org/api/3/action/package_search?q=spending" class="uri">http://demo.ckan.org/api/3/action/package_search?q=spending</a>).
    A list of attributes can be specified to present more information.
    Possible values: "name", "description", "revision\_timestamp",
    "format", "created"

-   **limit**: (Optional) Number. Default is 10. Limits the amount of
    datasets shown by the shortcode.

-   **filter**: (Optional) Number. Filters the datasets according to
    following criteria:
    -   '0' (ALL): Return all datasets (Default)
    -   '1' (ONLY WITH RESOURCES): Return only datasets featuring at
        least one resource.
-   **filter\_fields**: (Optional) JSON. Filters the datasets according
    to the content of the datasets' extra fields. The list of fields and
    values is specified as JSON string. The name of the fields must
    match exactly (case unsensitive) but for the value the php strpos()
    function will be employed. The OR operator will be applied if more
    than 1 key/value combination are given. See examples below.

-   **sort**: (Optional) String. As per the solr documentation, this is
    a comma-separated string of field names and sort-orderings.

-   **template**: (Optional) String. Render the information using
    different templates:
    -   dataset-list
    -   dataset-grid

#### Pagination

-   **page**: (Optional) Number. When used together with **limit**,
    returned datasets will get paginated. In case of possible
    pagination, this parameter specifies which page is returned. If
    there are not enough related datasets to paginate, this parameter
    will be ignored. Example: if there are 8 related datasets, limit =
    2, page = 2, then datasets 2 and 3 will be returned. Mind that order
    begins on 1.

-   **prev\_page\_link**: (Optional) String. If provided, and as long
    **limit** and **page** are also given parameters, shows a link to
    this URL. The default text is "Previous"

-   **prev\_page\_title**: (Optional) String. Replaces "Previous"
    (Standard text) with the specified text.

-   **next\_page\_link**: (Optional) String. If provided, and as long
    **limit** and **page** are also given parameters, shows a link to
    this URL. The default text is "Next"

-   **next\_page\_title**: (Optional) String. Replaces "Next" (Standard
    text) with the specified text.

Advanced
--------

-   **blank\_on\_empty**: (Optional) Boolean. Returns an empty string ""
    if no datasets have been found to return

Examples:

``` php
[wpckan_query_datasets query="coal"]
[wpckan_query_datasets query="corruption" limit="5"]
[wpckan_query_datasets query="corruption" limit="5" page="1"]
[wpckan_query_datasets organization="d9722d77-3b91-4c26-9172-950a9a4be07a"]
[wpckan_query_datasets query="politics" limit="3" page="2" prev_page_link="http://test?prev_page" next_page_link="http://test?next_page"]
[wpckan_query_datasets query="forestry" organization="odmcambodia" group="news"]
[wpckan_query_datasets query="elections" include_fields_dataset="title,notes,license" include_fields_resources="name,description,created"]
[wpckan_query_datasets limit="3" filter_fields='{"spatial-text":"England","date":"2015"}']
[wpckan_query_datasets query="coal" blank_on_empty="true"]
[wpckan_query_datasets query="*:*" type="library_record"]
[wpckan_query_datasets sort="metadata_modified+desc"]
```

``` html
<div class="wpckan_dataset_list">
  <ul>
    <li>
      <div class="wpckan_dataset">
        <div class="wpckan_dataset_title"><a href="http://link_to_dataset">Title</a></div>
        <div class="wpckan_dataset_notes">Notes</div>
        <div class="wpckan_dataset_license">License</div>
        <div class="wpckan_dataset_author">Author</div>
        /*.... other fields ....*/
        <div class="wpckan_resources_list">
          <ul>
            <li>
              <div class="wpckan_resource">
                <div class="wpckan_resource_name"><a href="http://link_to_resource">Name</a></div>
                <div class="wpckan_resource_description">Description</div>
                /*.... other fields ....*/
              </div>
            </li>
          </ul>
          /*.... other resources ....*/
        </div>
      </div>
    </li>
  /*.... other dataset <li> ....*/
  </ul>
</div>
<div class="wpckan_dataset_list_pagination">
<a href="#">Previous</a>
<a href="#">Next</a>
</div>
```

Also, the plugin exposes the **\[wpckan\_number\_of\_query\_datasets\]**
shortcode for returning the number of queried datasets so a summary can
be presented on the wordpress side. The shortcode has the same argument
as the shortcode above, and also following additional parameters:

-   **link\_url**: (Optional) Specify the URL to link the produced
    output with some other resource (i.e: in the CKAN instance)

-   **prefix**: (Optional) Prepends a string before the number.

-   **suffix**: (Optional) Appends a string after the number.

Examples:

``` php
[wpckan_number_of_query_datasets]
[wpckan_number_of_query_datasets link_url="http://link_to_more"]
[wpckan_number_of_query_datasets group="news"]
[wpckan_number_of_query_datasets group="news" limit="1"]
[wpckan_number_of_query_datasets group="news" suffix=" datasets found in the news."]
[wpckan_number_of_query_datasets group="news" prefix="Number of datasets: (" suffix=")" link_url="http://link_to_more"]
[wpckan_number_of_query_datasets organization="d9722d77-3b91-4c26-9172-950a9a4be07a"]
[wpckan_number_of_query_datasets limit="3" filter_fields='{"spatial-text":"England","date":"2015"}']
[wpckan_number_of_query_datasets limit="3" type='dataset']
[wpckan_number_of_query_datasets blank_on_empty="true"]
[wpckan_number_of_query_datasets type="library_record"]
```

An example (corresponding to the last example above) showing how the
information returned by this shortcode will be structured:

``` html
<div class="wpckan_dataset_number">
  <p><a target="_blank" href="http://link_to_more">Number of datasets: (5)</a></p>
</div>
```

Feature 3: Archiving WP Posts in CKAN
-------------------------------------

The plugin presents a metabox while users are editing posts. It allows
users to specify if the post should be archived as a CKAN dataset. The
plugin polls the CKAN instance and retrieves the list of available
organizations and groups in order for users to be able to determine to
which organization or group the dataset will be assign to. Also, when
that particular post will be archived.

This feature archives the custom fields along with the title and
description. If a valid URL is found in the value of the custom fields,
a new resource will be added to the dataset.

**WARNING** However, custom fields beginning with \*\*\_\*\* or
**wpckan\_** will not be stored.

Feature 4: Show dataset detail
------------------------------

The plugin exposes a shortcode which can be used to output the metadata
and resources of a CKAN dataset, specified by id parameter

-   **id**: String. Unique identifier of the dataset

Examples:

``` php
[wpckan_dataset_detail id="ckan-dataset-one"]
```

``` html
<div class="wpckan_dataset_detail">
    <h1 class="wpckan_dataset_title">title</h1>
    <a href="#" class="wpckan_dataset_owner_org">Organization</a>
    <p class="wpckan_dataset_notes">description</p>
  <ul class="wpckan_dataset_tags">
    <li class="wpckan_dataset_tag"><a href="#">Tag1</a></li>
    <li class="wpckan_dataset_tag"><a href="#">Tag2</a></li>
  </ul>
    <h2>Resources</h2>
    <ul class="wpckan_dataset_resources">
    <li class="wpckan_dataset_resource">
            <img src="#"></img><a href="#">Resource1</a>
        </li>
        <li class="wpckan_dataset_resource">
            <img src="#"></img><a href="#">Resource2</a>
        </li>
  </ul>
    <h2>Additional info</h2>
    <table class="wpckan_dataset_metadata_fields">
    <tr class="wpckan_dataset_metadata_field">
            <td>field name</td>
            <td>field value</td>
        </tr>
  </table>
</div>
<div class="wpckan_dataset_list_pagination">
<a href="#">Previous</a>
<a href="#">Next</a>
</div>
```

widgets
-------

This plugin ships with a series of widgets that basically expose the
functionality of the different shortcodes for easy integration on a
Wordpress site layout:

-   WPCKAN Related Datasets: Shows the information of the related
    datasets of the post or page the widget is integrated in. See
    **/inc/widgets/related-datasets-widget.php**
-   WPCKAN Query Datasets: Shows the results of the specified query. See
    **/inc/widgets/query-resources-widget.php**
-   WPCKAN Query resources by post's category: Shows the results of a
    query made with the specified field as filter and the post's or
    page's categories as values for the query. See
    **/inc/widgets/query-resources-by-category-widget.php**

CORS Support disabled for CKAN &gt;2.3
--------------------------------------

Taken from
<a href="http://docs.ckan.org/en/latest/changelog.html#id1" class="uri">http://docs.ckan.org/en/latest/changelog.html#id1</a>:

> Cross-Origin Resource Sharing (CORS) support is no longer enabled by
> default. Previously, Access-Control-Allow-\* response headers were
> added for all requests, with Access-Control-Allow-Origin set to the
> wildcard value \*. To re-enable CORS, use the new ckan.cors
> configuration settings (ckan.cors.origin\_allow\_all and
> ckan.cors.origin\_whitelist).

So, mind that the CKAN instance which this plugin is used with needs to
allow all origins or whitelist the domain where the wpckan is installed.

Support for ckanext-fluent and qTranslate/qTranslateX
-----------------------------------------------------

For the multilingual functionalities, this plugin relies on two other
components:

-   ckanext-fluent
    (<a href="https://github.com/ckan/ckanext-fluent" class="uri">https://github.com/ckan/ckanext-fluent</a>):
    This CKAN extension provides a way to store and return multilingual
    fields in CKAN datasets, resources, organizations and groups.

-   qTranslate/qTranslateX
    (<a href="https://github.com/qTranslate-Team/qtranslate-x" class="uri">https://github.com/qTranslate-Team/qtranslate-x</a>):
    This plugin offers a way to maintain dynamic multilingual content on
    a WordPress site.

If you are using both in your Wordpress/CKAN stack, WPCKAN will
automatically present localized information on its different templates,
if available. Otherwise, it falls back to English.

Installation
============

1.  Either download the files as zip or clone <code>git clone
    <a href="https://github.com/OpenDevelopmentMekong/wpckan.git" class="uri">https://github.com/OpenDevelopmentMekong/wpckan.git</a></code>
    into the Wordpress plugins folder.
2.  Install dependencies with composer
    (<a href="http://getcomposer.org" class="uri">http://getcomposer.org</a>)
    <code>composer install</code>
3.  Activate the plugin through the 'Plugins' menu in WordPress

Development
===========

1.  Install composer
    <a href="http://getcomposer.org/" class="uri">http://getcomposer.org/</a>
2.  Edit composer.json for adding/modifying dependencies versions
3.  Install dependencies <code>composer install</code>

Requirements
============

-   PHP 5 &gt;= 5.2.0
-   PHP Curl extension (in ubuntu sudo apt-get install php5-curl)

Uses
====

-   Analog logger
    <a href="https://github.com/jbroadway/analog" class="uri">https://github.com/jbroadway/analog</a>
-   Silex CKAN PHP Client
    <a href="https://github.com/SilexConsulting/CKAN_PHP" class="uri">https://github.com/SilexConsulting/CKAN_PHP</a>
-   Twitter's typeahead
    <a href="https://github.com/twitter/typeahead.js/" class="uri">https://github.com/twitter/typeahead.js/</a>

Testing
=======

Tests are found on /tests and can be run with `phpunit tests`

Continuous deployment
=====================

Everytime code is pushed to the repository, travis will run the tests
available on **/tests**. In case the code has been pushed to **master**
branch and tests pass, the \*\*\_ci/deploy.sh\*\* script will be called
for deploying code in CKAN's DEV instance. Analog to this, and when code
from **master** branch has been **tagged as release**, travis will
deploy to CKAN's PROD instance automatically.

For the automatic deployment, the scripts on \*\*\_ci/\*\* are
responsible of downloading the odm-automation repository, decrypting the
**odm\_tech\_rsa.enc** private key file ( encrypted using Travis-ci
encryption mechanism) and triggering deployment in either DEV or PROD
environment.

Copyright and License
=====================

This material is copyright (c) 2014-2015 East-West Management Institute,
Inc. (EWMI).

It is open and licensed under the GNU General Public License (GPL) v3.0
whose full text may be found at:

<a href="http://www.fsf.org/licensing/licenses/gpl-3.0.html" class="uri">http://www.fsf.org/licensing/licenses/gpl-3.0.html</a>

