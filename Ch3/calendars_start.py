#
# Example file for working with Calendars
#

# import the calendar module
import calendar
import datetime
from datetime import date

# create a plain text calendar
cal = calendar.TextCalendar(calendar.SUNDAY)
st = cal.formatmonth(2022, 3, 0, 0)
print(st)

# create an HTML formatted calendar
# hc = calendar.HTMLCalendar(calendar.MONDAY)
# ss = hc.formatmonth(2022,6,0)
# print(ss)

# loop over the days of a month
# # zeroes mean that the day of the week is in an overlapping month
# for i in cal.itermonthdays(2022, 3):
#     print(i)

# The Calendar module provides useful utilities for the given locale,
# such as the names of days and months in both full and abbreviated forms
# for name in calendar.month_name:
#     print(name)
#
# for day in calendar.day_name:
#     print(day)

# Calculate days based on a rule: For example, consider
# a team meeting on the first Friday of every month.
# To figure out what days that would be for each month,
# we can use this script:
# print("Team meeting will be on")
# for m in range(1, 13):
#     cal = calendar.monthcalendar(2022, m)
#     weekone = cal[0]
#     weektwo = cal[1]
#
#     if weekone[calendar.FRIDAY] != 0:
#         meetday = weekone[calendar.FRIDAY]
#     else:
#         meetday = weektwo[calendar.FRIDAY]
#     # print("%10s %2d" % (calendar.month_name[m], meetday))
#     print("%10s %2d" % (calendar.month_name[m], meetday))

print("*****************************")
# for m in range(1, 13):
#     cal = calendar.TextCalendar(calendar.SUNDAY)
#     print(cal.formatmonth(2022,m,0,0))
#
# today = date.today()
# days = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
# print("tomorrow's day will be ",days[(today.weekday()+1)%7])
today = date.today()
print(today)
# tomorrow=date(today.year,today.month,today.day+1)