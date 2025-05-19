import boto3
import csv

client = boto3.client("iam")

paginator = client.get_paginator("list_policies")
pages = paginator.paginate(Scope='Local')  # Scope: Local/AWS/All

with open("list_local_policies.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(['PolicyName', 'PolicyId', 'Arn', 'CreateDate'])

    for page in pages:
        for policy in page['Policies']:
            writer.writerow([
                policy['PolicyName'],
                policy['PolicyId'],
                policy['Arn'],
                policy['CreateDate']
            ])

print("saved list_local_policies.csv")