#!/usr/bin/env python3
"""return the elements in a mongo db collection"""


def list_all(mongo_collection):
    """return an empty list if collection is empty"""
    return [documents for documents in mongo_collection.find()]
