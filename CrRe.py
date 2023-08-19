#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 29 03:00:21 2023

@author: wesstonmccoll_snhu
"""

from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """
    def __init__(self):
        print("b")
    
    
    def __init__(self, username, password):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections.
        # This is hard-wired to use the aac database, the 
        # animals collection, and the aac user.
        # Definitions of the connection string variables are
        # unique to the individual Apporto environment.
        #
        # You must edit the connection variables below to reflect
        # your own instance of MongoDB!
        #
        # Connection Variables
        #
        print("A")
        USER = username
        PASS = password
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 30736
        DB = 'AAC'
        COL = 'animals'
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]
        print("You're connected")

    """
        create
            param: self, data(dictionary)
            returns: bool
            
            Function intakes a key/value pair and creates an entry
            After entry created, returns True
    """    
    def create(self, data):
        if data is not None:
            self.database.animals.insert_one(data)     
            return True
        else:
            raise Exception("Nothing to save, because data parameter is empty")
            return False

    """
        read
            param: self, data(dictionary)
            returns: dict
            
            Function intakes a key/value pair and returns entries that
            match data
            
    """ 
    def read(self, data):
        if data is not None:
            if self.database.animals.find(data):
                return self.database.animals.find(data)
            else:
                return
        else:
            raise Exception("No values to query for")
            
            
    """
        update
            param: self, data(dictionary), newData(dictionary)
            returns: int
            
            Function intakes two key/value pairs; first searches for entries
            that matches first key/value, then updates entry with second
            key/value pair. Returns number of entries edited
    """ 
            
    def update(self, data, newData):
        
        if data is not None and newData is not None:
            results = self.database.animals.update_many(data, {"$set":newData})     
            return results.modified_count
        else:
            raise Exception("Not enough arguments given to update")
            
    """
        delete
            param: self, data(dictionary)
            returns: int
            
            Function intakes a key/value pair and deletes entries that match
            the pair. Returns number of entries deleted
    """ 
            
    def delete(self, data):
        if data is not None:
            results = self.database.animals.delete_many(data)    
            return results.deleted_count
        else:
            raise Exception("Nothing to save, because data parameter is empty")
