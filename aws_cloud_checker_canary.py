import boto3
import json

aws_access_key_id = 'AKIA2OGYBAH6S4M5DDZO'
aws_secret_access_key = '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'
region = 'us-east-2'

session = boto3.Session(
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    region_name=region
)

s3 = session.resource('s3')

try:
    response = []
    for bucket in s3.buckets.all():
        response.append(bucket.name)
    print(json.dumps(response))
except Exception as e:
    print(f"Error: {e}")
