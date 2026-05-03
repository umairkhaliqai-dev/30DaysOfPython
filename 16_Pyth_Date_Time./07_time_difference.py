# To find the difference between two datetime or date objects, simply subtract them. The result is a timedelta object that shows the duration.

from datetime import datetime

start = datetime(2026, 5, 1, 9, 0, 0)
end = datetime(2026, 5, 3, 17, 30, 0)

difference = end - start
print("Difference:", difference)  # Output: 2 days, 8:30:00
print("Total seconds:", difference.total_seconds())