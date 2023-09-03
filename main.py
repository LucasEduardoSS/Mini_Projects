from kivy.app import App

from kivy.core.window import Window
from kivy.lang.builder import Builder
from kivy.uix.widget import Widget
import layout

Window.clearcolor = (1, 1, 1, 1)
Window.size = (1270, 720)
Window.minimum_width = 850
Window.minimum_height = 500


class Main(Widget):
    pass


class TaskDividerApp(App):
    pass


if __name__ == '__main__':
    TaskDividerApp().run()
