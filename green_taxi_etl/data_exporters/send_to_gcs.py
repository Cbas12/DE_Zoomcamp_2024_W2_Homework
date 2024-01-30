import pyarrow as pa
import pyarrow.parquet as pq
import os
import pandas as pd

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "/home/src/spatial-vision-412003-d340896a4e0f.json"

bucket_name = 'mage-zoomcamp-cbas'
project_id = 'spatial-vision-412003'

table_name = "green_taxi_data"

root_path = bucket_name+"/"+table_name

@data_exporter
def export_data(data, *args, **kwargs):
    tabla = pa.Table.from_pandas(data)

    gcs = pa.fs.GcsFileSystem()

    pq.write_to_dataset(tabla, root_path=root_path, partition_cols=['lpep_pickup_date'], filesystem=gcs)

    print("Filas cargas: "+str(data.shape[0]))