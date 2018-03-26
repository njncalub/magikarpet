#!/usr/bin/env python
import Polygon.IO

from pymongo import MongoClient

from main.managers import CarpetManager
from main.models import Acrylic, Fiber, Nylon, Wool
from main.settings import DATABASE_NAME, DATABASE_URL
from main.utils import (
    populate_collection,
    purge_collection,
)


def do_test(header):
    def decorator(function):
        def wrapper(*args, **kwargs):
            print(header)
            function(*args, **kwargs)
            print("-" * 100)
        return wrapper
    return decorator

@do_test(header="Listing all carpets in inventory:")
def list_all_carpets(shop):
    """
    List all carpets in inventory.
    """
    carpets = shop.find_all()
    for carpet in carpets:
        print(f"- {carpet.pretty_print()}")

@do_test(header="Finding all 'nylon' carpets in stock:")
def find_nylon_all(shop):
    """
    Find all 'nylon' carpets.
    """
    carpets = shop.find_all({'carpet_type': 'nylon'})
    for carpet in carpets:
        print(f"- {carpet.pretty_print()}")

@do_test(header="Finding all new 'nylon' carpets in stock:")
def find_nylon_new(shop):
    """
    Find all new 'nylon' carpets.
    """
    carpets = shop.get_new_carpets('nylon')
    for carpet in carpets:
        print(f"- {carpet.pretty_print()}")

@do_test(header="Finding all cut 'nylon' carpets in stock:")
def find_nylon_cut(shop):
    """
    Find all cut 'nylon' carpets.
    """
    carpets = shop.get_cut_carpets('nylon')
    for carpet in carpets:
        print(f"- {carpet.pretty_print()}")

@do_test(header="Finding a 'nylon' carpet that will fit an 85x85 order:")
def find_nylon_fits(shop):
    """
    Finding a 'nylon' carpet that will fit a job order.
    """
    carpet = shop.get_carpet_for_cutting('nylon', 85, 85)
    if carpet:
        print(f"- {carpet.pretty_print()}")

@do_test(header="Cutting a 'nylon' carpet that will fit an 85x85 order:")
def cut_nylon_fits(shop):
    carpet = shop.get_carpet_for_cutting('nylon', 85, 85)
    if carpet:
        successful = carpet.cut(85, 85)
        if successful:
            carpet.save(shop.objects)
            carpet.save_image()  # save SVG image in /generated/

@do_test(header="Adding additional 'nylon' carpets to the inventory:")
def restock_nylon_5(shop):
    """
    Restock 'nylon' carpets. Quantity: 5.
    """
    shop.restock('nylon', quantity=5)

def main():
    # set up database connection
    client = MongoClient(DATABASE_URL)
    database = client[DATABASE_NAME]
    carpets_collection = database.carpets
    
    # set up database with test data
    purge_collection(carpets_collection)
    populate_collection(carpets_collection)
    
    # set up carpet manager
    shop = CarpetManager(carpets_collection)
    
    # do some API tests
    list_all_carpets(shop)
    find_nylon_all(shop)
    find_nylon_new(shop)
    find_nylon_cut(shop)
    find_nylon_fits(shop)
    cut_nylon_fits(shop)
    restock_nylon_5(shop)
    list_all_carpets(shop)

if __name__ == '__main__':
    main()
