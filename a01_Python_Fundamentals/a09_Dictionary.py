"""Create a dictionary of AWS services and modifying the dictionary appropriately"""
def main():
    # Create a dictionary of AWS services and their descriptions
    aws_services = {
        'S3': "Simple storage service for object storage",
        'Lambda': "serverless compute service",
        'EC2': "Elastic Compute Cloud"
    }

    # Print the dictionary
    print(f"\n\t- Simple dictionary of AWS services and description:")
    print(f"\t{aws_services}")

    # Access the description of an item in the dictionary
    lambda_description = aws_services['Lambda']
    print(f"\n\t- Description of Lambda: \n\t{lambda_description}.")

    # Modify the description of a service
    aws_services['Lambda'] = "AWS serverless compute service"
    print(f"\n\t- Update description of Lambda: \n\t{aws_services}.")

    # Add a new service and its description to the dictionary
    aws_services['SNS'] = "Simple notification service"
    print(f"\n\t- Added SNS: \n\t{aws_services['SNS']}")

    # Remove the ... service from the dictionary
    del aws_services['Lambda']
    print(f"\n\t- Removed Lambda: \n\t{aws_services}")

    # Use the keys(), values(), and items() methods to display different aspects of the dictionary
    print(f"\n\t- {aws_services.keys()}")
    print(f"\n\t- {aws_services.values()}")
    print(f"\n\t- {aws_services.items()}")

    # Modify the dictionary to add a nested structure with additional information (launch_year)
    aws_services['EC2'] = {
        'description': "Elastic Compute Cloud",
        'launch_year': 2006
    }

    # Print the modified dictionary with nested structure
    print(f"\n\t- Modified dictionary with nested structure:")
    print(f"\t{aws_services}")
    print(f"\n\t{aws_services['EC2']}")

if __name__ == "__main__":
    main()   