from kivy.uix.screenmanager import Screen

from modules.handle_cache import set_item
from modules.session_manager import get_profiles
from modules.session_manager import configure_session


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
        if(profile == None):
            alert.open()
        else:
            root.manager.current = "main_screen"