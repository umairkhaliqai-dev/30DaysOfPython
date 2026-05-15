# ============================================================
# Day 27 - Topic 11: Find with Sort
# ============================================================
#
# .sort(field, direction) orders your results.
#
#   ASCENDING  (1)  → smallest to largest / A to Z
#   DESCENDING (-1) → largest to smallest / Z to A
#
# Single field:
#   collection.find().sort("age", ASCENDING)
#
# Multiple fields (list of tuples):
#   collection.find().sort([("grade", ASCENDING), ("age", DESCENDING)])
#
# ============================================================

import os
from dotenv import load_dotenv
from pymongo import MongoClient, ASCENDING, DESCENDING

load_dotenv()
client = MongoClient(os.getenv("MONGO_URI"))
db = client["thirty_days_python"]
students = db["students"]

# --- Sort by age ascending (youngest first) ---
print("=== Sorted by age ASCENDING ===")
for s in students.find().sort("age", ASCENDING):
    print(s["name"], "-", s["age"])

# --- Sort by name descending (Z to A) ---
print("\n=== Sorted by name DESCENDING ===")
for s in students.find().sort("name", DESCENDING):
    print(s["name"])

# --- Sort by grade ASC then age DESC ---
print("\n=== Sorted by grade ASC, then age DESC ===")
for s in students.find().sort([("grade", ASCENDING), ("age", DESCENDING)]):
    print(s["name"], "| grade:", s["grade"], "| age:", s["age"])

# ============================================================
# NOTE: Run 06_inserting_many_documents.py first to have data
# ============================================================
