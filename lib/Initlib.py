'''
Created on Dec 28, 2018

@author: 
'''
import base64
import json
import smtplib
from email.mime.text import MIMEText


http_proxy  = "http://www-proxy.idc.***.com:80"
https_proxy = "http://www-proxy.idc.***.com:80"
 

proxyDict = { 
              "http"  : http_proxy, 
              "https" : https_proxy, 
               
            }

username = base64.b64decode(b'TWlhNDE2').decode('utf-8')
password = base64.b64decode(b'ODIwMzExIXhpeXU=').decode('utf-8')
lab_test_get_url = base64.b64decode(b'aHR0cHM6Ly90YXNjZW50cmFsLmM5cWExMzIub3JhY2xlY29ycC5jb20vdGFzLWNlbnRyYWwvLmNvbW1vbi90YXMvYXBpL3YxL2RhdGFSZWdpb25zL0xBMDAx').decode('utf-8')
lab_test_post_url = base64.b64decode(b'aHR0cHM6Ly90YXNjZW50cmFsLmM5cWExMzIub3JhY2xlY29ycC5jb20vdGFzL2Rhc2hib2FyZC9yZXN0L2NvbW1hbmQ=').decode('utf-8')
lab_test_get_param_url = base64.b64decode(b'aHR0cHM6Ly90YXNjZW50cmFsLmM5cWExMzIub3JhY2xlY29ycC5jb206NDQzL3Rhcy1jZW50cmFsLy5jb21tb24vdGFzL2FwaS92MS8=').decode('utf-8')
labusername = base64.b64decode(b'T0NMT1VEOV9UQVNfQVBQSUQ=').decode('utf-8')
labpassword = base64.b64decode(b'cnZxcHUybmRzVTNfd2o=').decode('utf-8')
lab_post_username = base64.b64decode(b'T0NMT1VEOV9PUENJTkZSQV9BRE1JTlVJX0FQUElE').decode('utf-8') 
lab_post_password = base64.b64decode(b'Y2xvdWQ5X1RBUw==').decode('utf-8')  
lab_header_userid = base64.b64decode(b'WC1vcmFjbGUtVXNlcklk').decode('utf-8')
lab_header_authid = base64.b64decode(b'WC1PcmFjbGUtSWRlbnRpdHlTZXJ2aWNlR3VpZA==').decode('utf-8')
lab_header_authvalue = base64.b64decode(b'aWRjcy03NWVjYThkZGU5NTg0MWQzYTYyMjVhZjMxMjgyMTA0Yw==').decode('utf-8')

post_json = {"name":"modify_service_properties", "options":[{"key":"name", "value":"CECSAUTO"},{"key":"category", "value":"OrderProcessingInfo"},{"key":"property_name", "value":"allow_refresh_entitlement"}, {"key":"property_value", "value":"N"}]}
github_test_url = 'https://github.com/timeline.json'
github_test_rep_url = 'https://api.github.com/user/repos'

mail_from = '3411379@qq.com'  
mail_to = '3411379@qq.com' 
mail_pass='qatxubywfazgbhej' 
  
 
def sendmail():    
    msg_from=mail_from                                 
    passwd=mail_pass                                
    msg_to=mail_to                                
    subject="python"
    content="test"
    msg = MIMEText(content)
    msg['Subject'] = subject
    msg['From'] = msg_from
    msg['To'] = msg_to
    server = smtplib.SMTP_SSL("smtp.qq.com",465)
    server.set_debuglevel(1)
    server.ehlo()
    #server.starttls()
    server.login(msg_from, passwd)
    server.sendmail(msg_from, msg_to, msg.as_string())
    server.quit()