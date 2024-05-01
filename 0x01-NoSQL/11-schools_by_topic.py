#!/usr/bin/env python3
""" MongoDB Operations with Python using pymongo """


def schools_by_topic(mongo_collection, topic):
    """ List of school having a specific topic
    Args:
    mongo_collection: the pymongo collection object
    topics (string): will be topic searched

    Return:
    List: List of topics
    """
    documents = mongo_collection.find({"topics": topic})
    return list(documents)
