#!/usr/bin/env python3
""" Something """


def list_all(mongo_collection):
    """ Something """
    docs = mongo_collection.find()
    return list(docs) if docs else []
