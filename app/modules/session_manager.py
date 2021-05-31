from boto3 import client
from subprocess import check_output
from modules.handle_cache import get_item
from modules.handle_database import get_command


def configure_session():
    _client_sts = client("sts")
    _res = _client_sts.assume_role(RoleArn=get_item("role_arn"),
                                   RoleSessionName=get_item("profile"),
                                   SerialNumber=get_item("mfa_serial"),
                                   TokenCode=get_item("mfa"))
    _client = client(region_name=get_item("region"),
                     service_name=get_command(get_item("service")),
                     aws_access_key_id=_res['Credentials']['AccessKeyId'],
                     aws_secret_access_key=_res['Credentials']['SecretAccessKey'],
                     aws_session_token=_res['Credentials']['SessionToken'])
    return _client


def get_profiles():
    return check_output("aws configure list-profiles").decode("utf-8").split()


def get_item_aws_file(profile,item):
    try:
       _res = check_output(f"aws configure get {item} --profile {profile}").decode("utf-8").split()
    except:
        _res = ""
    return _res[0]