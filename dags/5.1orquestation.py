from airflow import DAG
from airflow.operators.empty import  EmptyOperator
from datetime import datetime

with DAG (
        dag_id="orquestation1",
        description="probando la funcionalidad de orquestacion",
        schedule_interval="0 7 * * 1",
        start_date=datetime(2022,8,1),
        end_date=datetime(2022,12,1),
        default_args={"dependece_on_past":True},
        max_active_runs=1) as dag:

    t1 = EmptyOperator(task_id="tarea1")

    t2 = EmptyOperator(task_id="tarea2")
                     
    t3 = EmptyOperator(task_id="tarea3")
                    

    t4 = EmptyOperator(task_id="tarea4")
                      

    t1 >> t2 >> [t3,t4]