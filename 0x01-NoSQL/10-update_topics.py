#!/usr/bin/env python3
""" 10. Change school topics """


def update_topics(mongo_collection, name, topics):
    """ Changes all topics of a school doc based on the name
    Args:
    mongo_collection: the pymongo collection object
    name (string): will be the school name to update
    topics (list of strings): will be the list of topics approached in the school
    """
    query = {"name": name}
    new_values = {"$set": {"topics": topics}}

    mongo_collection.update_many(query, new_values)
