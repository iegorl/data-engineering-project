import pandas as pd

dtype = {
    'LocationID': "Int64",
    'Borough': 'string',
    'Zone': 'string',
    'service_zone': 'string'
}

def load_zones_data():
    file = 'https://d37ci6vzurychx.cloudfront.net/misc/taxi+_zone_lookup.csv'

    df_iter_zone = pd.read_csv(file,
                      dtype=dtype,
                      iterator = True,
                      chunksize = 100
                      )
    return df_iter_zone