from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import unittest
import os
import time

class uilib:
    
    
    def setup(self,URL):
        browser = webdriver.Chrome()
        browser.get(URL)
        return browser  
    
    def locatelement(self,driver,locatorKey,locatorVal):
        if locatorKey == "id":
            element = driver.find_element_by_id(locatorVal)
        if locatorKey == "name":
            element = driver.find_element_by_name(locatorVal)
        if locatorKey == "css":
            element = driver.find_element_by_css_selector(locatorVal)
        if locatorKey == "xpath":
            element = driver.find_element_by_xpath(locatorVal)
        if locatorKey == "class":
            element = driver.find_element_by_class_name(locatorVal)
        if locatorKey == "linktest":
            element = driver.find_element_by_partial_link_text(locatorVal)
        if locatorKey == "tag":
            element = driver.find_element_by_tag_name(locatorVal)
        return element
    
    def waitForElementToBeVisible(self,driver,locatorKey,locatorVal):
        if locatorKey == "id":
            element = WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.ID, locatorVal)));
        elif locatorKey == "name":          
            element = WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.NAME, locatorVal)));
        elif locatorKey == "css":          
            element = WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, locatorVal)));  
        elif locatorKey == "xpath":          
            element = WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH, locatorVal))); 
        elif locatorKey == "class":          
            element = WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, locatorVal)));     
        elif locatorKey == "linktest":          
            element = WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.PARTIAL_LINK_TEXT, locatorVal)));   
        elif locatorKey == "tag":          
            element = WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.TAG_NAME, locatorVal)));             
                
        return element
        
    def safeEnterText(self,driver,locatorKey,locatorVal,context):
        self.waitForElementToBeVisible(driver, locatorKey, locatorVal)
        element = self.locatelement(driver,locatorKey,locatorVal)
        element.send_keys(context)
        
    def safeClick(self,driver,locatorKey,locatorVal):
        self.waitForElementToBeVisible(driver, locatorKey, locatorVal)
        element = self.locatelement(driver,locatorKey,locatorVal)
        element.click()
        
        
        
   
    

 