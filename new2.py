from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime,timedelta

def start():
    print('the process is started')

def inter():
    print('the data is started proccesing this is intermidete ')

def final():
    print('the data is start loading to sources')

default_args={
    'owner':'airflow',
    'retries':5,
    'retry_delay':timedelta(minutes=5)
}

with DAG(
    dag_id ='intermidiate',
    default_args=default_args,
    start_date=datetime(2024,7,15),
    schedule_interval='@daily',
    catchup=False

) as dag:
    task1= PythonOperator(
        task_id ='task11',
        python_callable=start
    )

task2= PythonOperator(
        task_id ='task21',
        python_callable=inter
    )
task3 =PythonOperator(
        task_id ='task31',
        python_callable=final
    )

task1 >> task2 >> task3