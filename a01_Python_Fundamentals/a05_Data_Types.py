def main():
    # String (str)
    instance_type = 't2.micro'
    message = "My instances are type: "

    # Integer (int)
    num_of_instances = 5
    hours_running = 10

    print (f"{message} {instance_type}. I have {num_of_instances} of them and they have been running {hours_running} hours.")

    # Boolean (bool)
    instances_running = True
    # print(f"Are my instances running? {instances_running}.")
    # print(f"My variable is of type: {type(instances_running)}")

    # Floating-Point Number (float)
    instances_cost_per_hour = 0.25
    print(f"The price of running them per instance per hour is {instances_cost_per_hour} USD.")


# Entry point of my script
if __name__ == '__main__':
    main()        
