#!/usr/bin/env python3
"""
Script that provides some stats about Nginx logs stored in MongoDB.
"""
from pymongo import MongoClient


def log_stats():
    """
    Connects to the MongoDB database and prints statistics
    about the Nginx logs.
    """
    # Connexion au serveur local
    client = MongoClient('mongodb://127.0.0.1:27017')
    
    # On cible la collection 'nginx' dans la base 'logs'
    nginx_collection = client.logs.nginx

    # 1. Nombre total de logs
    total_logs = nginx_collection.count_documents({})
    print(f"{total_logs} logs")

    # 2. Nombre de logs par méthode HTTP
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = nginx_collection.count_documents({"method": method})
        # Le \t sert à faire la tabulation demandée par la consigne
        print(f"\tmethod {method}: {count}")

    # 3. Nombre de logs pour le status check
    status_check = nginx_collection.count_documents(
        {"method": "GET", "path": "/status"}
    )
    print(f"{status_check} status check")


if __name__ == "__main__":
    log_stats()