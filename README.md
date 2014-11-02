CKAN Extensions registry and website.

## How it Works

* [Extension Master List][master] - maintained in Google Spreadsheet
  * name (id), title, url plus editorial information (show, featured etc) for all extensions we know about
* Metadata plus README for each extension is stored into `extensions/{extension-id}.md
  * Metadata attributes stored in frontmatter and README into the body
  * What extensions we store is driven by the master list (we download all extensions with show column = 1)
  * Script to do this is `scripts/generate.py`

[master]: https://docs.google.com/a/okfn.org/spreadsheets/d/1izCpljO6Et7zLUKcUlB4BzsMZTurENp56Iqi9kXOtgs/edit#gid=0

## Managing Updates and Buiding the Site

1. Add extension information to the [master list][master] (whether we plan to show the extension or not).

2. Then set show column value to 1 to have the extension included in the public extension registry.

3. Generate the local page for the extension or extensions using the `generate.py` script:

    (Re)-generate just one extension page:

    ```
    python scripts/generate.py {name-of-extension}
    ```

    (Re)-Generate pages for all extensions:

    ```
    python scripts/generate.py
    ```

## License

Copyright Open Knowledge (2014-) and licensed under the MIT License.


----

# Thoughts

## What do we include (?)


* Classic CKAN Extensions
* Apps (that build on the CKAN API)
* Tools (?) - e.g. something for managing CKAN better

