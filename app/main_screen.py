from kivy.uix.screenmanager import Screen
from modules.ec2 import describe_instances
from modules.handle_database import get_regions, get_services
from modules.handle_cache import set_item


class MainScreen(Screen):

    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        self.ids.spinner_region.values = get_regions()
        self.ids.spinner_service.values = get_services()

    def spinner_clicked(self, value, key):
        set_item(key, value)
