import boto3
import csv

client = boto3.client("iam")


response = client.list_attached_user_policies(UserName = "example-name")  # edit

with open("list_attached_user_policies.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["PolicyName", "PolicyArn"])

    for policy in response["AttachedPolicies"]:
        writer.writerow([
            policy["PolicyName"],
            policy["PolicyArn"],
            
        ])

print("saved list_attached_user_policies.csv")  # edit