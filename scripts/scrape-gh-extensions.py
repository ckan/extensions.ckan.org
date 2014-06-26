import urllib
import json
import csv

jsonfp = 'data/extensions-gh.json'
csvfp = 'data/extensions-gh.csv'

def get_extensions_on_github():
    '''Download list of CKAN extensions on Github.
    
    We find the extensions by the heuristic of searching for repositories with
    ckanext in their name.

    We try to filter out some "trivial" extensions (experiments etc) by
    ignorning extensions that end in ckanext or have deprecated in their name
    '''
    base = 'https://api.github.com/search/repositories?q=ckanext'

    # get number of pages to go through in results on github
    counturl = base + '&per_page=1'
    fo = urllib.urlopen(counturl)
    out = json.load(fo)
    total = int(out['total_count'])
    maxpage = int(total/100) + 2

    login_to_author = {
        'okfn': 'Open Knowledge',
        'ckan': 'CKAN',
        'datagovuk': 'Data.Gov.UK - Cabinet Office'
        }

    def _extract(repo_dict):
        login = repo_dict['owner']['login']
        if login in login_to_author:
            author = login_to_author[login]
        else:
            info = json.load(urllib.urlopen(repo_dict['owner']['url']))
            author = info.get('name', login)
            login_to_author[login] = author
        return {
            'name': repo_dict['name'],
            'title': repo_dict['description'],
            'author': author,
            'url': repo_dict['html_url'],
            'description': '',
            'type': 'Extension',
            'updated_at': repo_dict['updated_at'],
            'status': '',
            }

    results = []

    for idx in range(1, maxpage):
        url = base + '&per_page=100&page=%s' % idx 
        print url
        fo = urllib.urlopen(url)
        indata = json.load(fo)
        results += [
            _extract(item) for item in indata['items']
            # if just called ckanext probably just an experiment
            if not (
                item['name'].endswith('ckanext')
                or
                'deprecated' in item['name'].lower()
                or
                'deprecated' in item['description'].lower()
                )
            ]

    def ourcmp(x,y):
        return cmp(x['name'], y['name'])
    results = sorted(results, ourcmp)
    outfo = open(jsonfp, 'w')
    json.dump(results, outfo, indent=2)

def json_to_csv():
    fo = open(csvfp, 'w')
    fields = ['name', 'title', 'url', 'description', 'author', 'type',
            'status', 'updated_at']
    writer = csv.DictWriter(fo, fieldnames=fields, lineterminator='\n')
    writer.writeheader()

    data = json.load(open(jsonfp))
    for row in data:
        # get rid of utf8 errors by encoding in advance
        for k,v in row.items():
            if v != None:
                row[k] = v.encode('utf8')

        writer.writerow(row)

if __name__ == '__main__':
    get_extensions_on_github()
    # json_to_csv()

