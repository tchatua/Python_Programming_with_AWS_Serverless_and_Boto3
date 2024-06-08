# """
#     This script launch EC2 instance using Boto3 Python SDK
# """
# # Import statements
# import boto3

# new_instance = ec2.create_instance(
#     ImageId = "",
#     InstanceType = "",
#     MinCount = 1,
#     MaxCount = 1,
#     Placement={'AvailabilityZone': 'us-east1-a'},
#     SecurityGroupIds =[''],
#     KeyName = '',
#     SubnetId = '',
#     UserData = "#!/bin/bash\necho 'Hello, World' > /home/ec2-user/hello.txt\n",
#     TagSpecifications = [
#         {
#             'ResourceType': 'instance',
#             'Tags': [
#                 {
#                     'Key': 'Name',
#                     'Value': 'My Linux Instance'
#                 }
#             ]
#         }
#     ]

# )

"""
    This script launch EC2 instance using Boto3 Python SDK
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
    
