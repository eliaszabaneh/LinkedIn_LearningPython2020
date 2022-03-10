#
# Example file for working with timedelta objects
#

from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta

# construct a basic timedelta and print it
print(timedelta(days=365, hours=5, minutes=1))
now = datetime.now()
print("today's date is: " + str(now))
print("One year from now it will be: " + str(now + timedelta(days=365)))

# print today's date
print("In 2 days and 3 weeks it will be " + str(now + timedelta(days=2, weeks=3)))

# print today's date one year from now

# create a timedelta that uses more than one argument


# calculate the date 1 week ago, formatted as a string

t = datetime.now() - timedelta(weeks=1)
s = t.strftime("%A %B %d, %Y")
print("One week ago it was " + s)

### How many days until April Fools' Day?
today = date.today()
afd = date(today.year, 4, 1)
if afd < today:
    print("April Fool's day already went by %d days ago" % (today - afd).days)
    afd = afd.replace(year=today.year + 1)
time_to_afd = afd - today
print("It's just", time_to_afd.days, "days to April Fool's day")
# use date comparison to see if April Fool's has already gone for this year
# if it has, use the replace() function to get the date for next year


# Now calculate the amount of time until April Fool's Day
