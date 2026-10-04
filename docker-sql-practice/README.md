# NYC Taxi Data Engineering Pipeline

A practical data engineering project that ingests NYC Yellow Taxi trip data into PostgreSQL using Python and Docker.

## Project Overview

This project demonstrates a simple end-to-end data ingestion workflow.

The pipeline:

1. Downloads NYC Yellow Taxi trip data from a public source
2. Reads the CSV file in chunks using Pandas
3. Connects to PostgreSQL using SQLAlchemy and Psycopg
4. Creates the destination table
5. Loads the dataset into PostgreSQL in chunks
6. Runs the ingestion process inside Docker
7. Uses Docker networking to connect the ingestion container with PostgreSQL
8. Verifies the loaded data using SQL queries and pgAdmin

## Tech Stack

- Python
- Pandas
- PostgreSQL
- Docker
- SQLAlchemy
- Psycopg
- Click
- tqdm
- uv
- pgAdmin

## Project Structure

```text
docker-sql-practice/
│
├── Dockerfile
├── ingest_data.py
├── pyproject.toml
├── uv.lock
├── .python-version
├── .gitignore
└── README.md
```

## Data Source

This project uses the NYC Yellow Taxi Trip dataset.

Example dataset:

```text
yellow_tripdata_2021-01.csv.gz
```

The data is downloaded from the DataTalksClub NYC Taxi dataset repository.

## How the Pipeline Works

The ingestion script accepts command-line parameters including:

```text
--user
--password
--host
--port
--db
--table-name
--year
--month
--chunk-size
```

The script dynamically creates the dataset URL based on the selected year and month.

The dataset is read in chunks using Pandas so the entire file does not need to be loaded into memory at once.

Example:

```python
pd.read_csv(
    url,
    iterator=True,
    chunksize=chunk_size
)
```

The first chunk is used to create the PostgreSQL table schema.

The remaining chunks are appended to the table while tqdm displays the ingestion progress.

The pickup and drop-off timestamp columns are converted to datetime format before loading the data.

## PostgreSQL Setup

PostgreSQL was run inside a Docker container.

Example:

```bash
docker run -it \
  -e POSTGRES_USER=root \
  -e POSTGRES_PASSWORD=root \
  -e POSTGRES_DB=new_york_taxi \
  -v new_york_taxi_storage:/var/lib/postgresql \
  -p 5432:5432 \
  --name ny_taxi_dataset \
  postgres:18
```

## Docker Network

A custom Docker network was created so the ingestion container could communicate with PostgreSQL.

```bash
docker network create pg-network
```

## Build the Ingestion Image

```bash
docker build -t taxi_ingestion:v001 .
```

## Run the Data Ingestion Pipeline

```bash
docker run --rm \
  --network pg-network \
  taxi_ingestion:v001 \
  --user root \
  --password root \
  --host ny_taxi_dataset \
  --port 5432 \
  --db new_york_taxi \
  --table-name yellow_taxi_data \
  --year 2021 \
  --month 1 \
  --chunk-size 100000
```

## Result

The January 2021 NYC Yellow Taxi dataset was successfully loaded into PostgreSQL.

Final row count:

```text
1,369,765 rows
```

The loaded data was verified using SQL queries and pgAdmin.

## Skills Practiced

- Docker
- Docker networking
- PostgreSQL
- pgAdmin
- Python
- Pandas
- SQLAlchemy
- Psycopg
- Click CLI
- Chunk-based data ingestion
- SQL verification
- Working with large CSV datasets

## Learning Goal

The purpose of this project was to build a practical foundation in Data Engineering by creating a working pipeline from raw data ingestion to PostgreSQL storage.

This project is part of my transition from Data Analytics into Data Engineering through hands-on projects.
