#__author:jack
#date 2019-12-11 12:55

import time

#print(help(time))
print(time.time())
print(time.time_ns())
#print(time.clock())
time.sleep(1)

#time.struct_time(tm_year=2019, tm_mon=12, tm_mday=11, tm_hour=5, tm_min=50, tm_sec=21, tm_wday=2, tm_yday=345, tm_isdst=0)
print(time.gmtime())

print(time.localtime())
print(time.asctime())
print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))

#time.struct_time(tm_year=2019, tm_mon=12, tm_mday=11, tm_hour=14, tm_min=3, tm_sec=54, tm_wday=2, tm_yday=345, tm_isdst=-1)
print(time.strptime('2019-12-11 14:03:54','%Y-%m-%d %H:%M:%S'))

print(time.ctime(7200))
print(time.mktime(time.localtime()))


import datetime
print(datetime.datetime.now())