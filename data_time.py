# importing datetime module
import datetime
 
# assigned unix time
unix_time = 1691089993
 
date_time = datetime.datetime.fromtimestamp(unix_time)
 
# print unix time stamp
print("Unix_Time =>",unix_time)
 
# displaying date and time in a regular
# string format
print("Date & Time =>" ,
      datetime.datetime.fromtimestamp(unix_time).strftime('%Y-%m-%d %H:%M:%S'))