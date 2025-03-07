import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from airflow import DAG
from airflow.operators.python import PythonOperator
from pipelines.aws_s3_pipelines import upload_s3_pipeline
from pipelines.dataco_pipelines import staging_pipeline
from datetime import datetime, timedelta
default_args = {
    'owner': 'Le Huynh Thanh Duong',
    'start_date': datetime(2025, 2, 26),
    'depends_on_past': False,
    'email': ['lehuynhthanh2001@gmail.com'],
    'email_on_failure': True,
    'email_on_retry': False,
    # 'retries': 1,
    # 'retry_delay': timedelta(minutes= 5),
    # 'catchup': False
}

dag = DAG(
    dag_id = 'etl_retail_pipeline',
    default_args=default_args,
    schedule_interval= "@daily",
    tags = ['retail', 'pipeline','etl']
)
# upload_raw_to_s3 = PythonOperator(
#     task_id = 'upload_data',
#     python_callable= test,
#     dag = dag
# )
staging = PythonOperator(
    task_id = 'staging_data',
    python_callable= staging_pipeline,
    dag = dag
)