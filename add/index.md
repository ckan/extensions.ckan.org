---
layout: default
title: Add or Update an Extension
---

# Add or Update an Extension

## Add an Extension

To have an extension added to the registry:

[master]: {{site.extension_list_gdoc}}
[issues]: https://github.com/ckan/extensions.ckan.org/issues
[new]: https://github.com/ckan/extensions.ckan.org/issues/new

* Collect the following pieces of information:
  * Extension URL: URL to github repository for your extension (or URL to your repo if not in github)
  * Extension Author(s): e.g. John Doe or UK Government
  * Compatibility: CKAN Versions your extension is compatible with
  * Title: Short, descriptive title for your extensions e.g. "Disqus Comments per Dataset"
  * Name (Unique): Short url-usable unique name - usually this will be whatever is after ckanext- in your extension name on github e.g. `disqus` in `ckanext-disqus`
    * The name must be different from all other displayed extensions
* [Open an issue on the Extensions issue tracker][new] with title "Add Extension {Name of Your Extension}"

What we will then do:

* Add your extension to the [spreadsheet master list of extensions][master].
* Review your extension for quality
  * Is it reasonably documented?
  * Does it provide a generic feature or is it site specific?
* Assuming it passed the quality check it will be marked for inclusion in the public site here
* We will automatically collect information on your extension and store it here for display. Information includes:
  * README
    * README should be in markdown format preferably (plain text and restructured text accepted but discouraged)
    * README should start with a simple introductory paragraph (**not** a heading)
    * README should include install instructions (even if just `pip install ckanext-{name}`)
  * Recent activity on your extension
  * All of the information submitted in the original issue

#### For Extension Site Administrators

For your instructions see the [README][readme].

[readme]: {{site.github}}

## Update an Extension

* Please [open an issue on the Extensions issue tracker][new] with title like "Update Extension {Name of Your Extension}"
* Add details of what you want updated

