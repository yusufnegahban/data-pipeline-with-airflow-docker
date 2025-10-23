from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
from airflow.providers.postgres.hooks.postgres import PostgresHook
import scraper_airflow
import save_to_db_airflow

default_args = {
    'owner': 'yousef',
    'retries': 2,
    'retry_delay': timedelta(minutes=5),
}

def extract_books():
    books = scraper_airflow.scrape_books_from_toscrape(max_pages=2)
    if books:
        print("📘 Sample book:", books[0])
    return books


def load_books(ti):
    books = ti.xcom_pull(task_ids="extract_books")
    if books:
        hook = PostgresHook(postgres_conn_id="postgres_default")
        save_to_db_airflow.run_saver(books, hook=hook)
        print(f"✅ {len(books)} books saved to DB via hook")
    else:
        print("⚠️ No books to save.")

with DAG(
    dag_id="books_pipeline",
    default_args=default_args,
    description="Books ETL pipeline with Airflow",
    schedule_interval="@daily",
    start_date=datetime(2025, 9, 1),
    catchup=False,
) as dag:

    extract_task = PythonOperator(
        task_id="extract_books",
        python_callable=extract_books
    )

    load_task = PythonOperator(
        task_id="load_books",
        python_callable=load_books
    )

    extract_task >> load_task
