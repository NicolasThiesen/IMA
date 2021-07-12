from kivy.uix.screenmanager import Screen
from modules.handle_database import get_regions, get_services
from modules.handle_cache import set_item, get_item
from modules.handle_frontend import show_attributes


class MainScreen(Screen):

    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        self.ids.spinner_region.values = get_regions()
        _services = get_services()
        _services.sort()
        self.ids.spinner_service.values = _services

    def spinner_clicked(self, value, key, root=None):
        set_item(key, value)
        if key == "service":
            set_item("attributes", [])
            show_attributes(self, value)

    def handle_checkbox(self, instance, value):
        _attributes = get_item("attributes")
        if value:
            _attributes.append(instance.group)
        else:
            if instance.group in _attributes:
                _attributes.remove(instance.group)
        set_item("attributes", _attributes)

    def handle_mfa(self, MFA, Mapping):
        _access = get_item("AccessKeyId")
        if _access:
            Mapping().open()
        else:
            MFA().open()
