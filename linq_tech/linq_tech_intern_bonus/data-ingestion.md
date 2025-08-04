# Data Ingestion

The script `data_ingest.py` generates 50 random records with fields:
- `category`: Sales, Users, or Revenue
- `value`: Random float value
- `status`: "high" if value > 300 else "normal" (bonus transformation)
- `timestamp`: Recent timestamps for trend visualization

Run with:
```bash
python data_ingest.py
```
