from modules.handle_database import get_service_id, get_attributes
from kivy.uix.checkbox import CheckBox
from kivy.uix.label import Label


def show_attributes(self, service):
    _attributes = get_attributes(get_service_id(service))
    for attribute in _attributes:
        self.ids.grid.add_widget(Label(text=attribute))
        self.checkbox = CheckBox(group=attribute, background_radio_down="atlas://data/images/defaulttheme/checkbox_on", background_radio_normal="atlas://data/images/defaulttheme/checkbox_off")
        self.ids.grid.add_widget(self.checkbox)
        self.checkbox.bind(active=self.handle_checkbox)