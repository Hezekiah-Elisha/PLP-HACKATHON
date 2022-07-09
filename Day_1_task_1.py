from datetime import date, datetime

date = date.today()
dateTime = datetime.now()
# print(date)
day = date.strftime('%A')

dayShort = day[:3].title()

if dayShort == 'Mon' or dayShort == 'Tue' or dayShort == 'Wed' or \
    dayShort == 'Wed' or dayShort == 'Thu' or dayShort == 'Fri':
  fare = 100
elif dayShort == 'Sat':
  fare = 60
else:
  fare = 80

print(f"Date: {date}")
print(f"Day: {dayShort}")
print(f"Fare: {fare}")
