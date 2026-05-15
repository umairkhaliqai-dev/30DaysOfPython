# ============================================================
# Day 27 - Topic 08: Find with Query
# ============================================================
#
# Pass a query dictionary to find() or find_one() to filter results.
# This is like a SQL WHERE clause.
#
#   collection.find({"field": "value"})
#
# Only documents where field == value are returned.
# You can filter on any field, including nested fields using
# dot notation: {"address.city": "London"}
#
# ============================================================

import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()
client = MongoClient(os.getenv("MONGO_URI"))
db = client["thirty_days_python"]
students = db["students"]

# --- Find all students with grade "A" ---
print("=== Students with grade A ===")
for s in students.find({"grade": "A"}):
    print(s["name"], "-", s["grade"])

# --- find_one() by name ---
print("\n=== find_one() by name ===")
alice = students.find_one({"name": "Alice"})
print("Found:", alice)

# --- Find by age ---
print("\n=== Students aged 22 ===")
for s in students.find({"age": 22}):
    print(s["name"], s["age"])

# --- Query on nested field (dot notation) ---
# If your documents had an "address.city" field:
# students.find({"address.city": "London"})
print("\n=== Dot notation example (nested field) ===")
print("students.find({'address.city': 'London'})  ← use this for nested fields")

# ============================================================
# To run:
#   python 08_find_with_query.py
#
# REQUIRES: Run 06_inserting_many_documents.py first
# ============================================================
