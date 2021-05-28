from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager

from help_screen import HelpScreen
from initial_screen import InitialScreen
from kivy.config import Config
from main_screen import MainScreen
from modules.handle_cache import set_initial_structure
from modules.handle_frontend import show_attributes

# define the icon
Config.set('kivy','window_icon','assets/logo-solvimm.png')

# Import the Kivy Files
Builder.load_file("initial_screen.kv")
Builder.load_file("main_screen.kv")
Builder.load_file("help_screen.kv")

class IMA(App):
    def build(self):
        root = ScreenManager()
        root.add_widget(InitialScreen(name="initial_screen"))
        root.add_widget(MainScreen(name="main_screen"))
        root.add_widget(HelpScreen(name="help_screen"))
        return root


if __name__ == '__main__':
    set_initial_structure()
    IMA().run()
