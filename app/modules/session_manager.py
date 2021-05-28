import boto3
import subprocess


def configure_session(profile, region, service):
    session = boto3.Session(profile_name=profile, region_name=region)
    return session.client(service)


def get_profiles():
    return subprocess.check_output("aws configure list-profiles").decode("utf-8").split()
