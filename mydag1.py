from datetime import datetime

from airflow import DAG

from airflow.providers.amazon.aws.operators.s3 import S3CreateObjectOperator

with DAG('mydag1') as dag:
    S3CreateObjectOperator(
        task_id='create_s3_object',
        bucket_name='my-bucket',
        object_key='{{ ds }}_{{ run_id }}.txt',
        data='This is the content of the file.',
    )
