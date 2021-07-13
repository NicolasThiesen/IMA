from kivy.uix.popup import Popup
from modules.session_manager import configure_session
from modules.handle_cache import set_item, get_item


class MFA(Popup):
    def set_mfa(self):
        set_item("mfa", self.ids.mfa.text)
        _access = get_item("AccessKeyId")
        try:
            if not _access:
                configure_session()
        except Exception as err:
            print(err)
