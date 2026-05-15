# ============================================================
# Day 27 - Topic 05: Creating a Database and Collection
# ============================================================
#
# In MongoDB, databases and collections are created LAZILY.
# They don't physically exist until you insert the first document.
# You just reference them by name — MongoDB handles the rest.
#
#   client["db_name"]         → access/create a database
#   db["collection_name"]     → access/create a collection
#   collection.insert_one({}) → actually creates it on disk
#
# ============================================================

import os
from dotenv import load_dotenv
from pymongo import MongoClient

# Load MONGO_URI from your .env file
load_dotenv()
MONGO_URI = os.getenv("MONGO_URI")

# Connect to MongoDB Atlas
client = MongoClient(MONGO_URI)

# Step 1: Reference a database (created on first insert)
db = client["thirty_days_python"]

# Step 2: Reference a collection (created on first insert)
employees = db["employees"]

# Clear first to avoid duplicates on re-run
employees.delete_many({})

# Step 3: Insert a document — this actually creates the DB + collection
result = employees.insert_one({
    "name": "Bob Smith",
    "role": "Developer",
    "salary": 50000
})

print("✅ Connected to MongoDB Atlas!")
print("Inserted document ID:", result.inserted_id)

# Step 4: List all collections in the database
print("Collections in 'thirty_days_python':", db.list_collection_names())

# Step 5: List all databases on the server
print("All databases:", client.list_database_names())

# ============================================================
# To run:
#   python 05_creating_database_and_collection.py
# ============================================================
