import boto3
import csv

client = boto3.client("ec2")
paginator = client.get_paginator("describe_security_groups")
response_iterator = paginator.paginate()

with open("security_groups.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["GroupName", "GroupId", "VpcId", "Description"])

    for page in response_iterator:
        for sg in page["SecurityGroups"]:
            writer.writerow([
                sg.get("GroupName", ""),    
                sg.get("GroupId", ""),      
                sg.get("VpcId", ""),        
                sg.get("Description", ""), 
            ])

print("saved security_groups.csv")