from pydexcom import Dexcom
import time
username = "brmotta"
pwd = ""  # Password omitted in repository
dexcom = Dexcom(username, pwd)

bg = dexcom.get_current_glucose_reading()
