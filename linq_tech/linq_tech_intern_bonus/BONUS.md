

This project implements the optional bonus tasks.


- A new field `status` is added to each record.
- `status = "high"` if `value > 300`, else `"normal"`.


- Includes `Dockerfile` and `docker-compose.yml` to run MongoDB and Python app.


```bash
docker-compose up -d
```

Then you can exec into the app container to run the scripts:
```bash
docker exec -it linq_app bash
python datastore_setup.py
python data_ingest.py
python visualization.py
```
