from datetime import datetime

from airflow.providers.standard.operators.python import PythonOperator

from airflow import DAG
from commands.main import create_table, ingest_data

with DAG(
    dag_id="dag_create_table",
    start_date=datetime(2025, 5, 19),
    schedule="15 * * * *",  # every hour at **:15
    catchup=False,
) as dag:

    first_task = PythonOperator(task_id="create_table", python_callable=create_table)

    second_task = PythonOperator(task_id="ingest_data", python_callable=ingest_data)

first_task >> second_task
