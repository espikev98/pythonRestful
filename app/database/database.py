'''
Database package main module
'''
from pymongo import MongoClient

class Database():

    def __init__(self, hostname, port, username, password, db):
        self.client = MongoClient(hostname,
                                  port,
                                  username=username,
                                  password=password,
                                  authSource=db)

    def collection_create(self, collection_name):
        pass
