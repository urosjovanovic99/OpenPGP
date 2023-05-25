import struct

from kivy.properties import DictProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import Screen
from kivy.uix.widget import Widget
import hashlib
from datetime import date

from des3_utils.des3_utils import encrypt, derive_key_from_password, generate_salt, int_to_bytes, decrypt, bytes_to_int, \
    perform_encrypt, perform_decrypt
from key_rings.enumerations import ALGORITHM
from key_rings.private_key_ring import privateKeyRing, PrivateKeyRing
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

        (public, private) = rsa_util.generate_keys(int(key_size))

        key, encrypt_d = perform_encrypt(private.d, password)

        mask = (1 << 64) - 1

        privateKeyRing.append(PrivateKeyRing(date.today(), public.e, encrypt_d, private.n, email, algorithm, name, int(key_size), key, public.e & mask))


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
