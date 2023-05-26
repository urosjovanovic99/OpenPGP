import os

from kivy.properties import ObjectProperty, DictProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import Screen

from key_rings.private_key_ring import privateKeyRing
from key_rings.public_key_ring import publicKeyRing
from rsa_util.rsa_util import import_from_file

from key_rings.enumerations import KEY


class LoadDialog(FloatLayout):
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)


class SaveDialog(FloatLayout):
    save = ObjectProperty(None)
    text_input = ObjectProperty(None)
    cancel = ObjectProperty(None)


class ImportKeyScreen(Screen):
    data = DictProperty({})
    loadfile = ObjectProperty(None)
    savefile = ObjectProperty(None)
    text_input = ObjectProperty(None)

    def dismiss_popup(self):
        self._popup.dismiss()

    def show_load(self):
        content = LoadDialog(load=self.load, cancel=self.dismiss_popup)
        self._popup = Popup(title="Load file", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()

    def show_save(self):
        content = SaveDialog(save=self.save, cancel=self.dismiss_popup)
        self._popup = Popup(title="Save file", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()

    def load(self, path, filename):
        file_path = os.path.join(path, filename[0])
        if 'key_type' in self.data:
            with open(file_path) as stream:
                self.text_input.text = stream.read()
            key_type = KEY.PUBLIC if self.data['key_type'] == 'PUBLIC' else KEY.PRIVATE
            key = import_from_file(file_path, key_type)
            publicKeyRing.append(key) if key_type == KEY.PUBLIC else privateKeyRing.append(key)

        self.dismiss_popup()

