
def handle_describe(client, command):
    if command == "ec2":
        return client.describe_instances()
    elif command == "autoscaling":
        return client.describe_auto_scaling_groups()
    elif command == "ecs":
        return client.describe_clusters()
    elif command == "ebs":
        return client.describe_volumes()
    elif command == "elb" or command == "elbv2":
        return client.describe_load_balancers()
    elif command == "elasticbeanstalk":
        return client.describe_environments()
    elif command == "rds":
        return client.describe_db_clusters()


