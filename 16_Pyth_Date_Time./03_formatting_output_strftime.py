# The strftime() method (string format time) converts a datetime object into a string according to a specified format code (e.g., %Y for 4-digit year, %B for full month name).

from datetime import datetime

now = datetime.now()
formatted = now.strftime("%A, %B %d, %Y - %I:%M %p")
print("Formatted date:", formatted)  # Output: Saturday, May 03, 2026 - 02:15 PM