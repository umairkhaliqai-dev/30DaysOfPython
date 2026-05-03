# The time class represents time (hour, minute, second, microsecond) independent of any particular day. It is useful for storing or comparing times.


from datetime import time

# Create a time object
meeting_time = time(14, 30, 0)  # 2:30 PM
print("Meeting at:", meeting_time)

print("Hour:", meeting_time.hour)
print("Minute:", meeting_time.minute)