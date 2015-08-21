---
layout: extension
name: repeating
title: Repeating metadata fields (validators, template snippets and ckanext-scheming support)
author: open.canada.ca
homepage: https://github.com/open-data/ckanext-repeating
github_user: open-data
github_repo: ckanext-repeating
category: Extension
featured: 1
permalink: /extension/repeating/
---


ckanext-repeating
=================

This extension provides a way to store repeating
fields in CKAN datasets, resources, organizations and groups.

Add the `repeating` plugin to your ckan.plugins configuration
settings and use ckanext-scheming or a custom form plugin to
use the provided validators to store repeating values in
metadata fields.

The easiest way to use repeating fields is with
[ckanext-scheming](https://github.com/open-data/ckanext-scheming/).
Add `ckanext.repeating:presets.json` to your scheming.presets
configuration settings:

```json
scheming.presets = ckanext.scheming:presets.json
                   ckanext.repeating:presets.json
```
A repeating field in a scheming schema
will look something like:

```json
{
  "field_name": "authors",
  "preset": "repeating_text",
  "label": "Author",
  "form_blanks": 3
}
```

This new extra field "authors" will appear as multiple fields in the
dataset form, with three blank values below existing values.
by the [form snippet](ckanext/repeating/templates/scheming/form_snippets/repeating_text.html).

![Example of repeating form snippet](docs/repeating-form.png)

When displayed, each value for the text entered will appear separately
by the
[display snippet](ckanext/repeating/templates/scheming/display_snippets/repeating_text.html), eg.:

![Example of repeating display snippet](docs/repeating-display.png)

When the dataset is accessed from the API each value will appear
and are updated as items in a list, eg.:

```json
{
  "...": "...",
  "authors": [
    "Person One",
    "Person Two"
  ],
  "...": "..."
}

