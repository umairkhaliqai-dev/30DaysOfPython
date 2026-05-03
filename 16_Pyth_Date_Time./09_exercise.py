from datetime import datetime, date, time, timedelta

# 1. Get the current day, month, year, hour, minute and timestamp
now = datetime.now()
print("=" * 50)
print("1. CURRENT DATE & TIME INFORMATION")
print("=" * 50)
print(f"Current Day: {now.day}")
print(f"Current Month: {now.month}")
print(f"Current Year: {now.year}")
print(f"Current Hour: {now.hour}")
print(f"Current Minute: {now.minute}")
print(f"Current Second: {now.second}")
print(f"Timestamp (seconds since epoch): {now.timestamp()}")

# 2. Format the current date using: "%m/%d/%Y, %H:%M:%S"
print("\n" + "=" * 50)
print("2. FORMATTED CURRENT DATE")
print("=" * 50)
formatted_date = now.strftime("%m/%d/%Y, %H:%M:%S")
print(f"Formatted Date: {formatted_date}")

# 3. Convert "Today is 5 December, 2019" to time
print("\n" + "=" * 50)
print("3. STRING TO TIME CONVERSION")
print("=" * 50)
date_string = "5 December, 2019"
converted_date = datetime.strptime(date_string, "%d %B, %Y")
print(f"Original String: {date_string}")
print(f"Converted to datetime: {converted_date}")
print(f"Type: {type(converted_date)}")

# 4. Calculate time difference between now and new year
print("\n" + "=" * 50)
print("4. TIME DIFFERENCE: NOW vs NEW YEAR")
print("=" * 50)
new_year = datetime(now.year + 1, 1, 1, 0, 0, 0)
time_to_new_year = new_year - now
print(f"Current Date: {now}")
print(f"New Year {now.year + 1}: {new_year}")
print(f"Time remaining until New Year: {time_to_new_year}")
print(f"Days remaining: {time_to_new_year.days} days")
print(f"Total hours remaining: {time_to_new_year.total_seconds() / 3600:.2f} hours")

# 5. Calculate time difference between 1 January 1970 and now
print("\n" + "=" * 50)
print("5. TIME DIFFERENCE: UNIX EPOCH (1970-01-01) vs NOW")
print("=" * 50)
epoch = datetime(1970, 1, 1, 0, 0, 0)
time_since_epoch = now - epoch
print(f"Unix Epoch: {epoch}")
print(f"Current Date: {now}")
print(f"Time since epoch: {time_since_epoch}")
print(f"Total days: {time_since_epoch.days} days")
print(f"Total seconds: {time_since_epoch.total_seconds():.0f} seconds")
print(f"Total years: {time_since_epoch.days / 365.25:.2f} years")

# Bonus: Show timestamp for epoch
print(f"\nTimestamp for epoch (1970-01-01): {datetime(1970, 1, 1).timestamp()}")

# 6. Practical applications of datetime module
print("\n" + "=" * 50)
print("6. PRACTICAL APPLICATIONS OF DATETIME MODULE")
print("=" * 50)

applications = {
    "1. Time Series Analysis": [
        "Stock market price analysis over time",
        "Weather data tracking and forecasting",
        "Sales trend analysis by month/year",
        "Sensor data logging in IoT applications"
    ],
    
    "2. Activity Timestamp Logging": [
        "User login/logout tracking in web apps",
        "File modification and access times",
        "Database record creation/update timestamps",
        "System event logging and debugging"
    ],
    
    "3. Blog & Content Management": [
        "Post publication dates and scheduling",
        "Comment timestamps and moderation",
        "Content version control and editing history",
        "Archive posts by month/year"
    ],
    
    "4. Additional Real-world Uses": [
        "Age calculation (birthdays, eligibility)",
        "Countdown timers and reminders",
        "Expiration date checking (subscriptions, certificates)",
        "Scheduling automated tasks (cron jobs)",
        "Calculating time differences in project management",
        "Generating unique IDs based on timestamps",
        "Data partitioning and time-based sharding in databases",
        "Generating reports for specific time periods"
    ]
}

for category, examples in applications.items():
    print(f"\n{category}:")
    for example in examples:
        print(f"  • {example}")

# Bonus Example: Blog Post System
print("\n" + "=" * 50)
print("BONUS: SIMPLE BLOG POST EXAMPLE")
print("=" * 50)

class BlogPost:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
    
    def update_content(self, new_content):
        self.content = new_content
        self.updated_at = datetime.now()
    
    def get_time_since_posted(self):
        time_diff = datetime.now() - self.created_at
        if time_diff.days > 0:
            return f"{time_diff.days} days ago"
        elif time_diff.seconds // 3600 > 0:
            return f"{time_diff.seconds // 3600} hours ago"
        else:
            return f"{time_diff.seconds // 60} minutes ago"
    
    def display_post(self):
        print(f"\n📝 Title: {self.title}")
        print(f"👤 Author: {self.author}")
        print(f"🕒 Posted: {self.get_time_since_posted()}")
        print(f"📅 Created on: {self.created_at.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"📄 Content: {self.content}")

# Create a sample blog post
my_post = BlogPost(
    "Learning Python Datetime",
    "Today I learned how to handle dates and times in Python using the datetime module!",
    "Python Learner"
)

my_post.display_post()

# Simulate updating the post
print("\n--- Updating post content ---")
my_post.update_content("Updated: I now understand strftime, strptime, and timedelta completely!")
my_post.display_post()