
from pydexcom import Dexcom
import time
username = "brmotta"
pwd = ""  # Password omitted in repository
dexcom = Dexcom(username, pwd)

def update():
    bg = dexcom.get_current_glucose_reading()
    value = bg.value
    trend = bg.trend
    return bg, value, trend
bg, value, trend = update()

while True:
    if (bg <= 70):
        # Twilio Code Here
        pass
    elif (bg <= 120 and trend == 7):
        # Twilio Code Here
        pass
    elif (bg <= 100 and (trend == 6 or trend == 7)):
          # Twilio Code Here
          pass
    else:
        pass
    time.sleep(360)
    bg, value, trend = update()
