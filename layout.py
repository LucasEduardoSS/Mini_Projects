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
    def add_task(self):
        tasks.append({'Nome': 'Debugar Código', 'Peso': 5})


# Janela de Adicionar Pessoa
class AddPersonMenu(Screen):
    id = 1

    def add_person(self, nome, cargo):
        people.append({'Id': self.id, 'Nome':  nome, 'Cargo': cargo})
        self.id += 1
        print('Pessoa adicionada com sucesso')


# Janela de Adicionar Tarefa
class AddTaskMenu(Screen):
    id = 1
    
    def add_task(self, nome, peso):
        tasks.append({'Id': self.id, 'Nome': nome, 'Peso': peso})
        self.id += 1
        print('Tarefa adicionada com sucesso')


# Janela de Remover Registro
class RemoveRecordMenu(Screen):
    pass


# Janela de Remover Pessoa
class RemovePersonMenu(Screen):
    def remove_person(self, id):
        for person in people:
            if str(person["Id"]) == id:
                people.remove(person)
                print('Pessoa removida com sucesso')


# Janela de Remover Tarefa
class RemoveTaskMenu(Screen):
    def remove_task(self, id):
        for task in tasks:
            if str(task["Id"]) == id:
                tasks.remove(task)
                print('Tarefa removida com sucesso')


# Gerenciador de Janelas
class MenuScreenManager(ScreenManager):
    pass
