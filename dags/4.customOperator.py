from airflow import DAG
from datetime import datetime       
from helloOperator import HelloOperator        

with DAG (dag_id='customoperator',
        description='Nuestro primer custom operator',
        start_date=datetime(2022,8,1)) as dag:

    t1 = HelloOperator(task_id="Hello",
                    name="Johana")
    t1                
