from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, CardTransition

from initial_screen import InitialScreen
from modules.ec2 import describe_instances
from kivy.config import Config

# define the icon
from screens_manager import SecondScreen

Config.set('kivy','window_icon','assets/logo-solvimm.png')

# Import the Kivy Files
Builder.load_file("initial_screen.kv")

class IMA(App):
    def build(self):
        root = ScreenManager()
        root.add_widget(InitialScreen(name="initial_screen"))
        root.add_widget(SecondScreen(name="second"))
        return root

if __name__ == '__main__':
    IMA().run()
