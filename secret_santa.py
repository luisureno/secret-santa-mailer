from dotenv import load_dotenv
import os
import random
import smtplib
import ssl

load_dotenv()

def send_email(sender, receiver, recipient):
    password = os.environ['password']
    body_msg = f'''\
From: {sender}
Subject: Your Secret Santa Present

Hi! Your secret santa is {recipient}!
Remember to spend $50 on your gift, but don't s
'''
    