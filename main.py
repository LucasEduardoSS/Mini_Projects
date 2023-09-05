from kivy.app import App

from kivy.core.window import Window
from kivy.lang.builder import Builder
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty
from layout import *

Window.clearcolor = (1, 1, 1, 1)
Window.size = (1270, 720)
Window.minimum_width = 850
Window.minimum_height = 500


class MenuAddPerson(Widget):
    pass


class Main(RelativeLayout):
    pass    
        

class TaskDividerApp(App):
    pass


if __name__ == '__main__':
    TaskDividerApp().run()
