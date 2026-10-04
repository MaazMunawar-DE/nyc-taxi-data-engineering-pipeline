import click
import pandas as pd
from sqlalchemy import create_engine
from tqdm.auto import tqdm

@click.command()
@click.option("--user", type=str, required=True)
@click.option("--password", type=str, required=True)
@click.option("--host", type=str, required=True)
@click.option("--port", type=int, required=True)
@click.option("--db", type=str, required=True)
@click.option("--table-name", type=str, required=True)
@click.option("--year", type=int, required=True)
@click.option("--month", type=int, required=True)
@click.option("--chunk-size", type=int, required=True)
def run(
    user,
    password,
    host,
    port,
    db,
    table_name,
    year,
    month,
    chunk_size,
):
    engine= create_engine(
        f"postgresql+psycopg://{user}:{password}@{host}:{port}/{db}"
    )

    base_url= "https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow"
    file_name =f"yellow_tripdata_{year}-{month:02d}.csv.gz"
    url = f"{base_url}/{file_name}"
    df_iter= pd.read_csv(
        url,
        iterator=True,
        chunksize=chunk_size,   
    )

    first_chunk=next(df_iter)

    first_chunk["tpep_pickup_datetime"] = pd.to_datetime(
    first_chunk["tpep_pickup_datetime"]
    )

    first_chunk["tpep_dropoff_datetime"] = pd.to_datetime(
    first_chunk["tpep_dropoff_datetime"]
    )

    first_chunk.head(n=0).to_sql(
        name=table_name,
        con=engine,
        if_exists="replace",
        index=False
    )
    first_chunk.to_sql(
        name=table_name,
        con=engine,
        if_exists="append",
        index=False,
    )
    for df_chunk in tqdm(df_iter):
        df_chunk["tpep_pickup_datetime"] = pd.to_datetime(
            df_chunk["tpep_pickup_datetime"]
        )
        df_chunk["tpep_dropoff_datetime"] = pd.to_datetime(
            df_chunk["tpep_dropoff_datetime"]
        )
        df_chunk.to_sql(
            name=table_name,
            con=engine,
            if_exists="append",
            index=False
        )

if __name__ == "__main__":
    run()