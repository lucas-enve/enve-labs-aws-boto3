import boto3
import csv

ec2 = boto3.resource('ec2')

with open("Images.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["InstanceId", "ImageId", "Name", "OS Info"])

    for instance in ec2.instances.all():
        image = instance.image
        image.load()

        name = getattr(image, 'name', 'N/A')
        description = getattr(image, 'description', '')
        os_info = description or name or 'Unknown'

        writer.writerow([
            instance.id,
            image.id,
            name,
            os_info
        ])

print("saved Images.csv")
