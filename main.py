from kivy.app import App

from kivy.core.window import Window
from kivy.lang.builder import Builder
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
import layout

Window.clearcolor = (0, 0, 0, 0)
Window.size = (1270, 720)
Window.minimum_width = 850
Window.minimum_height = 500


class Main(Widget):
    pass


class TaskDividerApp(App):
    def build(self):
        return Main()


if __name__ == '__main__':
    TaskDividerApp().run()
