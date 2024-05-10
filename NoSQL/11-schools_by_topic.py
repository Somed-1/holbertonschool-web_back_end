#!/usr/bin/env python3
""" Something """


def schools_by_topic(mongo_collection, topic):
    """ Something """
    return mongo_collection.find({"topics": topic})
