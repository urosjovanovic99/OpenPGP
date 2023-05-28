from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.modalview import ModalView
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.screenmanager import Screen
from kivy.uix.textinput import TextInput

from key_rings.private_key_ring import PrivateKeyRing, privateKeyRing
from key_rings.private_key_utils import get_private_key_by_id, get_property_by_value, compare_passwords


class PrivateKeyRingExtended(PrivateKeyRing):
    def __init__(self, e, keyId, d, n, email, algorithm, name, keySize, Id):
        super(PrivateKeyRingExtended, self).__init__(e, keyId, d, n, email, algorithm, name, keySize)
        self.Id = Id


class CustomModalView(ModalView):
    def __init__(self, text, **kwargs):
        super(CustomModalView, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        self.text = text

        label = Label(text=self.text, font_size='12sp', color=(0.5, 0.5, 1, 1),
                      text_size=(self.width - 20, None), max_lines=100)
        layout.add_widget(label)

        close_button = Button(text="Close", size_hint=(None, None), size=(100, 50),
                              background_color=(0.2, 0.7, 0.3, 1), font_size='18sp')

        close_button.bind(on_release=self.dismiss)
        layout.add_widget(close_button)

        self.add_widget(layout)


class PasswordModalView(ModalView):
    def __init__(self, on_confirm, **kwargs):
        super(PasswordModalView, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')

        password_input = TextInput(multiline=False, password=True, hint_text="Password")
        layout.add_widget(password_input)

        confirm_button = Button(text="Confirm", size_hint=(None, None), size=(100, 50),
                                background_color=(0.2, 0.7, 0.3, 1), font_size='18sp')
        confirm_button.bind(on_release=lambda instance: on_confirm(password_input.text))
        layout.add_widget(confirm_button)

        close_button = Button(text="Cancel", size_hint=(None, None), size=(100, 50),
                              background_color=(0.8, 0.2, 0.3, 1), font_size='18sp')
        close_button.bind(on_release=self.dismiss)
        layout.add_widget(close_button)

        self.add_widget(layout)


class CustomLabel(RecycleDataViewBehavior, Label):
    id = None
    name = None
    selectedKey = None
    password_modal_view = None

    def __init__(self, **kwargs):
        super(CustomLabel, self).__init__(**kwargs)
        self.selected = False

    def refresh_view_attrs(self, rv, index, data):
        self.index = index
        return super(CustomLabel, self).refresh_view_attrs(rv, index, data)

    def on_touch_down(self, touch):
        if super(CustomLabel, self).on_touch_down(touch):
            return True
        if self.collide_point(*touch.pos):
            if touch.button == 'left':
                self.selected = not self.selected
                if self.selected:
                    self.on_selected()
                else:
                    pass

                return True

    def on_selected(self):
        self.selectedKey = get_private_key_by_id(self.id)

        if self.name != 'N' and self.name != 'D' and self.name != "Action":
            return
        if self.name == 'D':
            self.open_password_modal()
            return
        if self.name == "Action":
            self.show_actions()
            return

        text = f"{self.name}: {get_property_by_value(self.name, self.selectedKey)}"
        modal_view = CustomModalView(text=text)
        modal_view.open()


    def show_actions(self):
        modal_view = CustomModalView(text="Actions")

        grid_layout = GridLayout(cols=1, spacing=10, size_hint_y=None, height=150)

        delete_button = Button(text="Delete", size_hint=(None, None), size=(100, 50),
                               background_color=(0.8, 0.2, 0.3, 1), font_size='18sp')
        # delete_button.bind(on_release=self.delete_selected_key)
        grid_layout.add_widget(delete_button)

        export_button = Button(text="Export", size_hint=(None, None), size=(100, 50),
                               background_color=(0.2, 0.7, 0.3, 1), font_size='18sp')
        # export_button.bind(on_release=self.export_selected_key)
        grid_layout.add_widget(export_button)


        modal_view.add_widget(grid_layout)
        modal_view.open()

    def open_password_modal(self):
        def on_confirm(password):
            if compare_passwords(password, self.selectedKey):
                self.password_modal_view.dismiss()
                key = get_private_key_by_id(self.id)
                text = f"{self.name}: {get_property_by_value(self.name, key)}"
                modal_view = CustomModalView(text=text)
                modal_view.open()
            else:
                print("Incorrect password")

        self.password_modal_view = PasswordModalView(on_confirm=on_confirm)
        self.password_modal_view.open()


class DeleteKeysScreen(Screen):
    def on_enter(self):
        converted_objects = {}

        for index, obj in enumerate(privateKeyRing):
            converted_object = {
                'E': obj.e,
                'KeyId': obj.keyId,
                'D': obj.d,
                'N': obj.n,
                'Email': obj.email,
                'Algorithm': obj.algorith,
                'Name': obj.name,
                'KeySize': obj.keySize,
                'Action': 'ACTION',
                'Id': obj.id
            }
            converted_objects[index] = converted_object

        column_titles = [
            "E",
            "KeyId",
            "D",
            "N",
            "Email",
            "Algorithm",
            "Name",
            "Key size",
            "Actions"
        ]

        rows_length = len(privateKeyRing)
        self.columns = len(column_titles)

        table_data = []
        for y in column_titles:
            table_data.append(
                {'text': str(y), 'size_hint_y': None, 'height': 30, 'color': (.05, .30, .80, 1)})

        for z in range(rows_length):
            for y in converted_objects[z].keys():
                if y == 'Id':
                    continue
                table_data.append({'text': str(converted_objects[z][y]) if y != 'N' and y != 'D' else "",
                                   'size_hint_y': None,
                                   'height': 20,
                                   'color': (.06, .25, .50, 1),
                                   'id': converted_objects[z]['Id'],
                                   'name': y})

        self.ids.table_floor_layout.cols = self.columns
        self.ids.table_floor.data = table_data
