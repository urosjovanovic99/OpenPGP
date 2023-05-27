from kivy.uix.label import Label
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.screenmanager import ScreenManager, Screen
from key_rings.private_key_ring import PrivateKeyRing, privateKeyRing


class CustomLabel(RecycleDataViewBehavior, Label):
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
                    # self.bcolor = (0.06, 0.25, 0.50, 1)
                    self.on_selected()
                else:
                    # self.bcolor = (1, 1, 1, 1)
                    pass

                return True

    def on_selected(self):
        print(f"Selected: {self.text}")


class DeleteKeysScreen(Screen):
    def on_enter(self):

        converted_objects = {}

        for index, obj in enumerate(privateKeyRing):
            converted_object = {
                0: obj.e,
                1: obj.keyId,
                2: obj.d,
                3: obj.n,
                4: obj.email,
                5: obj.algorith,
                6: obj.name,
                7: obj.keySize,
            }
            converted_objects[index] = converted_object

        column_titles = [
            "e",
            "keyId",
            "d",
            "n",
            "email",
            "algorithm",
            "name",
            "keySize"
        ]

        rows_length = len(privateKeyRing)
        self.columns = len(column_titles)

        table_data = []
        for y in column_titles:
            table_data.append(
                {'text': str(y), 'size_hint_y': None, 'height': 30, 'color': (.05, .30, .80, 1)})  # append the data

        for z in range(rows_length):
            for y in range(self.columns):
                table_data.append({'text': str(converted_objects[z][y]), 'size_hint_y': None, 'height': 20,
                                   'color': (.06, .25, .50, 1)})  # Dodajte on_press atribut

        self.ids.table_floor_layout.cols = self.columns
        self.ids.table_floor.data = table_data

