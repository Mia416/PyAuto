'''
Created on Dec 24, 2018

@author: paul
'''
import requests
import json
import lib.Initlib as init
from collections import OrderedDict
 

#http://blog.51cto.com/ciscoexpert/2132837

r_p1 = requests.get(init.lab_test_get_param_url +'subscriptions/525065391',headers={init.lab_header_userid : "kimjin@ora.com" ,init.lab_header_authid:init.lab_header_authvalue}, auth=(init.labusername,init.labpassword))
print (r_p1.text)
r = requests.get(init.github_test_url, proxies=init.proxyDict) 
r1 = requests.get(init.github_test_rep_url, auth=(init.username,init.password),proxies=init.proxyDict)
r_l = requests.get(init.lab_test_get_url, auth=(init.labusername,init.labpassword))
r_p = requests.post(init.lab_test_post_url,auth=(init.lab_post_username,init.lab_post_password),json=init.post_json)
print (r_p.text)
print (r.text)
print (r1.text)
print (r_l.text)

