import boto3
import csv

client = boto3.client("iam")


response = client.list_policies(Scope= "Local" )  # Scope: Local/AWS/All

with open("list_policies.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["PolicyName", "PolicyId", "Arn", "CreateDate"])

    for policy in response["Policies"]:
        writer.writerow([
            policy["PolicyName"],
            policy["PolicyId"],
            policy["Arn"],
            policy["CreateDate"]
        ])

print("saved list_policies.csv") # edit