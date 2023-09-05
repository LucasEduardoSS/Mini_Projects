from kivy.uix.screenmanager import ScreenManager, Screen


class MainMenu(Screen):
    def on_press_records(self):
        pass

    def divideTasks(self):
        pass


class RecordsMenu(Screen):
    def add_record(self):
        pass


class AddRecordMenu(Screen):
    def add_person(self):
        print('Adicionar pessoa')

    def add_task(self):
        print('Adicionar tarefa')


class RemoveRecordMenu(Screen):
    def remove_person(self):
        print('Remover pessoa')

    def remove_task(self):
        print('Remvoer tarefa')
    

class MenuScreenManager(ScreenManager):
    pass
