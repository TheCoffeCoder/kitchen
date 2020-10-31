from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.properties import StringProperty,NumericProperty
from kivy.uix.button import Button
from kivymd.uix.list import TwoLineListItem, ThreeLineAvatarIconListItem,ThreeLineAvatarListItem
from kivy.uix.image import Image
from kivymd.uix.behaviors import RectangularElevationBehavior

from kivymd.app import MDApp


class Progressbar_image(Image):
    source = StringProperty('check.png')
    pass


class Progress_image(Image):
    pass


class Detail(GridLayout):

    pass


class Bar(GridLayout,RectangularElevationBehavior):
    pass


class Final(BoxLayout):
    pass


class Food_list(TwoLineListItem):
    text = StringProperty("burger")
    secondary_text = StringProperty("2")


class Customer_list(ThreeLineAvatarListItem):
    tertiary_text = StringProperty("Raihan")
    secondary_text = StringProperty("05615205123")


class Raider_list(ThreeLineAvatarIconListItem):
    secondary_text = StringProperty("Hakim")
    tertiary_text = StringProperty("0171165120")



class MainApp(MDApp):
    pass

MainApp().run()
