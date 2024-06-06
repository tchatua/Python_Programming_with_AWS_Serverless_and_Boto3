"""Creating a list of AWS service and modifying the list appropriately"""
def main():
    # Create a list of AWS services
    aws_services = ['s3', 'Lambda', 'EC2', 'RDS', 'DynamoDB']
    print(f"AWS services list: {aws_services}.")

    #Access the first service in the list
    first_service = aws_services[0]
    print(f"First service: {first_service}.")

    #Access the last service in the list
    last_service = aws_services[-1]
    print(f"Last service: {last_service}.")

    # Modify the first service in the list
    aws_services[0] = 'VPC'
    print(f"AWS services list (After modification): {aws_services}")

    # Modify the last service in the list
    aws_services[-1] = 'SNS'
    print(f"AWS services list (After modification): {aws_services}")
    # Add a new service to the list 
    aws_services.append('SQS')
    print(f"AWS services list with the new service: {aws_services}")

    # Remove the second service in the list
    aws_services.pop(1)
    print(f"AWS services list: {aws_services}")

    # Slice the list to get services from index 1 to 3 (inclusive of 1 and exclusive of 3)
    slices_services = aws_services[1:5]
    print(f"Sliced services: {slices_services}.")

    # Find the length of the list
    list_length = len(aws_services)
    print(f"Length of the AWS services list: {list_length}.")

if  __name__ == '__main__':
    main()




    




