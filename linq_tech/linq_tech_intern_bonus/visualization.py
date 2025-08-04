import matplotlib.pyplot as plt
from pymongo import MongoClient
import pandas as pd

client = MongoClient("mongodb://localhost:27017/")
db = client["linq_db"]
collection = db["metrics"]

df = pd.DataFrame(list(collection.find({}, {"_id":0})))
df.sort_values("timestamp", inplace=True)

plt.figure(figsize=(10,5))
for cat in df['category'].unique():
    subset = df[df['category']==cat]
    plt.plot(subset['timestamp'], subset['value'], label=cat)

plt.title("Category Trends Over Time")
plt.xlabel("Time")
plt.ylabel("Value")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("dashboard.png")
plt.show()
