'''
Created on Dec 24, 2018

@author: paul
'''
import logging

def get_logger(filename):    
    logging.basicConfig(filename=filename, filemode='a',level=logging.DEBUG,format='%(levelname)s  %(asctime)s  %(message)s')    
    return logging