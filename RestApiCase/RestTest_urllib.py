'''
Created on Dec 27, 2018

@author: paul
'''
import requests
import base64
import urllib.request 
import ssl
import lib.Initlib as init

#not ready for proxy setting


    

password_manager = urllib.request.HTTPPasswordMgrWithDefaultRealm()
password_manager.add_password(None, init.github_test_rep_url, init.username,init.password)
auth =  urllib.request.HTTPBasicAuthHandler(password_manager) # create an authentication handler
opener =  urllib.request.build_opener(auth) # create an opener with the authentication handler
urllib.request.install_opener(opener) # install the opener... 

proxy_support = urllib.request.ProxyHandler({'https': 'http://www-proxy.idc.oracle.com:80'})
opener =  urllib.request.build_opener(proxy_support) 
urllib.request.install_opener(opener)

#request =  urllib.request.Request(github_url,context=gcontext) # Manual encoding required
handler =  urllib.request.urlopen(init.github_test_rep_url)
 

print (handler.read())




