---
layout: extension
name: s3-resources
title: Upload resources to AWS S3
author: data.gov.sg
homepage: https://github.com/datagovsg/ckanext-s3-resources
github_user: datagovsg
github_repo: ckanext-s3-resources
category: Extension
featured: 
permalink: /extension/s3-resources/
---


CKAN Extension to upload resources to AWS S3
============================================

This extension can be used to upload your CKAN resources to AWS S3
instead of the CKAN server. You can blacklist certain resource types
(e.g. APIs) from being uploaded to S3. A paster command is provided to
migrate resources to S3.

Requirements
------------

-   `boto3` - for connecting to S3

Setup/Configuration
-------------------

For the extension to work, you need to ensure that the following
configuration options have been set in your configuration file `*.ini`:

-   `ckan.datagovsg_s3_resources.s3_aws_access_key_id` - AWS access key
    ID. Obtained from AWS.
-   `ckan.datagovsg_s3_resources.s3_aws_secret_access_key` - AWS secret
    access key ID. Obtained from AWS.
-   `ckan.datagovsg_s3_resources.s3_bucket_name` - The name of the
    bucket on S3 to upload the resources to.
-   `ckan.datagovsg_s3_resources.s3_url_prefix` - Base URL
    (<a href="https://s3.data.gov.sg" class="uri">https://s3.data.gov.sg</a>)
    -   Resource URLs will be in the form of
        `<base_url><package_name>/<resource_filename>`
        -   e.g. `https://s3.data.gov.sg/package-123/resource-123.csv`
    -   Package zip URLs will be in the form of
        `<base_url><package_name>/<package_name>.zip`
        -   e.g. `https://s3.data.gov.sg/package-123/package-123.csv`
    -   e.g.
        `ckan.datagovsg_s3_resources.s3_url_prefix = https://bucket-name.s3.amazonaws.com/`
-   `ckan.datagovsg_s3_resources.upload_filetype_blacklist` (optional) -
    A space separated list of file formats to ignore.
    -   e.g.
        `ckan.datagovsg_s3_resources.upload_filetype_blacklist = csv pdf xls`
-   `ckan.datagovsg_s3_resources.s3_aws_region_name` (optional) -
    Specify which AWS region to use.
    -   e.g. `ap-southeast-1`

Migration
---------

The extension includes a paster command to help migrate the existing
resources to S3. The command can be run by doing:

`paster --plugin=plugin_name migrate_s3`

