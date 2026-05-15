# A **MongoDB URI (Uniform Resource Identifier)** is the connection
#  string used to connect your Python app to a MongoDB database — either 
# locally or on MongoDB Atlas (cloud).
# MONGO_URI=mongodb+srv://umairkhaliqai_db_user:GbkPkFCpGfDgIKVg@cluster0.jzmc51m.mongodb.net/?appName=Cluster0
# We want to use Python to store and manage data in a database on the internet. That database is MongoDB Atlas — a free cloud database.
# 1. Created a MongoDB Atlas account
# Like signing up for Gmail — but instead of email, it gives you a database in the cloud.
# 2. Created a Cluster
# A cluster is basically your database server living on Amazon's computers (AWS) in Ireland. It's always online, free, and ready to store your data.
# 3. Created a database user
# Like creating a username and password to log into your database. Without this, nobody can access it.
# 4. Got the Connection String (URI)
# This is like the address + password combined into one long string. Your Python code uses this to find and log into your database on the internet.
# 5. Installed pymongo
# This is the Python package that lets Python "speak MongoDB's language" — without it, Python has no idea how to talk to MongoDB.
# 6. Installed python-dotenv
# This lets Python read your .env file where you safely stored the connection string — so you never hardcode passwords in your code.
# 7. Created the .env file
# A secret file storing your connection string privately — like a keychain kept off your code.

# ============================================================
# Day 27 - Topic 03: Getting Connection String (MongoDB URI)
# ============================================================
#
# A MongoDB URI is the connection string used to connect your
# Python app to a MongoDB database (local or cloud/Atlas).
#
# URI Format:
#   mongodb+srv://<username>:<password>@<cluster-url>/<dbname>?retryWrites=true&w=majority
#
# How to get it from MongoDB Atlas:
#   1. Go to https://www.mongodb.com and create a free account
#   2. Create a Cluster (free tier available)
#   3. Click Connect → Connect your application
#   4. Copy the URI and replace <password> with your password
#
# For LOCAL MongoDB:
#   mongodb://localhost:27017/
#
# SECURITY RULE: Never hardcode passwords in your code!
# Always use environment variables or a .env file.
#
# ============================================================

# Step 1: Install required packages
#   pip install pymongo python-dotenv

# Step 2: Create a .env file in your project folder:
#   MONGO_URI=mongodb+srv://alice:mypassword@cluster0.mongodb.net/mydb?retryWrites=true&w=majority

# Step 3: Load it in your Python file like this:

import os

# Simulating what loading from .env looks like
# (In real usage, use: from dotenv import load_dotenv; load_dotenv())

# --- Safe way to read the URI ---
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/")  # fallback to local

print("MongoDB URI loaded:", MONGO_URI)
print()

# --- What NOT to do ---
# BAD_URI = "mongodb+srv://alice:mypassword123@cluster0.mongodb.net/mydb"
# Never hardcode passwords like above — it's a security risk!

print("Tip: Add .env to your .gitignore so passwords are never pushed to GitHub.")

# ============================================================
# To run this file:
#   python 03_getting_connection_string.py
#
# No MongoDB connection is made here — just showing the setup.
# ============================================================
