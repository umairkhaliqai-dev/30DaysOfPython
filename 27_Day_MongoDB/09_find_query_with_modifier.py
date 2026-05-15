# ============================================================
# Day 27 - Topic 09: Find Query with Modifier (Comparison Operators)
# ============================================================
#
# MongoDB supports query OPERATORS for more complex filters.
# These go inside a nested dict with the field name.
#
#   $gt  → greater than          (>)
#   $gte → greater than or equal (>=)
#   $lt  → less than             (<)
#   $lte → less than or equal    (<=)
#   $ne  → not equal             (!=)
#   $in  → value is in a list    (IN)
#
# Syntax:
#   collection.find({"field": {"$operator": value}})
#
# ============================================================

import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()
client = MongoClient(os.getenv("MONGO_URI"))
db = client["thirty_days_python"]
students = db["students"]

# --- $gt: students older than 21 ---
print("=== Age > 21 ($gt) ===")
for s in students.find({"age": {"$gt": 21}}):
    print(s["name"], "-", s["age"])

# --- $gte and $lte: age between 20 and 22 ---
print("\n=== Age between 20 and 22 ($gte / $lte) ===")
for s in students.find({"age": {"$gte": 20, "$lte": 22}}):
    print(s["name"], "-", s["age"])

# --- $ne: students NOT in grade C ---
print("\n=== Not grade C ($ne) ===")
for s in students.find({"grade": {"$ne": "C"}}):
    print(s["name"], "-", s["grade"])

# --- $in: students with grade A or B ---
print("\n=== Grade A or B ($in) ===")
for s in students.find({"grade": {"$in": ["A", "B"]}}):
    print(s["name"], "-", s["grade"])

# ============================================================
# NOTE: Run 06_inserting_many_documents.py first to have data
# ============================================================
