from kivy.uix.popup import Popup
from modules.handle_conversion import conversion
from modules.handle_cache import get_item
from pathlib import Path

class Convert(Popup):
    global format_item
    format_item = ""

    def __init__(self, **kwargs):
        super(Convert, self).__init__(**kwargs)
        path = Path("../../../")
        self.ids.chooser.path = str(path.resolve())

    def radio_click(self, instance, value,  _format):
        global format_item
        if value:
            format_item = _format

    def handle_convert(self):
        global format_item
        if format_item != "":
            try:
                conversion(format_file=format_item, path=self.ids.chooser.path, dictionary=get_item("result_simplificated"), filename=f'result_{get_item("profile")}_{get_item("service")}_{get_item("region")}')
            except Exception as error:
                print(error)
                print(type(get_item("result")))