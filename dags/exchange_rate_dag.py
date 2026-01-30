from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import sys

sys.path.append("C:/chemin/vers/ton/projet/producer")

from exchange_rate_producer import fetch_and_send

default_args = {
    "owner": "data-engineer",
    "start_date": datetime(2025, 1, 1),
    "retries": 1
}

with DAG(
    dag_id="exchange_rate_hourly",
    default_args=default_args,
    schedule_interval="@hourly",
    catchup=False
) as dag:

    fetch_rates = PythonOperator(
        task_id="fetch_exchange_rates",
        python_callable=fetch_and_send
    )

    fetch_rates
