# ============================================================
# Day 27 - Topic 02: SQL vs NoSQL
# ============================================================
#
# SQL (e.g. MySQL, PostgreSQL)    | NoSQL (e.g. MongoDB)
# --------------------------------|-------------------------------
# Tables with rows & columns      | Collections with documents
# Fixed schema (rigid)            | Flexible schema (dynamic)
# Uses JOINs for relations        | Embedded/nested documents
# Scales vertically               | Scales horizontally
# Uses SQL language               | Uses MongoDB Query Language
# Best for structured data        | Best for unstructured/flexible data
#
# When to use MongoDB?
#   - Data structure changes often
#   - Working with JSON APIs
#   - Real-time apps or big data
#   - Need to scale across multiple servers
#
# ============================================================

# SQL would store hobbies in a SEPARATE table with a foreign key.
# MongoDB stores everything inside ONE document — much simpler.

# --- SQL style (simulated in Python) ---
sql_users_table = [
    {"id": 1, "name": "Alice", "age": 22},
]
sql_hobbies_table = [
    {"user_id": 1, "hobby": "reading"},
    {"user_id": 1, "hobby": "coding"},
]

print("=== SQL Style (two separate tables) ===")
print("Users  :", sql_users_table)
print("Hobbies:", sql_hobbies_table)

# --- MongoDB style (simulated in Python) ---
mongo_document = {
    "_id": 1,
    "name": "Alice",
    "age": 22,
    "hobbies": ["reading", "coding"]   # stored inside the same document
}

print("\n=== MongoDB Style (one document) ===")
print("Document:", mongo_document)
print("Hobbies :", mongo_document["hobbies"])

# ============================================================
# NOTE: No MongoDB connection needed for this file.
# ============================================================
