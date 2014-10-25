import csv
import os
import urllib
from collections import OrderedDict

class AttrDict(dict): 
    __getattr__ = dict.__getitem__
    __setattr__ = dict.__setitem__


def get_master(master_csv_url):
    fo = urllib.urlopen(master_csv_url)
    reader = csv.DictReader(fo)
    return [ AttrDict(x) for x in reader ]

# assumes on github
def get_extension_info(master_info_dict):
    outdict = AttrDict(master_info_dict)
    outdict.name = outdict.name.replace('ckanext-', '')
    # : is an illegal character in front-matter
    outdict.title = outdict.title.split('.')[0].replace(':', '-')
    # url is github url
    parts = outdict.url.split('/')
    outdict.github_user = parts[3]
    outdict.github_repo = parts[4]
    # try to find the README or README.md etc
    outdict.readme = _get_readme(outdict.github_user, outdict.github_repo)
    return outdict

def _get_readme(user, repo):
    exts = [ '.md', '.markdown', '.rst', '' ]
    for ext in exts:
        url = 'https://raw.githubusercontent.com/%s/%s/master/' % (user, repo)
        url += 'README' + ext
        urlfo = urllib.urlopen(url)
        if urlfo.getcode() != 404:
            return urlfo.read()

def write_extension(extension):
    print('Processing: %s' % extension.name)
    fp = os.path.join('extensions', '%s.md' % extension.name)
    outfo = open(fp, 'w')
    frontmatter = '''---
layout: extension
name: %(name)s
title: %(title)s
author: %(author)s
homepage: %(url)s
github_user: %(github_user)s
github_repo: %(github_repo)s
category: Extension
featured: %(featured)s
permalink: /extension/%(name)s/
---
''' % extension

    out = '%s\n\n%s\n' % (frontmatter, extension.readme)
    outfo.write(out)
    outfo.close()


# https://docs.google.com/a/okfn.org/spreadsheets/d/1izCpljO6Et7zLUKcUlB4BzsMZTurENp56Iqi9kXOtgs/edit#gid=0
master_csv_url = 'https://docs.google.com/spreadsheets/d/1izCpljO6Et7zLUKcUlB4BzsMZTurENp56Iqi9kXOtgs/export?gid=0&format=csv'

if __name__ == '__main__':
    toprocess = get_master(master_csv_url)
    toprocess = [ x for x in toprocess if x.show ]
    for ext in toprocess:
        info = get_extension_info(ext)
        write_extension(info)

