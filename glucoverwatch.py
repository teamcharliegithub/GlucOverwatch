from pydexcom import Dexcom
from twilio.rest import Client
import time

# Dexcom Tokens
username = "brmotta"
pwd = "3Ko17%g4395zxvI8B8TX"  # Password omitted in repository
dexcom = Dexcom(username, pwd)

# Twilio Tokens
account_sid = "AC5e7d47d2b8bfc7c808eba55c706d0d5e"
auth_token = "" # Token omitted in repository
client = Client(account_sid, auth_token)

def update():
    bg = dexcom.get_current_glucose_reading()
    value = bg.value
    trend = bg.trend
    return bg, value, trend
bg, value, trend = update()

while True:
    if (value <= 70):
        # Twilio Code Here
        pass
    elif (value <= 120 and trend == 7):
        # Twilio Code Here
        pass
    elif (value <= 100 and (trend == 6 or trend == 7)):
          # Twilio Code Here
          pass
    else:
        pass
    time.sleep(360)
    bg, value, trend = update()
