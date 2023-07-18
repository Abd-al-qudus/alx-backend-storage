#!/usr/bin/env python3
"""return all students sorted by average scores"""
from collections import OrderedDict


def top_students(mongo_collection):
    """sort collection and return sorted collection"""
    pipeline = [{'$addFields': {'averageScore': {'$avg': '$topics.score'}}},
                {'$sort': OrderedDict([('averageScore', -1), ('name', 1)])}]
    return mongo_collection.aggregate(pipeline)
