# Linq Technology Intern Assessment (With Bonus)

This repository contains the complete solution for the **Technology Intern Take-Home Assessment**, covering **all mandatory tasks** and **optional bonus features** (except Docker for this README).  
It demonstrates **database setup, data ingestion, visualization, and extended functionalities** to showcase real-world readiness.

---

## Professional Summary

This project showcases my ability to:

- Design and implement **data pipelines** using **Python and MongoDB**.
- Perform **data transformations** to enrich records with calculated fields.
- Build **static and real-time visualizations** for monitoring and analysis.
- Follow **clean coding practices** suitable for production-ready workflows.

**Highlights:**
- **Automated Data Flow:** From generation → ingestion → visualization.
- **Scalable & Organized:** Modular Python scripts.
- **Real-Time Ready:** Supports live data monitoring with dynamic charting.

---

## Prerequisites

Before running the project, ensure the following are installed:

- **Python 3.8+**  
- **Pip** package manager  
- **MongoDB (local installation)**  
  - [Download MongoDB Community Edition](https://www.mongodb.com/try/download/community)  
- **MongoDB Compass** *(Optional, for GUI verification)*  
- Install required Python packages:
  ```bash
  pip install pymongo pandas matplotlib
  -- Optional for real-time visualization bonus
  pip install streamlit
  
pymongo → For connecting to MongoDB
pandas → For data handling and transformation
matplotlib → For static and real-time visualization
streamlit (optional) → web dashboard bonus

Run Steps :
-------------------------------------------------------
Prerequisites
-------------------------------------------------------
- Install Python 3.8+
- Install MongoDB locally (default port: 27017)
- Install MongoDB Compass to verify data

Install Python packages:
pip install pymongo pandas matplotlib
pip install streamlit

-------------------------------------------------------
Start MongoDB
-------------------------------------------------------
- Start MongoDB server locally:
  mongod
- Verify connection at:
  mongodb://localhost:27017

-------------------------------------------------------
Navigate to Project Folder
-------------------------------------------------------
cd linq_tech (file_name)

-------------------------------------------------------
Setup Database
-------------------------------------------------------
python datastore_setup.py
- Creates database: linq_db
- Creates collection: metrics

-------------------------------------------------------
Insert Sample Data
-------------------------------------------------------
python data_ingest.py
- Inserts 50 mock records with:
  category, value, timestamp, status

-------------------------------------------------------
Generate Static Visualization
-------------------------------------------------------
python visualization.py
- Displays line chart
- Saves output as dashboard.png

-------------------------------------------------------
Run Real-Time Visualization
-------------------------------------------------------
1. In first terminal:
   python real_time_visualization.py
2. In second terminal:
   python data_ingest.py
- we can see the chart update live

-------------------------------------------------------
Verify Output
-------------------------------------------------------
- Check MongoDB Compass for inserted documents
- Verify dashboard.png in the folder

