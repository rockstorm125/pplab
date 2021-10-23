#PROGRAM 4
import pytz
from datetime import datetime
now = datetime.now(pytz.timezone("Asia/Kolkata"))
print (now.strftime('%a %B %d %I:%M:%S %Z %Y'))
