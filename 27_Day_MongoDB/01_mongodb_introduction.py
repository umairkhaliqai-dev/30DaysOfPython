# SHORT Note : 
# NoSQL (short for "Not Only SQL") refers to a broad category of 
# non-relational database systems designed to store, manage, 
# and retrieve data differently than traditional relational databases. 
#  Unlike SQL databases that rely on rigid, tabular structures with 
# predefined schemas, NoSQL databases offer flexible data models that can 
# handle structured, semi-structured, and unstructured data. 

# Key characteristics of NoSQL databases include:

# Flexible Schema: They do not require a fixed schema, allowing for 
# dynamic changes in data structure without downtime or complex migrations. 
# Horizontal Scalability: They are built to scale out across clusters of 
# servers, making them ideal for handling large volumes of data and high traffic. 
# Diverse Data Models: Common types include Key-Value stores (e.g., Redis),
#  Document databases (e.g., MongoDB), Wide-Column stores (e.g., Cassandra),
#  and Graph databases (e.g., Neo4j). 
# Performance Focus: They prioritize speed, availability, and partition 
# tolerance (often following the CAP theorem), frequently using eventual 
# consistency rather than strict ACID transactions to achieve high performance. 
# NoSQL is particularly suited for modern applications such as big data 
# analytics, real-time web applications, and IoT, where data volume and 
# variety exceed the capabilities of traditional relational systems.
    
## What is MongoDB?

# MongoDB is a **NoSQL, document-oriented database** that stores data as 
# flexible JSON-like documents (called BSON — Binary JSON). 
# Unlike traditional relational databases, MongoDB doesn't require a fixed 
# schema, making it ideal for handling dynamic or unstructured data.

# Key features:
# - Stores data in **collections** (like tables) and **documents** 
# (like rows)
# - Each document is a JSON-like object with key-value pairs
# - Highly scalable and flexible
# - Great for real-time applications, big data, and APIs
# $$ Using Python as a client to interact with a MongoDB database. 
# The official library pymongo allows Python to send commands 
# (insert, find, update, delete) to the MongoDB server.


# MongoDB was built from day 1 to handle nested objects and arrays efficiently.

# ============================================================
# Day 27 - Topic 01: MongoDB Introduction
# ============================================================
#
# What is MongoDB?
# ----------------
# MongoDB is a NoSQL, document-oriented database that stores
# data as flexible JSON-like documents (called BSON).
#
# Unlike SQL databases, MongoDB does NOT need a fixed schema.
# Each document can have different fields.
#
# Key Terms:
#   Database   → like a SQL database
#   Collection → like a SQL table
#   Document   → like a SQL row (but it's a dict/JSON object)
#
# ============================================================

# A MongoDB document is just like a Python dictionary.
# You can have nested dicts, lists, mixed types — all in one document.

student = {
    "_id": "001",
    "name": "Alice",
    "age": 22,
    "courses": ["Math", "Science"],   # arrays are supported natively
    "address": {                       # nested objects too
        "city": "London",
        "zip": "E1 6RF"
    }
}

print("Document (Python dict):")
print(student)
print()
print("Name   :", student["name"])
print("City   :", student["address"]["city"])
print("Courses:", student["courses"])

# ============================================================
# NOTE: This file does NOT require MongoDB to be installed.
# It just shows what a MongoDB document looks like in Python.
# From Topic 04 onwards, you need MongoDB + pymongo installed.
#
# To install pymongo:
#   pip install pymongo
# ============================================================
