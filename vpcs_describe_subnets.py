import boto3
import csv

client = boto3.client("ec2")
paginator = client.get_paginator("describe_subnets")
response_iterator = paginator.paginate()

with open("subnets.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "SubnetId", "VpcId", "AvailabilityZone", "CidrBlock"])
    
    for page in response_iterator:
        for subnet in page["Subnets"]:
            name = "Not defined"  
            for tag in subnet.get("Tags", []):
                if tag["Key"] == "Name":
                    name = tag["Value"]
                    break
            
            writer.writerow([
                name,
                subnet.get("SubnetId", " "),
                subnet.get("VpcId", " "),
                subnet.get("AvailabilityZone", " "),
                subnet.get("CidrBlock", " "),
            ])

print("saved subnets.csv")
