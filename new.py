from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import timedelta,datetime
import pandas as pd

def process_data():
    data = {
        'sal': [1000, 2000, 3000, 4000, 5000],
        'ename': ['sam', 'alan', 'jack', 'rock', 'alice']
    }

    
    df = pd.DataFrame(data)

    sum_value = df['sal'].sum()

 
    print("Sum of column 'column_name':", sum_value)


default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 4, 13),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Define the DAG
dag = DAG(
    'pandas_data_processing',
    default_args=default_args,
    description='A simple DAG to process data using Pandas',
    schedule_interval='@daily'
)

process_data_task = PythonOperator(
    task_id='process_data_task',
    python_callable=process_data,
    dag=dag,
)

process_data_task