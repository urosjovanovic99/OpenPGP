import string

from kivy.properties import DictProperty
from kivy.uix import popup
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import Screen


# close dialog method needs to be implemented
class Popups(FloatLayout):
    pass


class GenerateKeysScreen(Screen):
    data = DictProperty({})

    def show_popup(self):
        show = Popups()
        popup_window = Popup(title="Validation error", content=show,
                             size_hint=(None, None), size=(200, 200))
        popup_window.open()

    def confirm(self):
        if not ('name' in self.data and 'email' in self.data and 'key_size' in self.data and 'algorithm' in self.data):
            self.show_popup()
            print('All fields are required')
            return False

        # need generate key logic
        print(self.data)
