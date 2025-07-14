import smtplib
import re
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os

smtp_server = "smtp.gmail.com"
smtp_port = 587

username = "kodudhulapoojitha19@gmail.com"
password = "uxxl hsok cklp ysla"

from_email = username

x = True
while x:
  pattern = re.compile(r'^[A-Za-z ]+')
  text = input("Enter Name: ")
  matches = pattern.fullmatch(text)
  if matches != None:
    name = matches.group()
    x = False
  else:
    print("Enter Name in correct format")

x = True
while x:
  pattern = re.compile(r'\d{2}-\d{2}-\d{4}')
  dob1 = input("Enter Date of Birth: ")
  matches = pattern.fullmatch(dob1)
  if matches != None:
    dob = matches.group()
    x = False
  else:
    print("Enter DOB in correct format")

x = True
while x:
  pattern = re.compile(r'^[6789]\d{2}-\d{3}-\d{4}')
  phone1 = input("Enter Mobile Number: ")
  matches = pattern.fullmatch(phone1)
  if matches != None:
    phone = matches.group()
    x = False
  else:
    print("Enter Mobile in correct format")

insta = input("Enter Insta Id: ")

x = True
while x:
  pattern = re.compile(r'^[a-zA-Z0-9]*+@gmail.com\Z')
  email1 = input("Enter Email: ")
  matches = pattern.fullmatch(email1)
  if matches != None:
    email = matches.group()
    x = False
  else:
    print("Enter Email in correct format")

to_email = email
subject = f"Details of {name}"
body = f"Name: {name}\nDate of Birth: {dob}\nMobile No: {phone}\nInstagram ID: {insta}\nEmail: {email}"

msg = MIMEMultipart()
msg['From'] = from_email
msg['To'] = to_email
msg['Subject'] = subject
msg.attach(MIMEText(body, 'plain'))

server=smtplib.SMTP(smtp_server,smtp_port)
server.starttls()
server.login(username,password)
server.send_message(msg)
server.quit()

print("Email sent successfully")
