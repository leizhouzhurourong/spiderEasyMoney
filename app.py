# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 10:06:13 2018

@author: xuzairong
"""
from urlsMan import StockListUrlMan
from config import stockListUrl,stockUrl
from downLoader import Downloader
from myParser import Parser
from mongoDbMan import MongoMan
        

if __name__=="__main__":
    #url管理器
    urlsManObject = StockListUrlMan()
    stockListUrls  = urlsManObject.getStockListUrl(stockListUrl)
    #下载器
    downloaderObject  = Downloader()
    #解析器
    parserObject = Parser()
    #mongo管理器
    mongoManObject = MongoMan()
    #结果
    result = []
    count = 0
    for url in stockListUrls:
        print(url)
        try:
            driver = downloaderObject.getStockInfo(url)
            json = parserObject.parseCoreData(driver)
            json["url"] = url
            result.append(json)
            count = count+1
            print(count)
            if count%10 ==0:
                mongoManObject.insert_many(result)
                result=[]
        except Exception as es:
            print(es)
            
    #写到mongo
    mongoManObject.insert_many(result)
    
       
    