from classes import *
from time import sleep
from random import choice

def normal_distribution(people: list, tasks: list, view_distru=False):
    """Analyze and assigne tasks for each person fairly."""

    analyzed_tasks = []  # Stores the analyzed tasks
    analyzed_people = []  # Stores the analyzed people
    assigned_tasks = []  # Stores the assigned tasks
    selected_tasks = []  # Stores the selected tasks for the distru assign

    average_weight = sum(tasks[0].get_weights())/len(people)
    print(f'average weight: {average_weight}'), sleep(2)
    
    for i in range(len(people)):
        ''' Primarily, in the first aproximation, the algorithm select and 
        assign tasks, until the assigned weight achives a value about the 
        average. Then, in the second aproximation, searchs for a task with 
        a weight which can aproximate even more the assigned weight. '''

        # Selects randomly a person
        current_person = choice(people)

        # Verifies if the current person is available
        while current_person in analyzed_people:
            current_person = choice(people)

        # Shows the person being analyzed
        if view_distru:
            print('Analyzing person:', current_person.name), sleep(2)

        # Stores the current person total tasks weight
        ttw = 0
        aproximation = 0

        ''' In this section, is made the fisrt aproximation '''

        # Select and assign tasks until reaches the average weight
        while True:
            
            # Randomly choses a task
            current_task = choice(tasks)

            # Verifies if the current task is unassigned
            if current_task not in assigned_tasks or current_task not in analyzed_tasks:

                # Shows what task is being analyzed
                if view_distru:
                    print(f'Analyzing task \"{current_task.name}\"'), sleep(2)

                # Assigne a task if the total weight keeps below the avarege
                if (ttw + current_task.weight) <= average_weight:
                    selected_tasks.append(current_task)
                    assigned_tasks.append(current_task)
                    analyzed_tasks.append(current_task)
                    ttw += current_task.weight
                    aproximation = ((current_task.weight + ttw - average_weight)**2)**0.5

                    # Shows the task was assgined
                    if view_distru:
                        print(f'Task \"{current_task.name}\" assigned to {current_person.name}.'), sleep(2)
                        print(f'{current_person.name} total weight: {ttw}'), sleep(2)
                
                else:
                    break
                    
        if view_distru:
            print('Fisrt aproximation complete!'), sleep(2)
            
        ''' In this section, is made the second aproximation '''

        if view_distru:
            print('Begining second aproximation...'), sleep(2)

        # Clear analyzed task list
        analyzed_tasks.clear()

        # Stores the best task
        best_task = None

        # Analyze the tasks
        for task in tasks:

            # Verifies if the task was already assigned
            if task not in assigned_tasks:

                # Add the current task to the analyzed tasks
                analyzed_tasks.append(task)
                
                # Shows it passed the second test
                if view_distru:  
                    print(f"Test 2 - The task {task.name} is unassigned: Passed"), sleep(2)

                # Verifies the other tasks
                else:
                    # Stores the current other task weight difference
                    current_task_diff = ((ttw + task.weight - average_weight)**2)**0.5

                    # Verifies if other task weight fits better
                    if current_task_diff < aproximation:
                        
                        # New smallest difference
                        aproximation = current_task_diff

                        # New best task
                        best_task = task

                        # Shows that another task fits better
                        if view_distru:  
                            print(f"Test 4 - New best task: {task.name}"), sleep(2)

        # Assigne the best task after all being analyzed
        if best_task != None:

            selected_tasks.append(best_task)
            assigned_tasks.append(best_task)
            ttw += best_task.weight

            # Shows if the aproximation was successfull
            if view_distru:
                print(f'{current_person.name} total weight: {ttw}'), sleep(2)
                print("Second Aproximation complete!"), sleep(2)

        # Shows the analyzed tasks
        if view_distru:
            print("Tasks analyzed:", [task.name for task in analyzed_tasks]), sleep(2)

        # Creates the distribuition
        d1 = Distru(current_person, selected_tasks.copy())

        # Prepare the variables for a new iteration
        analyzed_people.append(current_person)
        analyzed_tasks.clear()
        selected_tasks.clear()
        ttw = 0

    if view_distru:
        print('Complete distribuition'), sleep(2)

    # Show the distributions
    # if view_distru:
    d1.show_distrus()

def random_distribuion(people: list, tasks: list, view_distru=False):
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
    
    d1.show_distrus()

p1 = Person('Lucas', 'IT', 'Developer')
p2 = Person('Romali', 'TI', 'Developer')
p3 = Person('Saulo', 'TI', 'Developer')

t1 = Task('Create a user interface', 5) 
t2 = Task('Debug Code', 7)
t3 = Task('Review a pull request', 3)
t4 = Task('Create a comple algorthm', 10)
t5 = Task('Update readme doc', 5)
t6 = Task('Clean the floor', 5)



# calc_distribution(Person.people, Task.tasks)
random_distribuion(Person.people, Task.tasks)
