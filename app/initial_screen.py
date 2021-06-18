from kivy.uix.screenmanager import Screen
from modules.handle_cache import set_item, get_item
from modules.session_manager import get_profiles
from modules.session_manager import get_item_aws_file

class InitialScreen(Screen):
    global profile
    profile = None

    def __init__(self, **kwargs):
        super(InitialScreen, self).__init__(**kwargs)
        self.ids.spinner_id.values = get_profiles()

    def spinner_clicked(self, value):
        global profile
        profile = value
        set_item("profile", value)

    def handle_enter(self, alert, root):
        global profile
        if profile is None:
            alert.open()
        else:
            set_item("mfa_serial", get_item_aws_file(profile, "mfa_serial"))
            set_item("role_arn", get_item_aws_file(profile, "role_arn"))
            root.manager.current = "main_screen"
