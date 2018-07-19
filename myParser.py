# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 11:20:08 2018

@author: xuzairong
"""
from bs4 import BeautifulSoup
class Parser:
    def __init__(self):
        pass
    def parseCoreData(self ,html):
         tbody = html.find_element_by_xpath(r"/html/body/div[1]/div[13]/div[1]/div[6]/div[1]")
         json = {}
         soup  =BeautifulSoup(tbody.get_attribute('innerHTML'),"lxml")
         trs = soup.select("tr")
         for tr in trs:
             tds = tr.select("td")
             for td in tds:
                 key = td.text.split(r"：")[0]
                 value =td.text.split(r"：")[1]
                 json[key] = value
         return json      
        