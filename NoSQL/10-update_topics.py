#!/usr/bin/env python3
""" Something """


def update_topics(mongo_collection, name, topics):
    """ Something """
    return mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
