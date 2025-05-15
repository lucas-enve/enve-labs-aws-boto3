import boto3
import csv

client = boto3.client("iam")

response = client.list_groups(PathPrefix="/")

with open("list_groups.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["GroupName", "GroupId", "Arn", "CreateDate"])

    for groups in response["Groups"]:
        writer.writerow([
            groups["GroupName"],
            groups["GroupId"],
            groups["Arn"],
            groups["CreateDate"]
        ])

print("saved list_groups.csv")
