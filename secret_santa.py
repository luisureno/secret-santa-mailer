from dotenv import load_dotenv
import os
import random
import smtplib
import ssl

load_dotenv()

def send_email(sender, receiver, recipient):
    #'password' is grabbing the password from our .env file
    password = os.environ['password']
    #the msg template that will be sent over to the reciever
    body_msg = f'''\
From: {sender}
Subject: Your Secret Santa Present

Hi! Your secret santa is {recipient}!
Remember to spend $50 on your gift, but don't s
'''
    #this creates a secure, encrypted connection set up
    context = ssl.create_default_context()
    #this means connect to the gmail email server using SSL to secure it
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context = context) as server:
        server.login(sender, password)
        server.sendmail(sender, receiver, body_msg)

names_list = ['Luis', 'Angel', 'Erica', 'Elav']
#this initializes the names and emails of our recipients
names_and_emails = [

    ['Luis', 'luis_ureno@yahoo.com'],
    ['Angel', 'totoureno@yahoo.com'],
    ['Erica', 'emtnz@sbcglobal.net'],
    ['Elav', 'info@elegantlavs.com']
]


#this checks to make sure that there are more than 2 people in the list
#else the program can not run
if len(names_list) <= 1:
    print('Not enough people to start a secret santa!')
    quit()
random.shuffle(names_and_emails)    
#this variable is important because it will make sure the last person
#in the list has someone to gift to
first_name = names_and_emails[0][0]

while len(names_and_emails) > 1:
    send_email('luisangelureno17@gmail.com', names_and_emails[0][1], names_and_emails[1][0])
    #this removes the first person from the list bc this was the person
    #who just got assigned a match
    names_and_emails.pop(0)
    #this will randomize the list again for the next match
    random.shuffle(names_and_emails)
#before the loop ends, one person is left in which they then 
#get selected the first person
send_email('luisangelureno17@gmail.com', names_and_emails[0][1], first_name)
