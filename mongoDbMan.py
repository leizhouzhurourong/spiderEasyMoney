# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 10:05:54 2018

@author: xuzairong
"""
import pymongo
from config import mongoPass,mongourl,dataBase,collection
class MongoMan:
    def __init__(self):
        # 连接到mongodb，如果参数不填，默认为“localhost:27017”
        self.client = pymongo.MongoClient(mongourl)
        self.db = self.client[dataBase]
        
        #连接到集合(表):myDatabase.myCollection
        self.db_coll = self.db[collection ]
    def insert_many(self,insertRecords):
        # 更高效，但要注意如果指定_id，一定不能重复
        # ordered = True，遇到错误 break, 并且抛出异常
        # ordered = False，遇到错误 continue, 循环结束后抛出异常
        self.db_coll.insert_many(insertRecords, ordered = True)
