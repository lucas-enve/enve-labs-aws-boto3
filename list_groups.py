import boto3
import csv

cliente = boto3.client("iam")

response = cliente.list_groups(PathPrefix="/")

#for groups in response["Groups"]:
    #print(groups)


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