# timedelta represents a duration (the difference between two dates or times). You can also create a timedelta manually to add or subtract from a datetime/date object.


from datetime import datetime, timedelta

today = datetime.now()
print("Today:", today)

# Create a duration of 5 days
duration = timedelta(days=5, hours=3)
future_date = today + duration
print("After 5 days and 3 hours:", future_date)

# Subtract 2 weeks
two_weeks = timedelta(weeks=2)
past_date = today - two_weeks
print("Two weeks ago:", past_date)