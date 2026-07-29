import pandas as pd

dtype = {
    "VendorID": "Int64",
    "passenger_count": "Int64",
    "trip_distance": "float64",
    "RatecodeID": "Int64",
    "store_and_fwd_flag": "string",
    "PULocationID": "Int64",
    "DOLocationID": "Int64",
    "payment_type": "Int64",
    "fare_amount": "float64",
    "extra": "float64",
    "mta_tax": "float64",
    "tip_amount": "float64",
    "tolls_amount": "float64",
    "improvement_surcharge": "float64",
    "total_amount": "float64",
    "congestion_surcharge": "float64"
}

parse_dates = [
    "tpep_pickup_datetime",
    "tpep_dropoff_datetime"
]

def load_taxi_data(year=2021, mounth=1):

    prefix = 'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/'
    file = f'{prefix}/yellow_tripdata_{year}-{mounth:02d}.csv.gz'

    df_iter_taxi = pd.read_csv(
            file,
            dtype=dtype,
            parse_dates=parse_dates,
            iterator=True,
            chunksize=100_000
            )

    return df_iter_taxi


