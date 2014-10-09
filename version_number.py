#!/anaconda/bin/python
#this is Python 3

import datetime
#Datetime module docs: https://docs.python.org/3/library/datetime.html
#Since I'm ONLY useing Days in this iteration, perhaps I should use datetime.date(birthdate) and datetime.date.today() instead
kojo_bdaySmall = datetime.date(1970, 8, 2)
nowSmall = datetime.date.today()
diffSmall = nowSmall - kojo_bdaySmall
majorMinor = int(diffSmall.days/365.25)
rev = diffSmall.days/365.25 - majorMinor
major = divmod(majorMinor, 10)[0]
minor = divmod(majorMinor, 10)[1]
print (major, minor, rev)

'''
Basic test of version number math
my_age = 23
first = my_age // 10
middle = my_age % 10
'''

##Same problem, but with datetime.datetime for greater granularity. But I'm not using that granularity yet
print()
print("Same problem, but with datetime.datetime for greater granularity.")
bday = datetime.datetime(1970, 8, 2)
now = datetime.datetime.today()
diff = now - bday
#diff = datetime.timedelta(15690, 53290, 67000)
diff
print ("values in 'datetime.timedelta' tuple are, (days, seconds, microseconds)")
print (diff)
print ("diff.days", diff.days)
print ("diff.min", diff.min)
print ("diff.microseconds", diff.microseconds)
majorMinorRev = diff.days/365.25
time_major = divmod(majorMinorRev, 10)[0]
time_minor = divmod(majorMinorRev, 10)[1]
print (time_major, time_minor, rev)

print()
print("Version 3")
now = datetime.datetime.now()
bd = datetime.datetime(1970, 8, 2, 6, 55)
var = now-bd # var is <class 'datetime.timedelta'>
years = var.days/365.25 #major and minor can come from this
sec_per_year = 3600*24*365.25
revision = var.seconds/sec_per_year
print(int(years // 10), ".", int(years % 10), ".", revision)

#In a later iteration, I'll use the minutes & microseconds. At this point I'm making the following simplifying assumptions:
   #Most people won't know their time of birth beyond the date
   #I want to get this working with what I can do now. I'll add granularity later, so it can update 'live' 

#Next step: use the Arrow library to make this work across time zones, or to allow people to use their timezone of birth
print()
print('Version 4: using <a href="http://crsmithdev.com/arrow/">Arrow</a>')
import arrow
utc = arrow.utcnow()
print("The current UTC date and time is", utc)

