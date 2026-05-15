# ============================================================
# Day 27 - Topic 12: Update with Query
# ============================================================
#
# Two update methods:
#   update_one(filter, update)  → updates FIRST matching document
#   update_many(filter, update) → updates ALL matching documents
#
# Always use $set operator — otherwise the whole document
# gets REPLACED with only the new fields!
#
# Common operators:
#   $set  → set a field to a new value
#   $inc  → increment a number field
#   $unset→ remove a field completely
#
# ============================================================

import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()
client = MongoClient(os.getenv("MONGO_URI"))
db = client["thirty_days_python"]
students = db["students"]

# --- update_one: change Bob's grade to A ---
print("=== update_one: Bob's grade → A ===")
result = students.update_one(
    {"name": "Bob"},           # filter: find Bob
    {"$set": {"grade": "A"}}   # update: set grade to A
)
print("Documents modified:", result.modified_count)

# Verify
bob = students.find_one({"name": "Bob"})
print("Bob's new grade:", bob["grade"])

# --- update_many: give all grade-A students a scholarship ---
print("\n=== update_many: scholarship = True for all grade-A ===")
result = students.update_many(
    {"grade": "A"},
    {"$set": {"scholarship": True}}
)
print("Documents modified:", result.modified_count)

# --- $inc: increment Dan's age by 1 ---
print("\n=== $inc: Dan's age + 1 ===")
students.update_one({"name": "Dan"}, {"$inc": {"age": 1}})
dan = students.find_one({"name": "Dan"})
print("Dan's new age:", dan["age"])

# ============================================================
# NOTE: Run 06_inserting_many_documents.py first to have data
# ============================================================
