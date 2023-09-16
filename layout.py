from kivy.uix.screenmanager import ScreenManager, Screen
from data import *
from main import Main
from functions import calc_average, get_weights


# Main Window
class MainMenu(Screen, Main):
    def divideTasks(self):
        weight_average = calc_average(get_weights(tasks))
        distributions


# Vizualization Menu Window
class ViewMenu(Screen):
    def view_people(self):
        for person in people:
            print(person)
    
    def view_tasks(self):
        for task in tasks:
            print(task)
    
    def view_all(self):
        # Imprime as pessoas
        print('People: ')
        for person in people:
            print(person)
        
        # Imprime as tarefas
        print('Tasks: ')
        for task in tasks:
            print(task)


# Records Menu Window
class RecordsMenu(Screen):
    pass


# Add Record Menu Window
class AddRecordMenu(Screen):
    pass


# Add Person Menu Window
class AddPersonMenu(Screen):
    id = 1

    def add_person(self, name, job):
        people.append({'Id': self.id, 'Name': name, 'Job': job})
        self.id += 1
        print('Successfully added person record!')


# Add Task Menu Window
class AddTaskMenu(Screen):
    id = 1
    
    def add_task(self, name, weight):
        tasks.append({'Id': self.id, 'Name': name, 'Weight': int(weight)})
        self.id += 1
        print('Successfully added task record!')


# Remove Records Menu Window
class RemoveRecordMenu(Screen):
    pass


# Remove Person Menu Window
class RemovePersonMenu(Screen):
    def remove_person(self, id):
        for person in people:
            if str(person["Id"]) == id:
                people.remove(person)
                print('Successfully removed person record!')


# Remove Task Menu Window
class RemoveTaskMenu(Screen):
    def remove_task(self, id):
        for task in tasks:
            if str(task["Id"]) == id:
                tasks.remove(task)
                print('Successfully removed task record!')


# Alter Record Menu Window
class AlterRecordMenu(Screen):
    pass


# Alter Person Menu Window
class AlterPersonMenu(Screen):
    def alter_person(self, id, name='name', job='job'):
        for person in people:
            if str(person['Id']) == id:
                if name != 'name' and job != 'weight':
                    person['Name'] = name
                    person['Job'] = job
                    print('Successfully altered record\'s name and job')

                else:
                    if name != 'name':
                        person['Name'] = name
                        print('Successfully altered record\'s name')
                    
                    if job != 'weight':
                        person['Wight'] = job
                        print('Successfully altered record\'s job')
                

# Alter Task Menu Window
class AlterTaskMenu(Screen):
    def alter_task(self, id, name='name', weight='weight'):
        for task in tasks:
            if str(task['id']) == id:
                if name != 'name' and weight != 'weight':
                    task['Name'] = name
                    task['Weight'] = weight
                    print('Sucessfully changed record\'s name and weight!')
                
                else:
                    if name != 'name':
                        task['Name'] = name
                        print('Sucessfully changed record\'s name!')
                    
                    if weight != 'weight':
                        task['Weight'] = weight
                        print('Sucessfully changed record\'s weight!')


# Windows Manger
class MenuScreenManager(ScreenManager):
    pass
