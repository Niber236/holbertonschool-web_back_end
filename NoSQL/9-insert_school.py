#!/usr/bin/env python3
"""
Module that inserts a new document in a MongoDB collection.
"""


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document in a collection based on kwargs.

    Args:
        mongo_collection: A pymongo collection object.
        **kwargs: The data for the new document.

    Returns:
        The _id of the newly inserted document.
    """
    # insert_one insère le dictionnaire kwargs et on récupère son ID généré
    new_document = mongo_collection.insert_one(kwargs)
    return new_document.inserted_id