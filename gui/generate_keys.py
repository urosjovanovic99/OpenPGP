import datetime

from kivy.uix.screenmanager import Screen

from key_rings.private_key_ring import privateKeyRing, PrivateKeyRing
from rsa_util.rsa_util import generate_keys


class GenerateKeysScreen(Screen):
    def collect_data(self, name, email, key_size, algorithm):
        if algorithm == 'RSA':
            (publicKey, privateKey) = generate_keys(int(key_size))





