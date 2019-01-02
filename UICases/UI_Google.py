'''
Created on Jan 2, 2019

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


class TestGooglePage(unittest.TestCase):
    def test_login(self):
        uilog = lib.UILogger.get_logger("Google_log.txt")
        try:
            li = lib.UIBaseLib.uilib()
            browser = li.setup("https://www.google.com/")
            li.safeEnterText(browser, "name", "q", "Tiger")
            li.sleep(browser,10)
            li.safeClick(browser, "name", "btnK")
            li.sleep(browser,10)
            element_result = li.locatelement(browser, "id", "resultStats")  
            print (li.get_element_value(browser, "id", "resultStats"))
            li.sleep(browser,10)
            li.Scroll_down(browser)
            li.Scroll_up(browser)
            li.save_screenshot(browser, "google0102.png")
        finally:
             browser.quit()  
        

if __name__ == '__main__':
    unittest.main()

