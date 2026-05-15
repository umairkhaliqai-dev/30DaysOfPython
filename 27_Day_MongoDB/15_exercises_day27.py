# ============================================================
# Day 27 - Topic 15: Exercises
# ============================================================
#
# This file runs all 5 exercises in sequence.
# Each exercise builds on the previous one.
#
# Exercise 1: Insert students
# Exercise 2: Find and filter
# Exercise 3: Sort and limit
# Exercise 4: Update
# Exercise 5: Delete and drop
#
# ============================================================

import os
from dotenv import load_dotenv
from pymongo import MongoClient, ASCENDING

load_dotenv()
client = MongoClient(os.getenv("MONGO_URI"))
db = client["thirty_days_python"]
students = db["exercise_students"]  # separate collection for exercises

# Clean start
students.delete_many({})
print("=" * 50)
print("DAY 27 EXERCISES")
print("=" * 50)

# -------------------------------------------------------
# Exercise 1: Insert at least 5 students
# -------------------------------------------------------
print("\n📝 Exercise 1: Inserting students...")

students.insert_many([
    {"name": "Alice",  "country": "UK",      "city": "London",     "age": 22, "skills": ["Python", "MongoDB"]},
    {"name": "Bob",    "country": "USA",      "city": "New York",   "age": 25, "skills": ["JavaScript", "React"]},
    {"name": "Carol",  "country": "Germany",  "city": "Berlin",     "age": 21, "skills": ["Python", "Flask"]},
    {"name": "David",  "country": "India",    "city": "Mumbai",     "age": 23, "skills": ["Java", "Spring"]},
    {"name": "Eve",    "country": "UK",       "city": "Manchester", "age": 20, "skills": ["Python", "Django"]},
])
print(f"✅ Inserted {students.count_documents({})} students")

# -------------------------------------------------------
# Exercise 2: Find all students from the UK
# -------------------------------------------------------
print("\n📝 Exercise 2: UK students...")
for s in students.find({"country": "UK"}):
    print(f"  {s['name']} - {s['city']}")

# -------------------------------------------------------
# Exercise 3: 3 youngest students sorted by age
# -------------------------------------------------------
print("\n📝 Exercise 3: 3 youngest students...")
for s in students.find().sort("age", ASCENDING).limit(3):
    print(f"  {s['name']} - age {s['age']}")

# -------------------------------------------------------
# Exercise 4: Update — mark students over 22 as senior
# -------------------------------------------------------
print("\n📝 Exercise 4: Mark seniors (age > 22)...")
result = students.update_many(
    {"age": {"$gt": 22}},
    {"$set": {"senior": True}}
)
print(f"  ✅ {result.modified_count} students marked as senior")

# -------------------------------------------------------
# Exercise 5: Delete students under 21, then drop collection
# -------------------------------------------------------
print("\n📝 Exercise 5: Delete under-21s and drop collection...")
result = students.delete_many({"age": {"$lt": 21}})
print(f"  Deleted {result.deleted_count} student(s) under 21")
print(f"  Remaining: {students.count_documents({})}")

students.drop()
print("  ✅ Collection dropped!")
print("  Collections left:", db.list_collection_names())

print("\n🎉 All Day 27 exercises complete!")
