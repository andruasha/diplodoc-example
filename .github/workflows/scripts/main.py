import os
import boto3

# Получение значений переменных среды из GitHub Actions
aws_access_key_id = os.environ.get("STORAGE_ACCESS_KEY_ID")
aws_secret_access_key = os.environ.get("STORAGE_SECRET_ACCESS_KEY")
region = os.environ.get("STORAGE_REGION")
endpoint = os.environ.get("STORAGE_ENDPOINT")
bucket_name = os.environ.get("STORAGE_BUCKET")

# Настройка клиента S3
s3 = boto3.client(
    "s3",
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    region_name=region,
    endpoint_url=endpoint,
)

def list_files_in_bucket(bucket):
    # Получение списка объектов в бакете
    objects = s3.list_objects(Bucket=bucket)
    
    # Вывод списка объектов
    for obj in objects.get("Contents", []):
        print(obj["Key"])

if __name__ == "__main__":
    list_files_in_bucket(bucket_name)
