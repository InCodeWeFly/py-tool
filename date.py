import datetime

#x = datetime.datetime.utcnow()
x = datetime.datetime.now()


print(x)
print(x.year)
print(x.month)
print(x.day)
print(x.hour)
print(x.minute)
print(x.second)
print(x.microsecond)
print(x.weekday())
print(x.timestamp())
print(x.astimezone())
print(x.timetz())
print(x.strftime("%A"))