from kivy.uix.popup import Popup
from kivy.core.clipboard import Clipboard
from json import loads, dumps
from modules.handle_cache import set_item, get_item
from modules.handle_database import get_command, get_key
from modules.session_manager import configure_session, get_client
from modules.handle_describe import handle_describe
from modules.handle_conversion import get_items_from_dic


class Mapping(Popup):

    def __init__(self, **kwargs):
        super(Mapping, self).__init__(**kwargs)
        _access = get_item("AccessKeyId")
        try:
            if not _access:
                configure_session()
            _client = get_client()
            _command = get_command(get_item("service"))
            _key = get_key(_command)
            _res = handle_describe(_client, _command)
            _show = get_items_from_dic(_res, get_item("attributes"), _command, _key)
            set_item("result_simplificated", _show)
            self.ids.result.text = dumps(_show, indent=4, sort_keys=True, default=str)
            set_item("result", _res)
        except Exception as err:
            print(err)

    def handle_copy(self):
        Clipboard.copy(self.ids.result.text)

    def handle_save_cache(self):
        try:
            result = loads(self.ids.result.text)
        except:
            result = self.ids.result.text
        set_item("result_with_attributes", result)