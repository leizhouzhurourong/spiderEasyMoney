# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 10:07:39 2018

@author: xuzairong
"""
import requests
from bs4 import BeautifulSoup
from config import stockUrl
class StockListUrlMan:
    def __init__(self):
        self.urls = []
    def getStockListUrl(self,stockListUrl):
        html = requests.get(stockListUrl).content
        soup = BeautifulSoup(html,"lxml")
        urlList = soup.find('div',class_='quotebody').find_all('a',{'target':'_blank'})
        for url in urlList:
            num =url.get_text().split('(')[1].strip(')')
            if num.startswith('00'):
                self.urls.append(stockUrl+"/sz"+num+".html")
            elif num.startswith('60'):
                self.urls.append(stockUrl+"/sh"+num+".html")
        return self.urls    