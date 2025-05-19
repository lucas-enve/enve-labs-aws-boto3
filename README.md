# enve-boto3-iam

![ENVE Labs Image](https://lwfiles.mycourse.app/662bd5aeace4f91c41b88682-public/0df4dfacf02d3b01f92fd56ea50a4a3f.png)

Scripts to audit IAM resources in AWS using boto3.

## Description

This repository contains Python scripts that use the **boto3** library to retrieve IAM information from AWS, such as:

- List users (using paginator)
- List user groups (using paginator)
- List policies (using pagitator)
- List roles (using paginator)
- List attached policies for a specific user (using paginator and sys.argv for user)
- List attached policies for a specific user group (using paginator and sys.argv for group name)

The output is exported to CSV files.

## Requirements

- Python 3.x
- pip install boto3
- AWS CLI pre-configured with valid credentials

## Usage

Run any of the Python scripts with Python 3. For example:

```bash
python3 list_users.py
```

## Setup

It's recommended to use a Python virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
pip install boto3
```
