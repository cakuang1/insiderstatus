from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.bash_operator import BashOperator
from datetime import datetime


import boto3
import os
from dotenv import load_dotenv
from datetime import datetime





load_dotenv('/opt/airflow/dags/.env')





def upload_to_s3():
    
    access_key = os.getenv('aws_access_key_id')
    secret_key = os.getenv('aws_secret_access_key')
    bucket_name = os.getenv('bucketname')
    current_date = datetime.now().strftime("%m-%d-%Y")
    print(access_key,secret_key,bucket_name)

    key = f'insider/{current_date}.csv'  # Key represents the file path in the S3 bucket


    # Create an S3 client
    s3_client = boto3.client('s3', aws_access_key_id=access_key, aws_secret_access_key=secret_key)

    # Upload the file to S3
    s3_client.upload_file('/downloads/test.csv', bucket_name, key)
    




with DAG('your_dag', start_date=datetime(2023, 1, 1), schedule_interval='@daily',catchup=False) as dag:
    downloader  = BashOperator(
        task_id='downloader',
        bash_command='python /opt/airflow/dags/dailyscraper.py'

    )
    uploader = PythonOperator(
        task_id = 'uploader',
        python_callable = upload_to_s3,
    
    )

    
    downloader >> uploader
    
