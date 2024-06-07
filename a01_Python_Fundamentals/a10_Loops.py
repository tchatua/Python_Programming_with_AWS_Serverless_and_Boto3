def foorLoop():
    ingredients = ['spinach', 'cheese', 'onions', 'mushrooms']

    # Use a for loop to iterate through the list ingredients
    for ingredient in ingredients:
        print(f"Adding {ingredient} to the recipe")

def whileLoop():
    desired_cookies = 12
    baked_cookies_count = 0

    # Use a while loop  to bake cookies until we reach the desire  number
    while baked_cookies_count < desired_cookies:
        print("Baking a cookie...")
        baked_cookies_count += 1

    print(f"We have baked {baked_cookies_count} cookies.")

def main():
    # List of AWS services
    aws_service = ['S3', 'Lambda', 'EC2', 'RDS', 'DynamoDB']
    print(f"\n\t- AWS Services list: \n{aws_service}")

    # Use a for loop to iterate through the list
    print(f"\n\t- Using a for loop to iterate through the list:")
    for service in aws_service:
        print(f"{service}")

    # Use a while loop to iterate through the list in reverse order
    print(f"\n\t- Using a while loop to iterate the list in a reverse order:")
    index = len(aws_service) -1
    # print(index)
    while index >= 0:
        print(aws_service[index])
        index -= 1

    # using enumerate() with a for loop to get both index value
    print(f"\n\t- Using enumerate() with a for loop to get both index and value")
    for index, service in enumerate(aws_service):
        print(f"Service # {index +1 }: {service}.")


if __name__ == '__main__':
    # print(f"\n\tThe For Loop")
    # foorLoop()

    # print(f"\n\tThe While Loop")
    # whileLoop()

    main()