#!/usr/bin/env python3
"""return the collection count for the method
    of nginx log file"""


if __name__ == "__main__":
    import pymongo

    client = pymongo.MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs
    collection = db.nginx

    total_logs = collection.count_documents({})
    print("{} logs".format(total_logs))

    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    for method in methods:
        count = collection.count_documents({'method': method})
        print('method {}: {}'.format(method, count))

    status_check_count = collection.count_documents(
        {'method': 'GET', 'path': '/status'})
    print('{} status check'.format(status_check_count))
