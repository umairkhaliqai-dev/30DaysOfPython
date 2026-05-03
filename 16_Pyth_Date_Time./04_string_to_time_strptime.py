# The strptime() method (string parse time) parses a string representing a time/date and returns a datetime object. You must provide the format of the input string.
from datetime import datetime

date_string = "03-05-2026 14:30:00"
parsed_date = datetime.strptime(date_string, "%d-%m-%Y %H:%M:%S")
print("Parsed datetime object:", parsed_date)
print("Type:", type(parsed_date))