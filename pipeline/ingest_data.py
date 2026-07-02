import pandas as pd
from sqlalchemy import create_engine
import click


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

@click.command()
@click.option('--pg-user', default='root', help='PostgreSQL user')
@click.option('--pg-password', default='root', help='PostgreSQL password')
@click.option('--pg-host', default='localhost', help='PostgreSQL host')
@click.option('--pg-port', default=5433, type=int, help='PostgreSQL port')
@click.option('--pg-db', default='ny_taxi', help='PostgreSQL database name')
@click.option('--target-table', default='yellow_taxi_data', help='Target table name')
def main(pg_user, pg_password, pg_host, pg_port, pg_db, target_table):
    year = 2021
    mounth = 1

    prefix = 'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/'
    file = f'{prefix}/yellow_tripdata_{year}-{mounth:02d}.csv.gz'

    engine = create_engine(f'postgresql+psycopg://{pg_password}:{pg_user}@{pg_host}:{pg_port}/{pg_db}')


    df_iter = pd.read_csv(
        file,
        dtype=dtype,
        parse_dates=parse_dates,
        iterator=True,
        chunksize=100_000
    )

    create_colums = True
    for chunk in df_iter:
        if create_colums:
            chunk.head(n=0).to_sql(name=target_table,
                                con=engine,
                                if_exists='replace')
            create_colums = False

        chunk.to_sql(name=target_table,
                     con=engine,
                     if_exists='append')


if __name__ == '__main__':
    main()


