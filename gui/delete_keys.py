from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import json
from kivy.uix.boxlayout import BoxLayout

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.properties import BooleanProperty, ListProperty, StringProperty, ObjectProperty
from kivy.uix.recyclegridlayout import RecycleGridLayout
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.recycleview.layout import LayoutSelectionBehavior
from kivy.uix.popup import Popup

from key_rings.private_key_ring import PrivateKeyRing, privateKeyRing


class DeleteKeysScreen(Screen):
    def on_enter(self):

        converted_objects = {}

        for index, obj in enumerate(privateKeyRing):
            converted_object = {
                0: obj.e,
                1: obj.keyId,
                2: obj.email,
                3: obj.algorith,
                4: obj.name,
                5: obj.keySize
            }
            converted_objects[index] = converted_object

        ring = PrivateKeyRing(None, None, None, None, None, None, None, None, None, None)
        column_titles = [
            "e",
            "keyId",
            "email",
            "algorithm",
            "name",
            "keySize",
        ]

        rows_length = len(privateKeyRing)
        self.columns = len(column_titles)

        table_data = []
        for y in column_titles:
            table_data.append(
                {'text': str(y), 'size_hint_y': None, 'height': 30, 'bcolor': (.05, .30, .80, 1)})  # append the data

        for z in range(rows_length):
            for y in range(self.columns):
                table_data.append({'text': str(converted_objects[z][y]), 'size_hint_y': None, 'height': 20,
                                   'bcolor': (.06, .25, .50, 1)})  # append the data

        self.ids.table_floor_layout.cols = self.columns  # define value of cols to the value of self.columns
        self.ids.table_floor.data = table_data  # add table_data to data value
