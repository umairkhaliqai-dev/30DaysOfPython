# ============================================================
# Day 27 - Topic 10: Limiting Documents
# ============================================================
#
# .limit(n) restricts how many documents are returned.
# Very useful for pagination or just previewing data.
#
#   collection.find().limit(n)
#
# You can combine it with a query filter too:
#   collection.find({"grade": "A"}).limit(2)
#
# ============================================================

import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()
client = MongoClient(os.getenv("MONGO_URI"))
db = client["thirty_days_python"]
students = db["students"]

# --- Get only first 2 students ---
print("=== First 2 students ===")
for s in students.find().limit(2):
    print(s["name"])

# --- Limit with a filter ---
print("\n=== First 2 grade-A students ===")
for s in students.find({"grade": "A"}).limit(2):
    print(s["name"], "-", s["grade"])

# --- Total count vs limited ---
total = students.count_documents({})
print(f"\nTotal students in DB : {total}")
print(f"Showing with limit(2): 2")

# ============================================================
# NOTE: Run 06_inserting_many_documents.py first to have data
# ============================================================
