import csv
import os
from urllib.request import urlopen
from urllib.error import HTTPError, URLError
import codecs
import pypandoc
from collections import OrderedDict

class AttrDict(dict):
    __getattr__ = dict.__getitem__
    __setattr__ = dict.__setitem__


def get_master(master_csv_url):
    fo = urlopen(master_csv_url)
    reader = csv.DictReader(codecs.iterdecode(fo, 'utf-8'))
    return [ AttrDict(x) for x in reader ]

# assumes on github
def get_extension_info(master_info_dict):
    outdict = AttrDict(master_info_dict)
    outdict.name = outdict.name.replace('ckanext-', '').lower()
    # : is an illegal character in front-matter
    outdict.title = outdict.title.split('.')[0].replace(':', '-')
    # url is github url
    parts = outdict.url.split('/')
    if len(parts) == 5:
        outdict['github_user'] = parts[3]
        outdict['github_repo'] = parts[4]
    else:
        outdict['github_user'] = ''
        outdict['github_repo'] = ''

    # try to find the README or README.md etc
    try:
        outdict.readme = _get_readme(outdict.github_user, outdict.github_repo)
    except (HTTPError, URLError):
        print(f'Error getting README for {outdict.name}')
        outdict['readme'] = '<Error getting README>'
    return outdict

def _get_readme(user, repo):
    exts = [ '.md', '.markdown', '.rst', '' ]
    for ext in exts:
        urlbase = 'https://raw.githubusercontent.com/%s/%s/master/' % (user, repo)
        url = urlbase + 'README' + ext
        urlfo = urlopen(url, timeout=5)
        if urlfo.getcode() == 404:
            # try lowercase readme
            url = urlbase + 'readme' + ext
            urlfo = urlopen(url)
        if urlfo.getcode() != 404:
            readme = urlfo.read()
            # {% is reserved for liquid templates
            readme = readme.replace(b'{% ', b'{%raw%}{% {%endraw%}')
            readme = readme.replace(b' %}', b'{%raw%} %}{%endraw%}')
            if ext == '.rst':
                readme = pypandoc.convert_text(readme, to='markdown_github', format = 'rst' )
            else:
                readme = pypandoc.convert_text(readme, to='markdown_github', format = 'markdown_github' )
            return readme

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

#    if type(extension.readme) == unicode:
#        extension.readme = extension.readme.encode('ascii', 'xmlcharrefreplace')
    out = '%s\n\n%s\n' % (frontmatter, extension.readme)
    outfo.write(out)
    outfo.close()


# https://docs.google.com/a/okfn.org/spreadsheets/d/1izCpljO6Et7zLUKcUlB4BzsMZTurENp56Iqi9kXOtgs/edit#gid=0
master_csv_url = 'https://docs.google.com/spreadsheets/d/1izCpljO6Et7zLUKcUlB4BzsMZTurENp56Iqi9kXOtgs/export?gid=0&format=csv'

import sys
if __name__ == '__main__':
    filt = sys.argv[1] if len(sys.argv) >= 2 else ''
    toprocess = get_master(master_csv_url)
    toprocess = [ x for x in toprocess if x.show and (filt in x.name)]
    for ext in toprocess:
        info = get_extension_info(ext)
        write_extension(info)

