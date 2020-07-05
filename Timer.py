import time

year, month, date, hour, minute, second, day, day2, isdst = time.gmtime()

daydict= {0:"Monday", 1:"Tuesday,", 2:"Wednesday", 3:"Thursday", 4:"Friday", 5:"Saturday", 6:"Sunday"}
mondict= {0:'January', 1:'Feburary',2:'March', 3:'April',4:'May', 5:'June',6:'July ', 7:'August',8:'September', 9:'October',10:'November', 11:'December'}
hour_here=hour-5
if second<10:
    add_zero_sec=0
else:
    add_zero_sec=""

if minute<10:
    add_zero_min="0"
else:
    add_zero_min=""
print(daydict[day], mondict[month-1], date, str(hour_here)+":"+add_zero_min+str(minute)+":"+str(add_zero_sec)+str(second), year)

time.sleep(4)
print(time.asctime())
print(time.ctime())
