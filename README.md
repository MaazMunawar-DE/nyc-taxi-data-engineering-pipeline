# 🚕 NYC Taxi Data Engineering Pipeline

A containerized data ingestion pipeline that processes NYC Yellow Taxi data in chunks and loads it into PostgreSQL using Python, Pandas, SQLAlchemy, and Docker.

## 🧰 Tech Stack
`Python` • `Pandas` • `PostgreSQL` • `SQLAlchemy` • `Docker` • `SQL`

## 🔄 Pipeline Overview
NYC Taxi CSV → Python/Pandas → PostgreSQL → SQL Verification

## 📁 Project Structure

```text
nyc-taxi-data-engineering-pipeline/
├── README.md
└── docker-sql-practice/
    ├── .gitignore
    ├── .python-version
    ├── Dockerfile
    ├── README.md
    ├── ingest_data.py
    ├── pyproject.toml
    ├── uv.lock
    └── src/
        └── docker_sql_practice/
