import os
from os.path import dirname

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager

from gui.generate_keys import GenerateKeysScreen
from gui.openPGP import OpenPGP


class OpenPGPApp(App):
    def build(self):
        return screen_manager


def load_gui():
    Builder.load_file('./gui/generate_keys.kv')
    Builder.load_file('./gui/openPGP.kv')


if __name__ == '__main__':
    load_gui()
    screen_manager = ScreenManager()
    screen_manager.add_widget(OpenPGP(name="screen_two"))
    screen_manager.add_widget(GenerateKeysScreen(name="screen_one"))
    OpenPGPApp().run()
