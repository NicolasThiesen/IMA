
def handle_describe(client, command):
    if command == "ec2":
        return describe_instances(client)
    elif command == "autoscaling":
        return describe_autoscaling(client)


def describe_instances(client):
    return client.describe_instances()


def describe_autoscaling(client):
    return client.describe_auto_scaling_groups()
