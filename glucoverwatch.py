from pydexcom import Dexcom
from decouple import config
import time

username = "brmotta"
pwd = config('SECRET_KEY')  # Password omitted in repository
dexcom = Dexcom(username, pwd)


def update():
    bg = dexcom.get_current_glucose_reading()
    value = bg.value
    trend = bg.trend
    return bg, value, trend


bg, value, trend = update()
print(bg.value)

while True:
    if (bg.value <= 70):
        # Twilio Code Here
        pass
    elif (bg.value <= 120 and trend == 7):
        # Twilio Code Here
        pass
    elif (bg.value <= 100 and (trend == 6 or trend == 7)):
        # Twilio Code Here
        pass
    else:
        pass
    time.sleep(360)
    bg, value, trend = update()
