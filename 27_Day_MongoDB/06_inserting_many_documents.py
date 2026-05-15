# ============================================================
# Day 27 - Topic 06: Inserting Many Documents to Collection
# ============================================================
#
# insert_one(doc)              → inserts a single document
# insert_many([doc1, doc2...]) → inserts multiple documents at once
#
# insert_many() takes a LIST of dictionaries.
# It returns an InsertManyResult with .inserted_ids (list of ObjectIds)
#
# MongoDB auto-assigns a unique "_id" (ObjectId) to each document
# if you don't provide one yourself.
#
# ============================================================

import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()
client = MongoClient(os.getenv("MONGO_URI"))
db = client["thirty_days_python"]
students = db["students"]

# Clear collection first to avoid duplicates on re-run
students.delete_many({})
print("Collection cleared.")

# --- insert_one() ---
single = students.insert_one({"name": "Zara", "age": 19, "grade": "B"})
print("\ninsert_one() ID:", single.inserted_id)

# --- insert_many() ---
new_students = [
    {"name": "Alice", "age": 20, "grade": "A"},
    {"name": "Bob",   "age": 22, "grade": "B"},
    {"name": "Carol", "age": 21, "grade": "A"},
    {"name": "Dan",   "age": 23, "grade": "C"},
]

result = students.insert_many(new_students)

print("\ninsert_many() IDs:")
for id in result.inserted_ids:
    print(" -", id)

print("\nTotal documents in collection:", students.count_documents({}))

# ============================================================
# To run:
#   python 06_inserting_many_documents.py
#
# REQUIRES: Local MongoDB running on port 27017
# ============================================================
