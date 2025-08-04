import matplotlib.pyplot as plt
import matplotlib.animation as animation
from pymongo import MongoClient
import pandas as pd

client = MongoClient("mongodb://localhost:27017/")
db = client["linq_db"]
collection = db["metrics"]

fig, ax = plt.subplots(figsize=(10, 5))

def animate(i):
    ax.clear()
    df = pd.DataFrame(list(collection.find({}, {"_id":0})))
    df.sort_values("timestamp", inplace=True)
    for cat in df['category'].unique():
        subset = df[df['category'] == cat]
        ax.plot(subset['timestamp'], subset['value'], label=cat)
    ax.set_title("Category Trends - Real-Time")
    ax.set_xlabel("Time")
    ax.set_ylabel("Value")
    ax.legend()

ani = animation.FuncAnimation(fig, animate, interval=5000)  # Refresh every 5 seconds
plt.show()
