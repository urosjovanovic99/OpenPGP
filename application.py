from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager

from gui.generate_keys.generate_keys import GenerateKeysScreen
from gui.import_export.import_key import ImportKeyScreen
from gui.main_screen.openPGP import OpenPGP


class OpenPGPApp(App):
    def build(self):
        return screen_manager


def load_gui():
    Builder.load_file('gui/generate_keys/generate_keys.kv')
    Builder.load_file('gui/import_export/import_key.kv')
    Builder.load_file('gui/main_screen/openPGP.kv')


if __name__ == '__main__':
    load_gui()
    screen_manager = ScreenManager()
    screen_manager.add_widget(OpenPGP(name="open_pgp_screen"))
    screen_manager.add_widget(GenerateKeysScreen(name="generate_keys_screen"))
    screen_manager.add_widget(ImportKeyScreen(name="import_key_screen"))
    OpenPGPApp().run()
