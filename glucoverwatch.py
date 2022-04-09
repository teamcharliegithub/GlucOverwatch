# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 12:43:00 2022

@author: attom
"""

from pydexcom import Dexcom
from twilio.rest import Client
import time
from decouple import config 
from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse

# Dexcom Tokens
username = "brmotta"
pwd = config('SECRET_KEY1')
dexcom = Dexcom(username, pwd)

patient="+15403517337"
caregiver="+12397383662"
sender="+17752389510"

# Flask application
app = Flask(__name__)



# Twilio Tokens
account_sid = "AC5e7d47d2b8bfc7c808eba55c706d0d5e"
auth_token = config('SECRET_KEY2')
client = Client(account_sid, auth_token) 

def update():
    bg = dexcom.get_current_glucose_reading()
    value = bg.value
    trend = bg.trend
    return bg, value, trend
bg, value, trend = update()
print(value)


while True:
    if (value <= 70):
        message = client.messages.create(to=patient, from_=sender, body="Your blood glucose is 70 or below. Reply YES to confirm treatment or reply NO to summon aid from your caregiver.")
        @app.route("/sms", methods=['GET', 'POST'])

        def incoming_sms(): 
            """Send a dynamic reply to an incoming text message"""

            # Get the message the user sent our Twilio number
            body = request.values.get('Body', None)
            # Start our TwiML response
            resp = MessagingResponse()
            
            if (body == 'YES'):
                resp.message("Thank you for confirming. Your caregiver will be notified.")
            elif body == "NO":
                resp.message("Help is on the way. Your caregiver has been summoned to aid you.")
                message = client.messages.create(to=caregiver, from_=sender, body='Your patient has a low blood glucose and requires immediate assistance. Please respond as quickly as possible.')
            elif body != 'YES' or body != 'NO':
                    resp.message("Your response was not processed. Please confirm treatment or summon aid.")

        if __name__ == "__main__":
            app.run(debug=True)
    time.sleep(360)
    bg, value, trend = update()


