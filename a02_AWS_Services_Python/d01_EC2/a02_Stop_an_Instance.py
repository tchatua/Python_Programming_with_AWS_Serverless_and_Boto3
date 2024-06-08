"""
    This script stop EC2 instance using Boto3 Python SDK
"""
# Import statements
import boto3

# # Stop an instance
# ec2.Instance(instance_id).stop()

# Stop an instance
ec2_resource.Instance(instance_id).stop()
print(f"Instance '{instance_name}-{instance_id}' stopped.")
