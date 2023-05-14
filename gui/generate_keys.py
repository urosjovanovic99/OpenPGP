import string

from kivy.properties import DictProperty
import datetime

from kivy.uix.screenmanager import Screen

from key_rings.private_key_ring import privateKeyRing, PrivateKeyRing
from rsa_util.rsa_util import generate_keys


class GenerateKeysScreen(Screen):
    data = DictProperty({})

    def confirm(self):
        if not ('name' in self.data and 'email' in self.data and 'key_size' in self.data and 'algorithm' in self.data):
            # need popup dialog here
            print('All fields are required')
            return False

        # need generate key logic
        print(self.data)

    pass
