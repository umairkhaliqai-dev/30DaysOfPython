# ============================================================
# Day 27 - Topic 14: Drop a Collection
# ============================================================
#
# Dropping a collection PERMANENTLY deletes everything in it
# including all documents AND indexes.
#
# Difference:
#   delete_many({}) → removes all documents, collection still exists
#   drop()          → removes the entire collection completely
#
# WARNING: No recycle bin in MongoDB. Dropped data is GONE.
#
# ============================================================

import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()
client = MongoClient(os.getenv("MONGO_URI"))
db = client["thirty_days_python"]

# --- See collections before drop ---
print("Collections BEFORE drop:", db.list_collection_names())

# --- Drop the employees collection ---
print("\n=== Dropping 'employees' collection ===")
db["employees"].drop()

# --- See collections after drop ---
print("Collections AFTER drop:", db.list_collection_names())

# --- Dropping a collection that doesn't exist = no error ---
print("\n=== Dropping a non-existent collection (safe) ===")
db["fake_collection"].drop()
print("No error raised — MongoDB handles this gracefully.")

# ============================================================
# NOTE: Run 05_creating_database_and_collection.py first
#       so the 'employees' collection exists to drop.
# ============================================================
