import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders
from datetime import datetime
import os


def send_msg(fullname, email, message):
    
    reporting_day = datetime.strftime(datetime.now(), '%d/%m/%Y')
    
    
    #####################Send Email ########################
    fromaddr= "yonis838@googlemail.com" #Person sending in the email. 
    sendto =['yonis838@googlemail.com','yakubmohamoud@honeycomb-technology.co.uk'] #List of email address you will be sending the email to
    password = os.environ['password'] #create an APP Password with Google 
    
    
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['Bcc'] = ', '.join(sendto) #Feel free to change to change BCC to CC or To. 
    msg['Subject'] = "Query from Honeycomb Website"
    
    body = "Fullname = " + fullname + "\n\nemail address = " + email + "\n\nMessage = " + message
    
    
    msg.attach(MIMEText(body, 'plain'))
    
    part = MIMEBase('application', "octet-stream")
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename= %s' % filename)
    
    msg.attach(part)
    
    
    try:
        smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
        smtpObj.ehlo()
        smtpObj.starttls()
        smtpObj.login(fromaddr, password)
    
        text = msg.as_string()
        smtpObj.sendmail(fromaddr, sendto , text)
        smtpObj.quit()
        print("Success")
    except Exception as e:
        print(e)