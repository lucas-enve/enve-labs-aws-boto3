import boto3
import csv

client = boto3.client("iam")


response = client.list_attached_group_policies(GroupName="example-group")  # edit

with open("list_attached_group_policies.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["PolicyName", "PolicyArn"])

    for policy in response["AttachedPolicies"]:
        writer.writerow([
            policy["PolicyName"],
            policy["PolicyArn"],
            
        ])

print("saved list_attached_group_policies.csv")  # edit