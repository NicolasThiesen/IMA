from kivy.uix.popup import Popup
from kivy.core.clipboard import Clipboard
from json import loads, dumps
from modules.handle_cache import set_item, get_item
from modules.handle_database import get_command
from modules.session_manager import configure_session
from modules.handle_describe import handle_describe
from modules.handle_conversion import get_items_from_dic

class Mapping(Popup):

    def __init__(self, **kwargs):
        super(Mapping, self).__init__(**kwargs)
        _client = configure_session()
        _res = handle_describe(_client, get_command(get_item("service")))
        _show = get_items_from_dic(_res, get_item("attributes"))
        self.ids.result.text = dumps(_show, indent=4, sort_keys=True, default=str)
        set_item("result", _res)


    def handle_copy(self):
        Clipboard.copy(self.ids.result.text)

    def handle_save_cache(self):
        try:
            result = loads(self.ids.result.text)
        except:
            result = self.ids.result.text
        set_item("result", result)