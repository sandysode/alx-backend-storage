#!/usr/bin/env python3
""" 9. Insert a document in Python """


def insert_school(mongo_collection, **kwargs):
    """ Inserts a new document in a collection based on kwargs

    Args:
    mongo_collection: the pymongo collection object
    **kwargs: represent data to insert
    """
    return mongo_collection.insert(kwargs)
