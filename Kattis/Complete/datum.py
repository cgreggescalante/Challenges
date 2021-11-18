# Datum
import calendar
import datetime

D, M = map(int, input().split())

date = datetime.datetime(2009, M, D)

print(calendar.day_name[date.weekday()])
