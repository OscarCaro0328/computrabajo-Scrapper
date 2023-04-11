import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os

email_password =os.environ.get('gmail_password') #clave creada por la aplicacion
smtp_port=587
smtp_server= 'smtp.gmail.com'
email_sender ='ingenieros.caroni@gmail.com'


#Send email with no attachment
def send_email(email_receiver_list: list[str], subject: str, body:str):
    
    for person in email_receiver_list:
    
        try:
            # Create the message object
            msg = MIMEMultipart()
            msg['From'] = email_sender
            msg['To'] = person
            msg['Subject'] = subject

            # Add the message body
            msg.attach(MIMEText(body, 'plain'))

            # Connect to the SMTP server and send the message
            TIE_server = smtplib.SMTP(smtp_server, smtp_port)
            TIE_server.starttls()
            TIE_server.login(email_sender, email_password)

            # Send the actual email
            print()
            print(f"Sending email to - {person}")
            TIE_server.sendmail(email_sender, person, msg.as_string())
            print(f"Email successfully sent to - {person}")
            print()
        
        except Exception as e:
            print(e)# If there's an error, print it out

        # Close the port
    TIE_server.quit()


#Send email with attachment to a list os people
def send_email_attach(email_receiver_list: list[str], subject: str, body:str, attachment_filename:str):

    for person in email_receiver_list:
        try: 
            msg = MIMEMultipart()
            msg['From']= email_sender
            msg['To']=person
            msg['Subject']= subject
            msg.attach(MIMEText(body, 'plain'))

            #open the file 
            attachment = open(attachment_filename, 'rb') #r is for read and b is for binary

            #Encode as base 64
            attachment_package = MIMEBase('application', 'octet-stream')
            attachment_package.set_payload((attachment).read())
            encoders.encode_base64(attachment_package)
            attachment_package.add_header('Content-Disposition', 'attachment; filename= '+ attachment_filename)
            msg.attach(attachment_package)

            #cast as a string
            text =msg.as_string()

            #connect to server
            print("Connecting to server...")
            TIE_server = smtplib.SMTP(smtp_server, smtp_port)
            TIE_server.starttls()
            TIE_server.login(email_sender, email_password)
            print("Connected to server :-)")
            print()

            # Send the actual email
            print()
            print(f"Sending email to - {person}")
            TIE_server.sendmail(email_sender, person, text)
            print(f"Email successfully sent to - {person}")
            print()
        except Exception as e:
            print("exception raised:", e)
    TIE_server.quit()


