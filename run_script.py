#!/usr/bin/env python3
import json

# initialize django
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'arcticapi.settings'
import django
django.setup()

# regular imports
from api.models import Category, Product

def main():
    
    with open('products.json') as json_file:
        data = json.load(json_file)
    
    products = data['products']
    cats = []
    for prod in products:
        if prod['category'] not in cats:
            cats.append(prod['category'])
    
    for c in cats:
        dbcat = Category()
        dbcat.title = c
        dbcat.save()
    for prod in products:
        dbprod = Product()
        dbprod.name = prod['name']
        dbprod.description = prod['description']
        dbprod.filename = prod['filename']
        dbprod.price = prod['price']
        dbprod.category = Category.objects.get(title=prod['category'])
        dbprod.save()

# bootstrap
if __name__ == '__main__':
    main()
