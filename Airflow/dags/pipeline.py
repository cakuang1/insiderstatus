from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.bash_operator import BashOperator
from datetime import datetime
import boto3













def upload_to_s3():





def redshiftupdate():
    













with DAG('your_dag', start_date=datetime(2023, 1, 1), schedule_interval='@daily') as dag:
    downloader  = BashOperator(
        task_id='downloader',
        bash_command='python /path/to/your_script.py'

    )
    
    
    
