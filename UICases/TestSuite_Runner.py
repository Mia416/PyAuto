'''
Created on Jan 4, 2019

@author: paul
'''
import HtmlTestRunner
import unittest
import UICases.UI_Google
import xmlrunner

def run_html_report():        
        testRunner=HtmlTestRunner.HTMLTestRunner(output='html_report_dir')
        test_suite = unittest.TestSuite()         
        test_suite.addTest(UICases.UI_Google.TestGooglePage('test_login'))        
        testRunner.run(test_suite)

def run_xml_report():             
        testRunner=xmlrunner.XMLTestRunner(output='..\\report')
        test_suite = unittest.TestSuite()        
        test_suite.addTest(UICases.UI_Google.TestGooglePage('test_login'))        
        testRunner.run(test_suite)


if __name__=='__main__':
         run_html_report()


 
    