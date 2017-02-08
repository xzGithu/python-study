#!/usr/bin/env python



import time,datetime

def get_week_day(dates):
    week_day_dict = {
        0 : 'Monday',
        1 : 'Tuesday',
        2 : 'Wednesday',
        3 : 'Thursday',
        4 : 'Firday',
        5 : 'Saturday',
        6 : 'Sunday',
    }

    day = dayday.weekday()
    return week_day_dict[day]

date = raw_input("Please input your date,and seperate by one Space:").split(' ')
#print date
dayday = datetime.date(int(date[0]),int(date[1]),int(date[2]))
print "Today is %s" %dayday.strftime('%A')
print "Today is the %s day of this week" %dayday.strftime('%w')
print "Today is the %s day of this year" %dayday.strftime('%j')
print "Today is the %s week of this year" %dayday.strftime('%U')
print get_week_day(dayday)
