from classes import *
from time import sleep
from random import choice
from statistics import pvariance

sleep_time = 1

def normal_distribution(people: list, tasks: list, view_distru=False):
    """Analyze and assigne tasks for each person fairly."""

    analyzed_tasks = []  # Stores the analyzed tasks
    analyzed_people = []  # Stores the analyzed people
    assigned_tasks = []  # Stores the assigned tasks
    selected_tasks = []  # Stores the selected tasks for the distru assign

    average_weight = sum(tasks[0].get_weights())/len(people)
    print(f'average weight: {average_weight}')
    
    for i in range(len(people)):
        '''  '''

        # Selects randomly a person
        current_person = choice(people)

        # Verifies if the current person is available
        while current_person in analyzed_people:
            current_person = choice(people)

        if view_distru:
            print('Analyzing person:', current_person.name), sleep(sleep_time)

        ttw = 0  # total task weight
        best_aproximation = ((ttw - average_weight)**2)**0.5

        while True:

            best_task = None
            
            if view_distru:
                print('Begining aproximation...'), sleep(sleep_time)

            # Analyze the tasks
            for task in tasks:
                # Verifies if the task was already assigned
                if task not in assigned_tasks:

                    # Add the current task to the analyzed tasks
                    analyzed_tasks.append(task) if task not in analyzed_tasks else None
                    
                    if view_distru:  
                        print(f"Analyzing task: {task.name}"), sleep(sleep_time)

                    # Stores the current task weight aproximation
                    current_task_aprox = ((ttw + task.weight - average_weight)**2)**0.5

                    # Verifies if other task weight fits better
                    if current_task_aprox <= best_aproximation:

                        # New best task
                        best_task = task
                        best_aproximation = current_task_aprox

                        if view_distru:  
                            print(f"New best task: {task.name}"), sleep(sleep_time)

            # Assigne the best task after all being analyzed
            if best_task != None:
                assigned_tasks.append(best_task)
                selected_tasks.append(best_task)
                ttw += best_task.weight

                # Show that a task was assigned
                if view_distru:
                    print(f'Task {best_task.name} assigned to {current_person.name}.'), sleep(sleep_time)

            if view_distru:
                print(f'{current_person.name} total weight: {ttw}'), sleep(sleep_time)
                print("Aproximation complete!"), sleep(sleep_time)

            # Breaks when can't aproximate more
            if best_task == None:
                break

        if view_distru:
            print("Tasks analyzed:", [task.name for task in analyzed_tasks]), sleep(sleep_time)

        # Creates the distribuition
        d1 = Distru(current_person, selected_tasks.copy())

        # Prepare the variables for a new iteration
        analyzed_people.append(current_person)
        analyzed_tasks.clear()
        selected_tasks.clear()

    if view_distru:
        print('Complete distribuition'), sleep(sleep_time)

    # if view_distru:
    Distru.distributions[-1].show_distrus()

def random_distribution(people: list, tasks: list, view_distru=False):
    """ Randomly distributes tasks """

    analyzed_people = []  # Stores who have been analyzed
    assigned_tasks = []  # Stores tasks that have been analyzed
    selected_tasks = []  # Stores the best tasks on each iteration

    # Avoid non integer tasks ratio
    if (len(tasks) % len(people)) == 0:
        # Calculate the task ratio
        tasks_qnt = int(len(tasks) / len(people))

        for i in range(len(people)):
            iter_person = choice(people)

            # Avoid duplicated person selection
            while iter_person in analyzed_people:
                iter_person = choice(people)

            for o in range(tasks_qnt):
                iter_task = choice(tasks)

                # Avoid duplicated task assignment
                while iter_task in assigned_tasks:
                    iter_task = choice(tasks)

                # Assign a random task
                selected_tasks.append(iter_task)
                assigned_tasks.append(iter_task)
            
            # Prepare for a new iteration
            d1 = Distru(iter_person, selected_tasks.copy())
            analyzed_people.append(iter_person)
            selected_tasks.clear()
    
    else:
        print('Impossível dividir aleatóriamente.')
    
    return d1.calc_distru_weight_variance()

def average_distribuition_variance(people: list, tasks: list, distru_method):
    sum = 0
    rep = 11

    # sums the variances for each distribution iteration
    if distru_method == 0:
        for i in range(1, rep):
            iter_variance = random_distribution(people, tasks)
            print(f'{i}° iteration variance: {iter_variance}')
            sum += iter_variance

    # sums the variances for each distribution iteration
    elif distru_method == 1:
        for i in range(1, rep):
            iter_variance = normal_distribution(people, tasks)
            print(f'{i}° iteration variance: {iter_variance}')
            sum += iter_variance
    
    print('Total average variance:', sum/rep)

# TESTING DATA - TASKS FOR 10 AVERAGE WEIGHT AND 3 PEOPLE
p1 = Person('Lucas', 'IT', 'Developer')
p2 = Person('Romali', 'TI', 'Developer')
p3 = Person('Saulo', 'TI', 'Developer')
t1 = Task('Create a user interface', 5)
t2 = Task('Debug Code', 7)
t3 = Task('Review a pull request', 3)
t4 = Task('Create a complex algorthm', 10)
t5 = Task('Update readme doc', 5)


# normal_distribution(Person.people, Task.tasks)
# random_distribution(Person.people, Task.tasks)
# average_distribuition_variance(Person.people, Task.tasks, 1)
