import boto3
import csv

client = boto3.client("iam")

paginator = client.get_paginator("list_users")

pages = paginator.paginate()


with open("list_users_paginator.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(['UserName', 'UserId', 'Arn', 'CreateDate'])

    for page in pages:
        for user in page['Users']:
            writer.writerow([
                user['UserName'],
                user['UserId'],
                user['Arn'],
                user['CreateDate']
            ])

print("saved list_users_paginator.csv")