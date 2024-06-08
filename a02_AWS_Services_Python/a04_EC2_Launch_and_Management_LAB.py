"""
    This script manage Amazon EC2 instances using Boto3 Python SDK
    URL: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/instance/index.html
    Using the Boto3 Python SDK for scripting on AWS to interact with AWS services programmatically.
"""
# Import statements
import boto3

# Create EC2 resource and instance name
ec2_resource = boto3.resource('ec2')
instance_name = 'mpp_ec2_d18udm'

# Store instance ID
instance_id = None

# Check if instance which you are trying to create already exists
# and only work with a instance that hasn't been terminate
instances = ec2_resource.instances.all()
instance_exists = False

for instance in instances:
    for tag in instance.tags:
        if tag['Key'] == 'Name' and tag['Value'] == instance_name:
            instance_exists = True
            instance_id = instance.id
            print(f"An instance named '{instance_name}' with id '{instance_id}' already exist")
            break
    if instance_exists:
        break

if not instance_exists:
    # Launch new EC2 instance if it hasn't already been created
    new_instance = ec2_resource.create_instances(
        ImageId = 'ami-00beae93a2d981137', # Amazon Linux 2023 AMI
        InstanceType = 't2.micro', 
        MinCount = 1,
        MaxCount = 1,
        KeyName = 'private-ssh-key',
        TagSpecifications = [
            {
                'ResourceType': 'instance',
                'Tags': [
                    {
                        'Key': 'Name',
                        'Value': instance_name
                    }
                ]
            }
        ]

    )
    instance_id = new_instance[0].id
    print(f"Instance named '{instance_name}' with id '{instance_id}' created.")
    
# # Stop an instance
# ec2_resource.Instance(instance_id).stop()
# print(f"Instance '{instance_name}-{instance_id}' stopped.")

# # Start an instance
# ec2_resource.Instance(instance_id).start()
# print(f"Instance '{instance_name}-{instance_id}' started.")

# Terminate an instance
ec2_resource.Instance(instance_id).terminate()
print(f"Instance '{instance_name}-{instance_id}' has been terminated.")
