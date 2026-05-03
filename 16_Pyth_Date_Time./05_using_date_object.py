# The date class (inside the datetime module) deals exclusively with dates (year, month, day) without time components. You can create a date object or extract the date part from a datetime object.


from datetime import date

# Create a specific date
independence_day = date(1947, 8, 15)
print("Independence Day:", independence_day)

# Get today's date
today = date.today()
print("Today's date:", today)