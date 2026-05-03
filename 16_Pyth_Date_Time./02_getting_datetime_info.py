# You can extract specific components (year, month, day, hour, minute, second, microsecond) from a datetime object using its attributes.


from datetime import datetime

now = datetime.now()
print("Year:", now.year)
print("Month:", now.month)
print("Day:", now.day)
print("Hour:", now.hour)
print("Minute:", now.minute)
print("Second:", now.second)