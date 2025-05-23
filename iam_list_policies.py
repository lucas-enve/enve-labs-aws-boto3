import boto3
import csv

client = boto3.client("iam")

paginator = client.get_paginator("list_policies")
pages = paginator.paginate(Scope='ALL')  # Scope: Local/AWS/All

with open("list_attached_policies.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(['PolicyName', 'PolicyId', 'Arn', 'AttachmentCount', 'CreateDate']) # ADD :

    for page in pages:
        for policy in page['Policies']:
            if policy['AttachmentCount'] > 0:
                writer.writerow([
                    policy['PolicyName'],
                    policy['PolicyId'],
                    policy['Arn'],
                    policy['AttachmentCount'],
                    policy['CreateDate']
                ])

print("saved list_attached_policies.csv")