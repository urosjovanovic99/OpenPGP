
from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label

from key_rings.private_key_ring import privateKeyRing


class DeleteKeysScreen(Screen):

    def __init__(self, **kwargs):
        super(DeleteKeysScreen, self).__init__(**kwargs)

    def on_enter(self):
        self.populate_data()

    def populate_data(self):
        box_layout = self.ids.box_layout
        box_layout.clear_widgets()  # Clear existing widgets before populating new data

        for obj in privateKeyRing:
            properties = vars(obj)
            for key, value in properties.items():
                if key is "hashedPassword" or key is "d":
                    continue
                label_key = Label(text=key.capitalize(), size_hint=(0.4, None), height='30dp')
                label_value = Label(text=str(value), size_hint=(0.6, None), height='30dp')
                box_layout.add_widget(label_key)
                box_layout.add_widget(label_value)

            # Add a separator line between iterations
            separator = Label(text='-----------------', size_hint=(1, None), height='2dp')
            box_layout.add_widget(separator)
