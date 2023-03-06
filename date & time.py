
from datetime import datetime
today = datetime.today()
d1 = today.strftime("%d/%m/%Y")
print("Current Date and Time is:")
print("date =", d1)
now = datetime.now()
dt_string = now.strftime("%H:%M:%S")
print("time =", dt_string)