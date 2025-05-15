import boto3
import csv

allusers = boto3.client("iam")


response = allusers.list_users(PathPrefix="/")

with open("list_users.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["UserName", "UserId", "Arn", "CreateDate"])

    for user in response["Users"]:
        writer.writerow([
            user["UserName"],
            user["UserId"],
            user["Arn"],
            user["CreateDate"]
        ])

print("saved list_users.csv") # edit

