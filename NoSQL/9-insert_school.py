#!/usr/bin/env python3
""" Something """


def insert_school(mongo_collection, **kwargs):
    """ Something """

    return mongo_collection.insert_one(kwargs).inserted_id
