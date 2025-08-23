import sys
from airflow import DAG 
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

sys.path.append('/opt/airflow/api-request')

def safe_main_callable():
    from insert_records import main
    return main()

def example_task():
    print("This is an example task.")

default_args = {
    'owner': 'airflow',
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    dag_id='weather-api-orchestrator',
    description='A DAG to orchestrate data',
    default_args=default_args,
    start_date=datetime(2025, 7, 23),
    schedule=timedelta(minutes=5),
    catchup=False
)

with dag:
    task1 = PythonOperator(
        task_id='ingest_data_task',
        python_callable=safe_main_callable
    )