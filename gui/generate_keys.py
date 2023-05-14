from kivy.properties import DictProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import Screen
from kivy.uix.widget import Widget


class ValidationPopup(FloatLayout):
    pass


class InputPasswordPopup(FloatLayout):
    data = DictProperty({})
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
        self.validation_popup_window = Popup(title="Input password", content=show,
                                             size_hint=(None, None), size=(200, 200))
        self.validation_popup_window.open()

    def close_validation_popup(self):
        self.validation_popup_window.dismiss()

    def close_input_password_popup(self):
        self.input_password_popup_window.dismiss()

    def confirm(self):
        if not ('name' in self.data and 'email' in self.data and 'key_size' in self.data and 'algorithm' in self.data):
            self.show_validation_popup()
            print('All fields are required')
            return False

        # need generate key logic
        print(self.data)
        self.show_input_password_popup()
