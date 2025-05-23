import boto3
import csv
from botocore.exceptions import ClientError

client = boto3.client('s3')
buckets = client.list_buckets()['Buckets']

with open("bucket_info.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(['BucketName', 'Region'])

    for bucket in buckets:
        name = bucket['Name']
        try:
            region = client.head_bucket(Bucket=name)['ResponseMetadata']['HTTPHeaders']['x-amz-bucket-region']
        except ClientError:
            region = 'Unknown'
            print(f"{name} (error)")
        writer.writerow([name, region])

print("save bucket_info.csv")


