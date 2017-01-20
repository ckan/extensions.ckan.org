---
layout: extension
name: mapviews
title: CKAN Resource View to build maps and choropleth maps
author: CKAN
homepage: https://github.com/ckan/ckanext-mapviews
github_user: ckan
github_repo: ckanext-mapviews
category: Extension
featured: 1
permalink: /extension/mapviews/
---


ckanext-mapviews
================

![Pakistan choropleth map](doc/img/pakistan.png)

This extension adds regular and choropleth maps to CKAN, using the new Resource
View being developed on CKAN's master branch (currently unreleased).

It uses [LeafletJS](http://leafletjs.com), which is compatible with all major
browsers (including IE7+).

Installation
------------

Clone this repository and run `python setup.py install`. Then add
`navigablemap` and/or `choroplethmap` to the list in `ckan.plugins`
in your CKAN config file.

Restart your webserver. You should see the new "Navigable Map" and/or
"Choropleth Map" chart types (depending on which plugins you added to the list)
as options in the view type's list on any resource that's in the DataStore.

Usage
-----

### Pre-requisites

To start creating choropleth maps, you need two things: the data you want to
plot, and a GeoJSON defining the geographical regions you'd like to plot it.
The data itself needs to be in a resource inside the DataStore, and the map
needs to be in the same domain as CKAN itself (to avoid [same-origin
policy](http://en.wikipedia.org/wiki/Same-origin_policy) issues). The easiest
way to do so is to upload the GeoJSON as another resource.

Each GeoJSON feature needs a property related to a column in the data. It can
be an id, name, or anythings that uniquely identifies that feature, so we know
where to plot the data.

### Example

We'll create a map to try to understand the internet usage across the world. To
do so, we need a worldmap in GeoJSON and the internet usage data.

A good source of GeoJSON files is the [Natural Earth
Data](http://naturalearthdata.com/) website. We'll be using their [world map at
1:110 million
scale](https://github.com/nvkelso/natural-earth-vector/blob/master/geojson/ne_110m_admin_0_countries.geojson).

We'll be plotting the [Internet usage per 100
people in 2012](doc/internet-users-per-100-people.csv) all across the world. The data
comes from the great [World Bank's Data
Bank](http://databank.worldbank.org/data/home.aspx). It looks like this:

<table>
<colgroup>
<col width="15%" />
<col width="13%" />
<col width="33%" />
<col width="15%" />
<col width="17%" />
<col width="4%" />
</colgroup>
<thead>
<tr class="header">
<th>Country Name</th>
<th>Country Code</th>
<th>Indicator Name</th>
<th>Indicator Code</th>
<th>2012</th>
<th>...</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Afghanistan</td>
<td>AFG</td>
<td>Internet users (per 100 people)</td>
<td>IT.NET.USER.P2</td>
<td>5.45454545454545</td>
<td>...</td>
</tr>
<tr class="even">
<td>Albania</td>
<td>ALB</td>
<td>Internet users (per 100 people)</td>
<td>IT.NET.USER.P2</td>
<td>54.6559590399494</td>
<td>...</td>
</tr>
<tr class="odd">
<td>Algeria</td>
<td>DZA</td>
<td>Internet users (per 100 people)</td>
<td>IT.NET.USER.P2</td>
<td>15.2280267564417</td>
<td>...</td>
</tr>
<tr class="even">
<td>American Samoa</td>
<td>ASM</td>
<td>Internet users (per 100 people)</td>
<td>IT.NET.USER.P2</td>
<td></td>
<td>...</td>
</tr>
<tr class="odd">
<td>Andorra</td>
<td>ADO</td>
<td>Internet users (per 100 people)</td>
<td>IT.NET.USER.P2</td>
<td>86.4344246167258</td>
<td>...</td>
</tr>
<tr class="even">
<td>...</td>
<td>...</td>
<td>...</td>
<td>...</td>
<td>...</td>
<td>...</td>
</tr>
</tbody>
</table>

To identify each country, we have its name and code. We need to have either
attribute in the GeoJSON feature's properties. Opening that file, we see:

``` javascript
{
  "features": [
    {
      "geometry": {
        "coordinates": [
          // ...
        ],
        "type": "Polygon"
      },
      "properties": {
        "name": "Afghanistan",
        "region_un": "Asia",
        "region_wb": "South Asia",
        "wb_a3": "AFG",
        // ...
      },
      "type": "Feature"
    },
    // ...
  ]
}
```

We can map either `Country Name` with `name`, or `Country Code`
with `wb_a3`. Let's use the country code.

In your CKAN instance, create a new dataset (i.e. "World Bank's Indicators"),
and upload two resources: the GeoJSON and the data file.

Go to the data file's manage resource page and create a new `Choropleth Map` view. You'll see a form with a few fields. Use "Internet usage across
the globe" as a title, leave the description empty (if you want). Now we need
to add the GeoJSON.

Select in the `GeoJSON Resource` field the resource you just created. The
`GeoJSON Key Field` should be `wb_a3`, as we found out before. We'll
link that field to the `Country Code` column in our data, so set it
in the `Key` field.

Now, we just need to select what value we want to plot (let's use the latest
year, in the `2012` column), and what label to use (`Country Name`).
You can leave the remaining fields blank. In the end, we'll have:

| Attribute         | Value                            |
|-------------------|----------------------------------|
| GeoJSON Resource  | *(Your GeoJSON Resource's name)* |
| GeoJSON Key Field | wb\_a3                           |
| Key               | Country Code                     |
| Value             | 2012                             |
| Label             | Country Name                     |
| Redirect to URL   |                                  |
| Fields            |                                  |

Click on `Preview` and you should see a map like:

![Worldwide Internet usage](doc/img/worldwide-internet-usage.png)

Congratulations! You've just created your first choropleth map. You can go
ahead and see how the maps look like in other years. We can't compare the maps
directly, as the scales change depending on the data, but the difference from
2000 to 2012 is still impressive.

### Filters

If the map is shown in places other than its original URL in the resource
view's list (for example, inside a
[ckanext-dashboard](//github.com/ckan/ckanext-dashboard) or
[ckanext-page](//github.com/ckan/ckanext-pages)), its regions become clickable.

When the user clicks on a region, we'll add a filter to the current page using
the `Key` attribute. Using the previous example, if I clicked on Brazil, it'll
add the filters `Country Code:BRA` to the current page.

The user can deactivate the filters by clicking on the same region again, and
can activate multiple filters.

If you'd like to, when clicking on a region, redirect the user to another page
with that filter set (for example, another resource view or a dashboard),
you can add the target URL to the `Redirect to URL` field. If that's left
blank, it'll simply add filters to the current page.

To learn more about it, check the
[ckanext-viewhelpers](//github.com/ckan/ckanext-viewhelpers) page.

License
-------

Copyright (C) 2014 Open Knowledge Foundation

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published
by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.

