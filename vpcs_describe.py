import boto3
import csv

client = boto3.client("ec2")

paginator = client.get_paginator('describe_vpcs')
response_iterator = paginator.paginate()

with open("all_vpcs_info.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "VpcId" "State", "CidrBlock", "IsDefault"])

    for page in response_iterator:
        for vpc in page["Vpcs"]:
            
            name = "Not defined"
            for tag in vpc.get("Tags", []):
                if tag["Key"] == "Name":
                    name = tag["Value"]
                    break  

            writer.writerow([
                name ,
                vpc.get("VpcId"),
                vpc.get("State"),
                vpc.get("CidrBlock"),
                vpc.get("IsDefault")
            ])

print("saved all_vpcs_info.csv")
