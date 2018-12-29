'''
Created on Dec 28, 2018

@author: chenz
'''
import smtplib
from email.mime.text import MIMEText
import socks

#socks.setdefaultproxy(socks.SOCKS5, 'www-proxy.idc.oracle.com', 80)
#socks.wrapmodule(smtplib)
#https://www.cnblogs.com/lovealways/p/6701662.html

msg_from='3411379@qq.com'                                
passwd='qatxubywfazgbhej'                                   
msg_to='3411379@qq.com'                                 
                            
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