# good morning sir 

import time
hour = time.localtime().tm_hour
minute = time.localtime().tm_min

time = float(str(hour)+ '.' +str(minute))

print(hour , minute)


if( time > 3.00 and time<12.00 ):
    print("Good morning sir")
elif(time>=12.00 and time <=16.00):
    print("Good afternoon sir")
elif(time>16.00 and time<20.00):
    print("Good evening sir")
else:
    print("Have a good night sir")
