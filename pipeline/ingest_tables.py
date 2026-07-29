import ingest_zone
import ingest_taxi_data
from sqlalchemy import create_engine
import click

@click.command()
@click.option('--pg-user', default='root', help='PostgreSQL user')
@click.option('--pg-password', default='root', help='PostgreSQL password')
@click.option('--pg-host', default='localhost', help='PostgreSQL host')
@click.option('--pg-port', default=5433, type=int, help='PostgreSQL port')
@click.option('--pg-db', default='ny_taxi', help='PostgreSQL database name')
def ingest_tables(pg_user, pg_password, pg_host, pg_port, pg_db):
    engine = create_engine(f'postgresql://{pg_user}:{pg_password}@{pg_host}:{pg_port}/{pg_db}')


    tables = {'yellow_taxi_data': ingest_taxi_data.load_taxi_data(),
              'taxi_zone': ingest_zone.load_zones_data(),
    }

    for table in tables.keys():
        created_columns = True
        for chunk in tables[table]:
            if created_columns:
                chunk.head(n=0).to_sql(name=table,
                                       con=engine,
                                       if_exists='replace'
                                       )
                created_columns = False


            chunk.to_sql(name=table,
                         con=engine,
                         if_exists='append'
                         )

if __name__ == '__main__':
    ingest_tables()


