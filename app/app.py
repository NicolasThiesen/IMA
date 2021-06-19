from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager

from screens.help.help_screen import HelpScreen
from screens.initial.initial_screen import InitialScreen
from screens.profile.profile_screen import ProfileScreen
from kivy.config import Config
from screens.main.main_screen import MainScreen
from modules.handle_cache import set_initial_structure

# define the icon
Config.set('kivy', 'window_icon', 'assets/logo-solvimm.png')

# Import the Kivy Files
Builder.load_file("screens/initial/initial_screen.kv")
Builder.load_file("screens/main/main_screen.kv")
Builder.load_file("screens/help/help_screen.kv")
Builder.load_file("screens/profile/profile_screen.kv")


class IMA(App):
    def build(self):
        root = ScreenManager()
        root.add_widget(InitialScreen(name="initial_screen"))
        root.add_widget(MainScreen(name="main_screen"))
        root.add_widget(HelpScreen(name="help_screen"))
        root.add_widget(ProfileScreen(name="profile_screen"))

        return root


if __name__ == '__main__':
    set_initial_structure()
    IMA().run()
