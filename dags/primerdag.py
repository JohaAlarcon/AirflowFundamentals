from airflow import DAG
from airflow.operators.empty import EmptyOperator
from datetime import datetime

with DAG(dag_id="primerdag",
         description="Nuestro primer dag",
         start_date=datetime(2022,7,1),
         schedule_interval="@once") as dag:
    
    t1=EmptyOperator(task_id="Dummy")