from kivy.properties import DictProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import Screen
from kivy.uix.widget import Widget
import hashlib

from key_rings.enumerations import ALGORITHM
from rsa_util import rsa_util


class ValidationPopup(FloatLayout):
    pass


class InputPasswordPopup(FloatLayout):
    data = DictProperty({})

    def confirm(self):
        if 'password' not in self.data:
            return

        password = self.data['password']
        name = self.data['name']
        email = self.data['email']
        key_size = self.data['key_size']
        algorithm = ALGORITHM.RSA if self.data['algorithm'] == 'RSA' else ALGORITHM.ELGAMAL
        sha_password = hashlib.sha512(str(password).encode())
        (public, priv) = rsa_util.generate_keys(key_size)
        print(sha_password.hexdigest())
    pass


class GenerateKeysScreen(Screen):
    data = DictProperty({})
    validation_popup_window: Popup = None
    input_password_popup_window: Popup = None

    def show_validation_popup(self):
        show = ValidationPopup()
        self.validation_popup_window = Popup(title="Validation error", content=show,
                                             size_hint=(None, None), size=(200, 200))
        self.validation_popup_window.open()

    def show_input_password_popup(self):
        show = InputPasswordPopup()
        show.data = self.data
        self.input_password_popup_window = Popup(title="Input password", content=show,
                                                 size_hint=(None, None), size=(200, 200))
        self.input_password_popup_window.open()

    def close_validation_popup(self):
        self.validation_popup_window.dismiss()

    def close_input_password_popup(self):
        self.input_password_popup_window.dismiss()

    def confirm(self):
        if 'name' not in self.data or 'email' not in self.data or 'key_size' not in self.data or 'algorithm' not in self.data:
            self.show_validation_popup()
            return False

        self.show_input_password_popup()
