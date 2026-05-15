import os
from dotenv import load_dotenv
from flask import Flask
from pymongo import MongoClient

load_dotenv()
app = Flask(__name__)
client = MongoClient(os.getenv("MONGO_URI"))
db = client["thirty_days_python"]
students = db["students"]

@app.route("/")
def home():
    count = students.count_documents({})
    return f"<h2>✅ Flask + MongoDB Connected!</h2><p>Total students: {count}</p>"

@app.route("/students")
def get_students():
    all_students = list(students.find({}, {"_id": 0}))
    return {"students": all_students}

if __name__ == "__main__":
    app.run(debug=True)