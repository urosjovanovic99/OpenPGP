import string

from kivy.properties import DictProperty
from kivy.uix.screenmanager import Screen


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
