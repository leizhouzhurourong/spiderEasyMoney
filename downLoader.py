# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 10:27:34 2018

@author: xuzairong
"""
from selenium import webdriver
from selenium.common.exceptions import TimeoutException                                                                                                                                                         
from selenium.webdriver.support.ui import WebDriverWait                                                                                                                                                         
from selenium.webdriver.common.by import By                                                                                                                                                                     
from selenium.webdriver.support import expected_conditions as EC                                                                                                                                                

class Downloader:
    def __init__(self):
        self.driver = webdriver.PhantomJS()
        self.driver.set_page_load_timeout(20)
    def getStockInfo(self ,url):
        try:
            self.driver.get(url)
            return self.driver
        except Exception as e:
           return None
        