# ============================================================
# Day 27 - Topic 07: MongoDB Find
# ============================================================
#
# Two main methods to read documents:
#
#   find_one()  → returns the FIRST matching document (as a dict)
#   find()      → returns a Cursor (iterable) of ALL matching docs
#
# Calling find() with NO arguments returns ALL documents.
# A Cursor is like a generator — loop over it or wrap with list().
#
# ============================================================

import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()
client = MongoClient(os.getenv("MONGO_URI"))
db = client["thirty_days_python"]
students = db["students"]

# --- find_one() ---
print("=== find_one() ===")
first = students.find_one()
print("First document:", first)

# --- find() all documents ---
print("\n=== find() all documents ===")
all_students = students.find()   # returns a Cursor object
for student in all_students:
    print(student)

# --- Convert cursor to a list ---
print("\n=== find() as a list ===")
students_list = list(students.find())
print("Total:", len(students_list))
print("First item from list:", students_list[0])

# --- find() with projection (choose which fields to show) ---
# 1 = include field, 0 = exclude field
print("\n=== find() with projection (name and grade only) ===")
for s in students.find({}, {"_id": 0, "name": 1, "grade": 1}):
    print(s)

# ============================================================
# To run:
#   python 07_mongodb_find.py
#
# REQUIRES: Run 06_inserting_many_documents.py first
#           so there is data in the collection.
# ============================================================
