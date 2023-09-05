from kivy.uix.screenmanager import ScreenManager, Screen
from data import *


# Janela principal
class MainMenu(Screen):
    def on_press_records(self):
        pass

    def divideTasks(self):
        pass

# Janela de Visualização
class ViewMenu(Screen):
    def view_people(self):
        for person in people:
            print(person)
    
    def view_tasks(self):
        for task in tasks:
            print(task)
    
    def view_all(self):
        # Imprime as pessoas
        print('Pessoas: ')
        for person in people:
            print(person)
        
        # Imprime as tarefas
        print('Tarefas: ')
        for task in tasks:
            print(task)


# Janela de Registros
class RecordsMenu(Screen):
    def add_record(self):
        pass


# Janela de Adicionar Registro
class AddRecordMenu(Screen):
    def add_person(self):
        people.append({'Nome': 'Lucas', 'Cargo': 'Programação'})

    def add_task(self):
        tasks.append({'Nome': 'Debugar Código', 'Peso': 5})


# Janela de Adicionar Tarefa
class RemoveRecordMenu(Screen):
    def remove_person(self):
        print('Remover pessoa')

    def remove_task(self):
        print('Remvoer tarefa')
    

# Gerenciador de Janelas
class MenuScreenManager(ScreenManager):
    pass
