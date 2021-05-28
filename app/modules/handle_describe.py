import asyncio


async def handle_describe(client, command):
    if command == "ec2":
        return asyncio.create_task(describe_instances(client))
    elif command == "autoscaling":
        return asyncio.create_task(describe_autoscaling(client))


async def describe_instances(client):
    return client.describe_instances()


async def describe_autoscaling(client):
    return client.describe_auto_scaling_groups()
