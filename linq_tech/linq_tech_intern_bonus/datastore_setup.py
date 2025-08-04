from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["linq_db"]
collection = db["metrics"]

print("Database and collection created successfully!")