from pydexcom import Dexcom
import time
username = "brmotta"
pwd = ""  # Password omitted in repository
dexcom = Dexcom(username, pwd)

bg = dexcom.get_current_glucose_reading()
trend = bg.trend

while True:
    if (bg <= 70):
        # Twilio Code Here
    elif (bg <= 120 and trend == 7):
        # Twilio Code Here
    elif (bg <= 100 and (trend == 6 or trend == 7):
          # Twilio Code Here
    else:
    time.sleep(360)
    bg = dexcom.getcurrent_glucose_reading()
    trend = bg.trend

