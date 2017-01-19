---
layout: extension
name: patcategories
title: CKAN extension to offer a list of categories defined by Provincia Autonoma di Trento
author: Open Data in Trentino
homepage: https://github.com/opendatatrentino/ckanext-patcategories
github_user: opendatatrentino
github_repo: ckanext-patcategories
category: Extension
featured: 
permalink: /extension/patcategories/
---


ckanext patcategories
=====================

Install
=======
```bash
pip install -e git+https://github.com/opendatatrentino/ckanext-patcategories.git#egg=ckanext-categories 
```

How to use
==========

I comandi che possono essere usati per creare e cancellare nuove voci
dei vocabolari presenti; i comandi vanno lanciati dalla cartella del
plugin "ckanext-patform",

start from the directory ckanext-patform 
(eg. 
```bash
cd /where/is/ckan/ckanext-patform )
```

to add a term in the vocabulary
```bash
paster pat add-term <vocab_name> <new_term> -c <path to config file>
```
to remove a term from the vocabulary
```bash
paster pat remove-term <vocab_name> <term_to_remove> -c <path to config file>
```

Example
=======
```
paster pat add-term category_vocab Mobilita -c /etc/ckan.ini
````

The terms cad be added to this different vocabularies:
- category_vocab (Categories)
- holders_vocab (Holders)
- coverage_vocab (Geographical coverage)

Categories used in dati.trentino.it
===================================
Ambiente
Amministrazione
Conoscenza
Cultura
Demografia
Economia
Gestione del territorio
Meteo
Mobilita
Politica
Sicurezza
Sport
Welfare

