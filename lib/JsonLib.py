'''
Created on Jan 3, 2019

@author: mia
'''
import json
import urllib.request
from urllib.request import urlopen
import xml.etree.ElementTree as ET


def load_fromURL():
    url = 'http://xxxx.xxxx.com:8080/v1/services/_/versions/_/artifacts?release=17.2.1&previous_release=17.1.6&qualifiers=tasbp'
    response = urlopen(url)
    json_to_python = json.load(response)
    #print (json_to_python)
    #urlpath = (json_to_python["artifacts"][1]["uri"])
    for node in json_to_python["artifacts"]:
        print (node["uri"])
        
def load_fromString():
    jsonstring ={
     'artifacts':
     [
     {
      'qualifier':'tasbp',
      'service':{
        'release':'17.2.1',
        'display_name':'Application Container Cloud',
        'artifact_id':'apaas',
        'version':'17.2.1-531',
        'target_maturity':'production',
        'service_id':'c7928dd7-dca5-4225-9486-f2286e417e45'
        },
     'uri':'http://almrepo.us.xxxxx.com/artifactory/xxxxx/com/xxxx/opc/definition/tasbp-apaas/17.2.1-1703131042/tasbp-apaas-17.2.1-1703131042.zip'
     },
     {
      'qualifier':'tasbp',
      'service':{
        'release':'17.2.1',
        'display_name':'psm',
        'artifact_id':'psm',
        'version':'17.2.1-548',
        'tags':[
        '17.2.1.2'
               ],
     'target_maturity':'production',
     'service_id':'8720ac6d-c99b-4bbe-9958-094ee35bc99c'
     },
     'uri':'http://almrepo.us.xxxxx.com/artifactory/xxxxx/opc/definition/tasbp-psm-jaas/17.1.5-543/tasbp-psm-jaas-17.1.5-543.zip'
     },
     ]
     }
    python_to_json2 = json.dumps(jsonstring,sort_keys=True,indent =4,separators=(',', ': '),ensure_ascii=True )
    json_to_python = json.loads(python_to_json2)
    for node in json_to_python["artifacts"]:
        urladdress = node["uri"]
        filename = urladdress.split('/')[-1]
        print(filename)
        #req = urllib.request.urlretrieve(urladdress, filename) 
        #print (node["uri"])   
        
        
def load_xml_node():
        xmltree = ET.parse('../doc/test1.xml')
        for node in xmltree.findall('.//{http://xmlns.schemas.oracle.com/tasBlueprint}name'):
            print (node.tag, node.text)
            break
        for node in xmltree.iter('{http://xmlns.schemas.oracle.com/tasBlueprint}name'):
            print (node.tag, node.text)
            break        
        
def load_from_data():            
        data = {"project":"platform/xxxxx/xxxxxx/build/repo","branch":"xxxxx_xx.xxxxx.xxx.1.0-dev","id":"T19797TIE76757IT78689899G",
                "number":"1917095","subject":"xxxxx-2.0: blah blah blah","owner":{"name":"David","email":"david@xxxx.com","username":"david"},
                "url":"https://link_to_repo.com/1917095","createdOn":"1493282302","lastUpdated":"1493813064","sortKey":"000899786887","open":"false","status":"MERGED"}

        data1 = {
             "businesses": [
                 {
                     "id": "gaumont-wilson-toulouse-2",
                     "name": "Gaumont Wilson",
                     "city": "Toulouse"           
                 },
                 
                {
                     "id": "la-cinmathque-de-toulouse-toulouse",
                     "name": "La Cinmathque de Toulouse",
                     "city": "Toulouse"
                },
                {
                     "id": "abc-toulouse",
                     "name": "ABC",
                     "city": "Toulouse"
                 },
                         ]
                }
        jsonobject = json.dumps(data)
        print (jsonobject)
        jsonobjectToString = json.loads(jsonobject)
        print (jsonobjectToString)

        print (jsonobjectToString["number"])
        print (jsonobjectToString["owner"]["email"])

        jsonobject = json.dumps(data1)
 
        jsonobjectToString = json.loads(jsonobject)
        for resp in jsonobjectToString['businesses']:
            print(resp['id'])
            print(resp['name'])
            print(resp['city'])
