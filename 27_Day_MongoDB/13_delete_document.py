# ============================================================
# Day 27 - Topic 13: Delete Document
# ============================================================
#
# Two delete methods:
#   delete_one(filter)  → deletes FIRST matching document
#   delete_many(filter) → deletes ALL matching documents
#
# WARNING: delete_many({}) with empty filter deletes EVERYTHING!
# Always test your filter with find() before deleting.
#
# ============================================================

import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()
client = MongoClient(os.getenv("MONGO_URI"))
db = client["thirty_days_python"]
students = db["students"]

print("Students before delete:", students.count_documents({}))

# --- delete_one: remove Dan ---
print("\n=== delete_one: remove Dan ===")
result = students.delete_one({"name": "Dan"})
print("Deleted count:", result.deleted_count)

# --- delete_many: remove all grade-C students ---
print("\n=== delete_many: remove all grade-C students ===")
result = students.delete_many({"grade": "C"})
print("Deleted count:", result.deleted_count)

# --- Check remaining ---
print("\nStudents remaining:", students.count_documents({}))
print("Remaining names:")
for s in students.find({}, {"_id": 0, "name": 1, "grade": 1}):
    print(" -", s["name"], s["grade"])

# ============================================================
# NOTE: Run 06_inserting_many_documents.py first to have data
# ============================================================
