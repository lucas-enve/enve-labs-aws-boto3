import boto3
import sys
from botocore.exceptions import ClientError

if len(sys.argv) !=2:
    print("use:python storage_class.py <bucket_name>")
    sys.exit(1)


bucket_name = sys.argv[1]  

s3 = boto3.resource('s3')
bucket = s3.Bucket(bucket_name)


try:
    for obj in bucket.objects.all():
        print(f"{obj.key} - {obj.storage_class or 'STANDARD'}")
except ClientError as e:
    print(f"{bucket_name} (error)")
