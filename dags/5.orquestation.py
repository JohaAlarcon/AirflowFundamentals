from airflow import DAG
from airflow.operators.bash import  BashOperator
from datetime import datetime

with DAG (
        dag_id="orquestation",
        description="probando la funcionalidad de orquestacion",
        schedule_interval="@daily",
        start_date=datetime(2023,8,1),
        end_date=datetime(2023,9,1),
        default_args={"dependece_on_past":True},
        max_active_runs=1) as dag:

    t1 = BashOperator(task_id="tarea1",
                      bash_command="sleep 2 && echo 'Tarea 1'")

    t2 = BashOperator(task_id="tarea2",
                      bash_command="sleep 2 && echo 'Tarea 2'")

    t3 = BashOperator(task_id="tarea3",
                      bash_command="sleep 2 && echo 'Tarea 3'")

    t4 = BashOperator(task_id="tarea4",
                      bash_command="sleep 2 && echo 'Tarea 4'")

    t1 >> t2 >> [t3,t4]