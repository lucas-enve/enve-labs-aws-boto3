import boto3
from botocore.exceptions import ClientError
import sys 

if len(sys.argv) != 2:
    print("Uso: python3 bucket_policies.py <bucketName>")
    sys.exit(1)

bucket_name = sys.argv[1]    

s3 = boto3.client('s3')

try:
    result = s3.get_bucket_policy(Bucket=bucket_name)
    print(result['Policy'])

except ClientError as e:
    if e.response["Error"]["Code"] == 'NoSuchBucketPolicy':
        print(f'El bucket "{bucket_name}" no tiene política asignada.')
    else:
        raise
