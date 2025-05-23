import boto3
import csv
import sys

if len(sys.argv) != 2:
    print("Uso: python list_attached_user_policies_paginator.py <UserName>")
    sys.exit(1)

user_name = sys.argv[1]

client = boto3.client('iam')
paginator = client.get_paginator('list_attached_user_policies')

pages = paginator.paginate(UserName=user_name)

with open(f"list_attached_user_policies_paginator_{user_name}.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["PolicyName", "PolicyArn"])

    for page in pages:
        for policy in page["AttachedPolicies"]:
            writer.writerow([
                policy["PolicyName"],
                policy["PolicyArn"],
            ])

print(f"saved list_attached_user_policies_paginator_{user_name}.csv")
