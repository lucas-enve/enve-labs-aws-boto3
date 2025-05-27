import boto3
import csv

client = boto3.client("ec2")

paginator = client.get_paginator('describe_security_group_rules')
response_iterator = paginator.paginate()

with open("security_group_rules.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow([
        "GroupId", "SecurityGroupRuleId", "IsEgress", "IpProtocol",
        "FromPort", "ToPort", "CidrIpv4", "ReferencedGroupId"
    ])

    for page in response_iterator:
        for rule in page["SecurityGroupRules"]:
            writer.writerow([
                rule.get("GroupId", ""),
                rule.get("SecurityGroupRuleId", ""),
                rule.get("IsEgress", ""),
                rule.get("IpProtocol", ""),
                rule.get("FromPort", ""),
                rule.get("ToPort", ""),
                rule.get("CidrIpv4", ""),
                rule.get("ReferencedGroupId", "")
            ])

print("saved 'security_group_rules.csv'")
