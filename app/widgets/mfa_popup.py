from kivy.uix.popup import Popup

from modules.handle_cache import set_item


class MFA(Popup):
    def set_mfa(self):
        set_item("mfa", self.ids.mfa.text)