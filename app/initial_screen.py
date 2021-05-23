from kivy.uix.screenmanager import Screen
from kivy.factory import Factory
from modules.session_manager import get_profiles



class InitialScreen(Screen):
    global profile
    profile = None

    def __init__(self, **kwargs):
        super(InitialScreen, self).__init__(**kwargs)
        self.ids.spinner_id.values = get_profiles()

    def spinner_clicked(self, value):
        global profile
        profile = value

    def handle_enter(self, alert, root):
        if(profile == None):
            alert.open()
        else:
            root.manager.current = "second"