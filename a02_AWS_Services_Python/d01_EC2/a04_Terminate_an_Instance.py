"""
    This script terminate EC2 instance using Boto3 Python SDK
"""
# Import statements
import boto3

# Terminate an instance
ec2.Instance(instance_id).terminate()