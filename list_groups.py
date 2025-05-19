import boto3
import csv

client = boto3.client("iam")

paginator = client.get_paginator("list_groups")

pages = paginator.paginate()

with open("list_groups_paginator.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(['GroupName', 'GroupId', 'Arn', 'CreateDate'])

    for page in pages:
        for group in page['Groups']:
            writer.writerow([
                group['GroupName'],
                group['GroupId'],
                group['Arn'],
                group['CreateDate']
            ])

print("saved list_groups_paginator.csv")
