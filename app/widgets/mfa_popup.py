from kivy.uix.popup import Popup

from modules.handle_cache import set_item


class MFA(Popup):
    def __init__(self, **kwargs):
        super(MFA, self).__init__(**kwargs)

    def set_mfa(self):
        set_item("mfa", self.ids.mfa.text)
