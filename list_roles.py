import boto3
import csv

client = boto3.client("iam")

paginator = client.get_paginator("list_roles")

pages = paginator.paginate()

with open("list_roles_paginator.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(['RoleName', 'RoleId', 'Arn', 'CreateDate'])

    for page in pages:
        for role in page['Roles']:
            writer.writerow([
                role['RoleName'],
                role['RoleId'],
                role['Arn'],
                role['CreateDate']
            ])

print("saved list_roles_paginator.csv")
