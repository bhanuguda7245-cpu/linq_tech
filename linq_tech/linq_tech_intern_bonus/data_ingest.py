import random
from datetime import datetime, timedelta
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["linq_db"]
collection = db["metrics"]

categories = ["Sales", "Users", "Revenue"]

data = []
for i in range(50):
    value = round(random.uniform(10, 500), 2)
    status = "high" if value > 300 else "normal"  # Bonus transformation
    data.append({
        "category": random.choice(categories),
        "value": value,
        "status": status,
        "timestamp": datetime.now() - timedelta(minutes=i*5)
    })

collection.insert_many(data)
print("Inserted 50 mock records with status field into MongoDB.")
