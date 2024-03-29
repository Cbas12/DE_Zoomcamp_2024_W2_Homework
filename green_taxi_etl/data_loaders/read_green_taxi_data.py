import io
import pandas as pd
import requests

if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data(*args, **kwargs):
    #Fuentes
    url_202010="https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2020-10.csv.gz"
    url_202011="https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2020-11.csv.gz"
    url_202012="https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2020-12.csv.gz"

    #Formato
    green_taxi_dtypes = {
        'VendorID': pd.Int64Dtype(),
        'store_and_fwd_flag': str,
        'RatecodeID': pd.Int64Dtype(),
        'PULocationID': pd.Int64Dtype(),
        'DOLocationID': pd.Int64Dtype(),
        'passenger_count': pd.Int64Dtype(),
        'trip_distance': float,
        'fare_amount': float,
        'extra': float,
        'mta_tax': float,
        'tip_amount': float,
        'tolls_amount': float,
        'ehail_fee': str,
        'improvement_surcharge': float,
        'total_amount': float,
        'payment_type': pd.Int64Dtype(),
        'trip_type': pd.Int64Dtype(),
        'congestion_surcharge': float
    }

    parse_fechas = ['lpep_pickup_datetime','lpep_dropoff_datetime']
    
    url_lista = [url_202010,url_202011,url_202012]

    #Crear df sin filas
    df = pd.read_csv(url_202010,sep=",",compression="gzip",dtype=green_taxi_dtypes,parse_dates=parse_fechas).head(n=0)
    
    
    #Cargar tres archivos
    print("Filas: "+str(df.shape[0]))
    for url in url_lista:             
        df_temp = pd.read_csv(url,sep=",",compression="gzip",dtype=green_taxi_dtypes,parse_dates=parse_fechas)
        df = pd.concat([df,df_temp])
        print("Filas: "+str(df.shape[0]))

    #print(df.head())
    return df


@test
def test_output(output, *args) -> None:
    assert output is not None, 'The output is undefined'
