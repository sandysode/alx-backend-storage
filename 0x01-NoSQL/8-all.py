#!/usr/bin/env python3
""" 8. List all documents in Python """


def list_all(mongo_collection):
    """ List all documents in a collection
    Args:
    mongo_collection: the pymongo collection object

    Return:
    List of documents or an empty list
    """
    documents = mongo_collection.find()

    if documents.count() == 0:
        return []

    return documents
