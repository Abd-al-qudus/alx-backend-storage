#!/usr/bin/env python3
"""insert into a mongo db collection"""


def insert_school(mongo_collection, **kwargs):
    """insert into a mongo db based on kwargs"""
    return mongo_collection.insert_one(kwargs).inserted_id
