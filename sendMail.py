from email.mime.text import MIMEText
import smtplib,os
from email.mime.multipart import MIMEMultipart
import ConfigParser
Config = ConfigParser.ConfigParser()
dirname=os.getcwd()


filename = dirname+'/config.cfg'
Config.read(filename)


class sendMail:
 def mail(self,n):
    fromaddr =Config.get("mail", "fromaddr")
    toaddr=Config.get("mail", "toaddr")
    msg = MIMEMultipart()
    msg[ 'From' ] = fromaddr
    msg[ 'To' ] = toaddr
    msg[ 'Subject' ] = "Error"

    body = str(n)
    msg.attach(MIMEText(body, 'plain'))

    #server = smtplib.SMTP('smtp.office365.com', 587)
    server=smtplib.SMTP('localhost')
    #server.starttls()
    #server.login("antara.ray@mavs.uta.edu", "*********")
    text = msg.as_string()
    server.sendmail(msg[ 'From' ],msg[ 'To' ].split(","), text)
    server.quit()