import boto3
import csv

client = boto3.client('iam')

response = client.list_roles(PathPrefix = "/" )

with open("list_roles.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["RoleName", "RoleId", 'Arn', 'CreateDate'])

    for role in response['Roles']:
        writer.writerow([
            role['RoleName'],
            role['RoleId'],
            role['Arn'],
            role['CreateDate']
        ])

print("saved list_roles.csv")
