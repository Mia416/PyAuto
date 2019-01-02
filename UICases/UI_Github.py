'''
Created on Dec 24, 2018

@author: paul
'''

from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import unittest
import os
import time
import base64
import lib.UIBaseLib
import lib.UILogger
import lib.Initlib as init


class TestStringMethods(unittest.TestCase):
    
    url="https://github.com/login"
        

    def test_login(self):
        #copy chromedriver.exe to python/scripts folder          
        
 
        
        uilog = lib.UILogger.get_logger("log.txt")
        #print(username)              
        
        #req_url = "https://github.com/login"
        #browser = webdriver.Chrome()
        #browser.get(self.url)        
        try:
            li = lib.UIBaseLib.uilib()
            browser = li.setup("https://github.com/login")
            li.safeEnterText(browser,"id","login_field",init.username)
            li.safeEnterText(browser,"id","password",init.password)
            li.safeClick(browser, "name", "commit")
            element_result = li.waitForElementToBeVisible(browser, "css", "span[title='SAutoTest']")       
            self.assertIsNotNone(element_result) 
            uilog.info("log in well")          
           
            
        finally:
            browser.quit()     


if __name__ == '__main__':
    unittest.main()

