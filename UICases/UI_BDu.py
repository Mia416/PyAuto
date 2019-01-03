'''
Created on Jan 3, 2019

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

class TestBaiduPage(unittest.TestCase):
    def test_login(self):
        uilog = lib.UILogger.get_logger("baidu_log.txt")
        try:
            li = lib.UIBaseLib.uilib()
            browser = li.setup("https://www.baidu.com/")
            li.safeEnterText(browser, "id", "kw", "automation test")
            li.sleep(browser,10)
            li.safeClick(browser, "id", "su")
            li.sleep(browser,10)
            element_result = li.locatelement(browser, "class","nums_text")  
            print (li.get_element_value(browser, "class","nums_text"))
            w_handle = li.getwindowhandle(browser)
            li.hardsleep(10)
            li.Scroll_down(browser)
            li.Scroll_up(browser)
            li.save_screenshot(browser, "baidu0103.png")
            li.safeClick(browser, "xpath","//*[@id='1']/h3/a") 
            li.hardsleep(10)
            
            li.switchwindow(browser, w_handle)
            li.hardsleep(10)
        finally:
             browser.quit()  
        

if __name__ == '__main__':
    unittest.main()

