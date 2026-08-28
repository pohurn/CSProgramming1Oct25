
#we need to import the library first
import datetime

# get the current date and time
# now = datetime.datetime.now()

# print(now)
# print(now.year)
# print(now.month)
# print(now.day)
# print(now.hour)
# print(now.second)
# print(now.microsecond)


# you just want today's date

# today = datetime.date.today()
# print(today)

# let's say the user inputs a date of birth
# you want to calculate his age

# year month day
# birthdate = datetime.date(2008,5,15)
# print(birthdate)

# dateToCompare = datetime.date(2002,7,25)

# if birthdate > dateToCompare:
#     print("greater")
# else:
#     print("smaller")


# today = datetime.date.today()

# print(today) #2026-08-27

# 27/08/2026
# 27 August 2026

# in python there is something : strftime
# strftime => string format time

#27/08/2026
# today = datetime.date.today()

# print(today.strftime("%d/%m/%Y"))

# %d - DAY
# %m - MONTH
# %Y - YEAR => 2026
# %y - YEAR => 26
# %M - MINUTE
# %S - SECOND
# %B - MONTH IN FULL
# %b - MONTH IN SHORT
# %A - DAY IN FULL

# now = datetime.datetime.now()
# print(now.strftime("%I:%M%p")) #12 h format 8:04PM
# print(now.strftime("%H %M")) #24 h format 20 04

# # 27 August 2026
# print(today.strftime("%dn%B %Y"))

# # 27 Aug 26
# print(today.strftime("%d %b %y"))

# print(today.strftime("%A, the %d %B %Y"))