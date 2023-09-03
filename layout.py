from kivy.uix.screenmanager import ScreenManager, Screen

menu_add_record_opacity = 0


class MainMenu(Screen):
    def on_press_registros(self):
        pass

    def divideTasks(self):
        pass


class RegistersMenu(Screen):
    def add_person(self):
        menu_add_record_opacity = 1
        return menu_add_record_opacity
    

class MenuScreenManager(ScreenManager):
    pass
