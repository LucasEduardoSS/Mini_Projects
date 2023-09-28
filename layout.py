from kivy.uix.screenmanager import ScreenManager, Screen
from data import *
from main import Main
from functions import *
from classes import *


# Main Window
class MainMenu(Screen, Main):
    def divideTasks(self):
        weight_average = calc_average(get_weights(Task.tasks))
        # distributions


# Vizualization Menu Window
class ViewMenu(Screen):
    def view_people(self):
        for person in Person.people:
            person.__repr__()
    
    def view_tasks(self):
        for task in Task.tasks:
            task.__repr__()
    
    def view_all(self):
        # Imprime as pessoas
        print('People: ')
        for person in Person.people:
            person.__repr__()
        
        # Imprime as tarefas
        print('Tasks: ')
        for task in Task.tasks:
            task.__repr__()


# Records Menu Window
class RecordsMenu(Screen):
    pass


# Add Record Menu Window
class AddRecordMenu(Screen):
    pass


# Add Person Menu Window
class AddPersonMenu(Screen):
    def add_person(self, name: str, sector: str, job: str):
        try:
            Person(name, sector, job)
            print('Successfully added person record!')

        except ValueError:
            print('Incorrect value.')
        except TypeError:
            print('Incorrect type')


# Add Task Menu Window
class AddTaskMenu(Screen):

    def add_task(self, name, weight):
        # new_weight_variance = 

        Task(name, int(weight))
        print('Successfully added task record!')


# Remove Records Menu Window
class RemoveRecordMenu(Screen):
    pass


# Remove Person Menu Window
class RemovePersonMenu(Screen):
    def remove_person(self, id):
        for person in Person.people:
            if str(person.id) == id:
                Person.people.remove(person)
                print('Successfully removed person record!')


# Remove Task Menu Window
class RemoveTaskMenu(Screen):
    def remove_task(self, id):
        for task in Task.tasks:
            if str(task.id) == id:
                Task.tasks.remove(task)
                print('Successfully removed task record!')


# Alter Record Menu Window
class AlterRecordMenu(Screen):
    pass


# Alter Person Menu Window
class AlterPersonMenu(Screen):
    def alter_person(self, id, name='name', job='job'):
        for person in Person.people:
            if str(person.id) == id:
                if name != 'name' and job != 'weight':
                    person.name = name
                    person.job = job
                    print('Successfully altered record\'s name and job')

                else:
                    if name != 'name':
                        person.name = name
                        print('Successfully altered record\'s name')
                    
                    if job != 'job':
                        person.job = job
                        print('Successfully altered record\'s job')
                

# Alter Task Menu Window
class AlterTaskMenu(Screen):
    def alter_task(self, id, name='name', weight='weight'):
        for task in Task.tasks:
            if str(task.id) == id:
                if name != 'name' and weight != 'weight':
                    task.name = name
                    task.weight = weight
                    print('Sucessfully changed record\'s name and weight!')
                
                else:
                    if name != 'name':
                        task.name = name
                        print('Sucessfully changed record\'s name!')
                    
                    if weight != 'weight':
                        task.weight = weight
                        print('Sucessfully changed record\'s weight!')


# Windows Manger
class MenuScreenManager(ScreenManager):
    pass
