'''
Created on Jan 3, 2019

@author: chenz
'''
import xml.etree.ElementTree as ET



def getelementfromfile():    
    tree = ET.parse('../doc/1.xml')
    root = tree.getroot()
    element = root[0].tag
    first_text = root[0].text #This is the first sentence
    button = root[0][0].tag #button
    buttontext = root[0][0].text #click
    for node in tree.iter('element'):
         print(node.text)
         print(node.attrib)

def getelementbynamespace():    
    tree = ET.parse('../doc/XMLNamespace.xml')
    root = tree.getroot()
    tag1 = root.find('.//{http://some/www.hello.com}tag1')  # accessing tag with namespace
    print(tag1.text)
         
def fetchelementfromfile():
    tree = ET.parse('../doc/3.xml')
    root = tree.getroot()
    print (root[1][0].get('name'))    
    for neighbor in root.iter('part'):
         print(neighbor.get('name'))
         
def gettailvalue():     
    tree = ET.parse('../doc/tail.xml')
    root = tree.getroot()
    print(root.find('TAGB').tail.strip())

def pushallchilddata():
    tree = ET.parse('../doc/4.xml')
    root = tree.getroot()
    ditresult =[]
    for child in root:
         for child1 in child:         
            ditresult.append(child1.tag)
            print (ditresult)

         
def retriveeachelementfromfile():
 
         tree = ET.parse('../doc/example.xml')
         root = tree.getroot()
         #As an Element, root has a tag and a dictionary of attributes:
         print(root.tag)
         print(root.attrib)
         #It also has children nodes over which we can iterate:
         for child in root:
             print(child.tag)
             print(child.attrib)  
    
        #Children are nested, and we can access specific child nodes by index:
             print (root[0][1].text)
#Element has some useful methods that help iterate recursively over all the sub-tree below it 
#(its children, their children, and so on). For example, Element.iter():
             for neighbor in root.iter('neighbor'):
                 print (neighbor.tag)    
                 print(neighbor.attrib)   
    
#Element.findall() finds only elements with a tag which are direct children of the current element. Element.find() finds the first child with a particular tag, 
#and Element.text accesses the element text content. Element.get() accesses the element attributes:
             for country in root.findall('country'):
                 rank = country.find('rank').text
                 name = country.get('name')
                 print(name, rank)
    
#getelementbynamespace()