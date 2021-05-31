from kivy.uix.popup import Popup
from modules.handle_conversion import get_items_from_dic, conversion
from modules.handle_cache import get_item


class Convert(Popup):
    global format_item
    format_item = ""

    def radio_click(self, instance, value,  _format):
        global format_item
        if value:
            format_item = _format

    def handle_convert(self):
        global format_item
        if format_item != "":
            try:
                _dic = get_items_from_dic(get_item("result"), get_item("attributes"))
                conversion(format_file=format_item, path=self.ids.chooser.path, dictionary=_dic, filename="result-"+get_item("service"))
            except Exception as error:
                print(error)
                print(type(get_item("result")))