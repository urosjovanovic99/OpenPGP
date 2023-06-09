from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager

from gui.delete_keys.delete_keys import DeleteKeysScreen

from gui.generate_keys.generate_keys import GenerateKeysScreen
from gui.import_key.import_key import ImportKeyScreen
from gui.main_screen.open_pgp import OpenPGP


class OpenPGPApp(App):
    def build(self):
        return screen_manager


def load_gui():
    Builder.load_file('gui/generate_keys/generate_keys.kv')
    Builder.load_file('gui/import_key/import_key.kv')
    Builder.load_file('gui/main_screen/open_pgp.kv')
    Builder.load_file('gui/delete_keys/delete_keys.kv')


if __name__ == '__main__':
    load_gui()
    screen_manager = ScreenManager()
    screen_manager.add_widget(OpenPGP(name="open_pgp_screen"))
    screen_manager.add_widget(GenerateKeysScreen(name="generate_keys_screen"))
    screen_manager.add_widget(ImportKeyScreen(name="import_key_screen"))
    screen_manager.add_widget(DeleteKeysScreen(name="delete_keys"))
    OpenPGPApp().run()
