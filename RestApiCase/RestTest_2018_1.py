'''
Created on Dec 27, 2018

@author: paul
'''
import base64
import lib.Initlib as init
import lib.JsonLib as jsoninit


jsoninit.load_xml_node()
#init.sendmail()

# test file 
t1 = base64.b64encode(b'idcs-75eca8dde95841d3a6225af31282104c')
print (t1)
#t2 = base64.b64decode(b'aHR0cHM6Ly90YXNjZW50cmFsLmM5cWExMzIub3JhY2xlY29ycC5jb20vdGFzL2Rhc2hib2FyZC9yZXN0L2NvbW1hbmQ=').decode('utf-8')
#print (t2)

username = base64.b64decode(b'TWlhNDE2').decode('utf-8')
password = base64.b64decode(b'ODIwMzExIXhpeXU=').decode('utf-8')