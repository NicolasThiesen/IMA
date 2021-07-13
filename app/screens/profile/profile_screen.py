from kivy.uix.screenmanager import Screen
from modules.session_manager import set_profile
from kivy.factory import Factory

class ProfileScreen(Screen):

    def __init__(self, **kwargs):
        super(ProfileScreen, self).__init__(**kwargs)

    def handle_add(self, Alert):
        _profile_name = self.ids.perfil_name.text
        _mfa_serial = self.ids.mfa_serial.text
        _role_arn = self.ids.role_arn.text
        if "" not in [_profile_name, _mfa_serial, _role_arn]:
            set_profile(_profile_name, _mfa_serial, _role_arn)
            alert = Alert(title="Status")
            alert.ids.alert_text.text = f"Os items foram inseridos com sucesso!\nPerfil Criado: [b]{_profile_name}[/b]"
            self.ids.perfil_name.text, self.ids.mfa_serial.text, self.ids.role_arn.text = "", "", ""
        else:
            alert = Alert(title="Erro")
            alert.ids.alert_text.text = "Você precisa preencher todos os campos"
        alert.open()
