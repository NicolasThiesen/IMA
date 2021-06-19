from boto3 import client
from subprocess import check_output, run
from modules.handle_cache import get_item, set_item
from modules.handle_database import get_command


def configure_session():
    _client_sts = client("sts")
    _res = _client_sts.assume_role(RoleArn=get_item("role_arn"),
                                   RoleSessionName=get_item("profile"),
                                   SerialNumber=get_item("mfa_serial"),
                                   TokenCode=get_item("mfa"))
    set_item("AccessKeyId", _res["Credentials"]["AccessKeyId"])
    set_item("SecretAccessKey", _res["Credentials"]["SecretAccessKey"])
    set_item("SessionToken", _res["Credentials"]["SessionToken"])


def get_client():
    _client = client(region_name=get_item("region"),
                     service_name=get_command(get_item("service")),
                     aws_access_key_id=get_item('AccessKeyId'),
                     aws_secret_access_key=get_item('SecretAccessKey'),
                     aws_session_token=get_item('SessionToken'))
    return _client


def set_profile(profile_name, mfa_serial, role_arn):
    try:
        run(f"aws configure set profile.{profile_name}.mfa_serial {mfa_serial}", shell=True)
        run(f"aws configure set profile.{profile_name}.role_arn {role_arn}", shell=True)
        run(f"aws configure set profile.{profile_name}.source_profile default", shell=True)
    except:
        print("Erro ao adicionar um novo profile")


def get_profiles():
    return check_output("aws configure list-profiles").decode("utf-8").split()


def get_item_aws_file(profile,item):
    try:
       _res = check_output(f"aws configure get {item} --profile {profile}").decode("utf-8").split()
    except:
        _res = ""
    return _res[0]