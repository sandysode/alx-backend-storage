#!/usr/bin/env python3
""" 14. Top students """


def top_students(mongo_collection):
    """ Returns all students sorted by average score
    Args:
    mongo_collection: the pymongo collection object"""
    student = mongo_collection.aggregate([
        {
            "$project": {
                "name": "$name",
                "averageScore": {"$avg": "$topics.score"}
            }
        },
        {"$sort": {"averageScore": -1}}
    ])

    return student
