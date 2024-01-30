if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    #Quitar viajes pasajeros=0 o con distancia=0    
    df = data[((data['passenger_count'] > 0) & (data['trip_distance'] > 0))]

    #crear columna de fecha
    df['lpep_pickup_date'] = df['lpep_pickup_datetime'].dt.date
    #print(df[['lpep_pickup_datetime','lpep_pickup_date']])

    #arreglar mayusculas en nombres de columnas
    df.columns = (df.columns
                     .str.replace(' ','_')
                     .str.lower()
    )

    return df


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
