import os
import boto3
from botocore.client import Config

ACCESS_KEY_ID = os.environ.get('ACCESS_KEY_ID')
ACCESS_SECRET_KEY = os.environ.get('ACCESS_SECRET_KEY')
BUCKET_NAME = 'uploading-from-local-dir'

path = '/home/ubuntu/workspace/files'
print(os.listdir(path))
for filename in os.listdir(path):
    data = open('files/'+ filename, 'rb')
    s3 = boto3.resource(
        's3',
        aws_access_key_id=ACCESS_KEY_ID,
        aws_secret_access_key=ACCESS_SECRET_KEY,
        config=Config(signature_version='s3v4')
    )
    s3.Bucket(BUCKET_NAME).put_object(Key=filename, Body=data)
    os.remove('files/'+ filename) 
    print("File Removed!")

print ("Done")