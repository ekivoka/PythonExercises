# put your python code her
import datetime
year, month, day = input().split(' ')
year, month, day = int(year), int(month), int(day)
days = int(input())

mydate = datetime.date(year, month,day)
d = datetime.timedelta(days=days)
mydate += d
print(mydate.year,mydate.month,mydate.day)
