import datetime
import calendar
  
def findDay(date):
    born = datetime.datetime.strptime(date, '%m %d %Y').weekday()
    return (calendar.day_name[born])
  
date = input()
day = findDay(date)
print(day.upper())