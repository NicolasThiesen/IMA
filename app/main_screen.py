from kivy.uix.screenmanager import Screen
from modules.handle_describe import handle_describe
from modules.handle_database import get_regions, get_services, get_command
from modules.handle_cache import set_item, get_item
from modules.handle_frontend import show_attributes
from modules.session_manager import configure_session
import asyncio
from kivy.uix.floatlayout import FloatLayout

class ConfigTab(FloatLayout):
    pass

class MainScreen(Screen):

    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        self.ids.spinner_region.values = get_regions()
        self.ids.spinner_service.values = get_services()

    def spinner_clicked(self, value, key, root=None):
        set_item(key, value)
        if key == "service":
            show_attributes(self, value)

    def handle_checkbox(self, instance, value):
        _attributes = get_item("attributes")
        if value:
            _attributes.append(instance.group)
        else:
            _attributes.remove(instance.group)
        set_item("attributes", _attributes)

