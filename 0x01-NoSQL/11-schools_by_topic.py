#!/usr/bin/env python3
"""return topics in collection with specific values"""


def schools_by_topic(mongo_collection, topic):
    """filter the db collection"""
    filtered_topics = {
        'topics' : {
            '$elemMatch': {
                '$eq': topic
            }
        }
    }
    return [documents for documents in mongo_collection.find(filtered_topics)]
