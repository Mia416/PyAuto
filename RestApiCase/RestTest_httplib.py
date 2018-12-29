'''
Created on Dec 27, 2018

@author: paul
'''
import httplib2
import urllib.request
import socks
import lib.Initlib as init
 
#https://github.com/httplib2/httplib2/wiki/Examples-Python3
#https://github.com/httplib2/httplib2/wiki/Examples




h = httplib2.Http()
h.add_credentials(init.username,init.password)
#change to real o
h = httplib2.Http(proxy_info = httplib2.ProxyInfo(socks.PROXY_TYPE_HTTP, 'www-proxy.idc.**.com', 80))

r,content = h.request(init.github_test_url,"GET",headers={'content-type':'text/plain'})
print (content)

 
 
h = httplib2.Http(".cache")
h.add_credentials(init.labusername,init.labpassword) 
content = h.request(init.lab_test_get_url, "GET")
print (content)
 