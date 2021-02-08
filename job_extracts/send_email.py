#send email

#### Where ever you see python comments, is what you should change. IF it doesnt contain a python comment do not change!!!

import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders
from datetime import datetime
from jobextracts import job_extraction



def extract_send():

    job_extraction()
    
    reporting_day = datetime.strftime(datetime.now(), '%d/%m/%Y')
    
    
    #####################Send Email ########################
    fromaddr="yonis838@googlemail.com" #Person sending in the email. 
    sendto =['yonis838@googlemail.com','yakubmohamoud@honeycomb-technology.co.uk'] #List of email address you will be sending the email to
    password = 'odqhescsdicrxbdx' #create an APP Password with Google 
    
    
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['Bcc'] = ', '.join(sendto) #Feel free to change to change BCC to CC or To. 
    msg['Subject'] = "reporting_day Reed API extract - Developer Roles".replace("reporting_day", reporting_day)# The email subect line
    
    body = """
    Hello Everyone, 
    
    Please see attached document for the latest Developers role picked up from the Reed API. 
    
    If you find that the spreadsheet contains any recruitment company, please let me know so they can be blacklisted.
    
    
    With Regards,
    
    Yonis Mohamoud
    
    """ # The body of the email, write whatever you like
    
    
    msg.attach(MIMEText(body, 'plain'))
    
    filename = 'spreadsheets/Developer.csv' # This is the name you will give your new attached document 
    attachment = open(filename, 'rb') # add in the filepath and filename of the file you want to attach
    
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