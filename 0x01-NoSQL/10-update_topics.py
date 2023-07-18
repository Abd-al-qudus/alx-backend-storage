#!/usr/bin/env python3
"""update many value in the mongodb collection"""


def update_topics(mongo_collection, name, topics):
    """update topic based on name"""
    mongo_collection.update_many(
        {'name': name},
        {'$set': {'topics': topics}}
    )
