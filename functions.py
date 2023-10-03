from classes import *
from time import sleep
from random import choice

def calc_distribution(people: list, tasks: list, view_distru=False):
    """Analyze and assigne tasks for each person fairly."""

    analyzed_tasks = []  # Stores the analyzed tasks
    analyzed_people = []  # Stores the analyzed people
    assigned_tasks = []  # Stores the assigned tasks
    selected_tasks = []  # Stores the selected tasks for the distru assign

    average_weight = Task.weight_average
    
    for i in range(len(people)):
        ''' Primarily, the algorithm select and assign tasks, until the
        assigned weight achives a value about the average. Then, if possible,
        searchs for a task with a weight which can aproximate even more the
        assigned weight. '''

        # Selects randomly a person
        current_person = choice(people)

        # Verifies if the current person is available
        while current_person in analyzed_people:
            current_person = choice(people)

        # Shows the person being analyzed
        if view_distru:
            print('Analyzing person:', current_person.name), sleep(2)

        # Stores the current person total tasks weight
        TTW = 0

        # Select and assign tasks until reaches the average weight
        while len(analyzed_tasks) < (len(tasks) - len(assigned_tasks)):
            # Randomly selects a task
            current_task = choice(tasks)

            # Avoid selecting an already selected task
            while current_task in analyzed_tasks or current_task in assigned_tasks:

                if view_distru:  # Shows what task is being changed
                    print(f'Changing task: {current_task.name} ', end=""), sleep(2)
                
                # Randomly selects a task
                current_task = choice(tasks)

                if view_distru:  # Shows the changed to task
                    print(f'to {current_task.name}...'), sleep(2)

            if view_distru:  # Shows the task being analyzed 
                print(f'Analyzing task: \"{current_task.name}\"...'), sleep(2)

            # Assigne a task if the total weight keeps below the avarege
            if (TTW + current_task.weight) <= average_weight:
                selected_tasks.append(current_task)
                assigned_tasks.append(current_task)
                analyzed_tasks.append(current_task)
                TTW += current_task.weight

                # Shows the task was assgined
                if view_distru:
                    print(f'Task \"{current_task.name}\" assigned to {current_person.name}.'), sleep(2)
                
                print('Fisrt aproximation complete!'), sleep(2)

            else:
                ''' This is an important section, it searches for a task that can
                aproximate the current person total tasks weight to the average,
                verifying each unassigned task.'''

                print('Begining second aproximation...'), sleep(2)

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
                            print("Test 2 - The task isn't already assigned: Passed"), sleep(2)
                        
                        # First analyzed task
                        if best_task == None:
                            # Shows it passed the third test: first task
                            if view_distru:  
                                print("Test 3 - Empty analized tasks list: Passed"), sleep(2)

                            # Smallest difference
                            smallest_diff = (TTW + task.weight) - average_weight
                            best_task = task
                        
                        # Verifies the other tasks
                        else:
                            # Stores the current other task weight difference
                            current_task_diff = TTW + task.weight - average_weight

                            # Verifies if other task weight fits better
                            if current_task_diff < smallest_diff:
                                
                                # Shows that another task fits better
                                if view_distru:  
                                    print("Test 4 - Task analyzed with smaller difference: Passed"), sleep(2)
                                
                                # New smallest difference
                                smallest_diff = (TTW + task.weight) - average_weight

                                # New best task
                                best_task = task

                # Assigne the best task after all being analyzed
                if best_task != None:

                    selected_tasks.append(best_task)
                    assigned_tasks.append(best_task)
                    TTW += best_task.weight

                    # Shows if the aproximation was successfull
                    if view_distru:
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
        TTW = 0

    print('Complete distribuition'), sleep(2)

    # Show the distributions
    # if view_distru:
    d1.show_distrus()


p1 = Person('Lucas', 'IT', 'Developer')
p2 = Person('Romali', 'TI', 'Developer')
p3 = Person('Saulo', 'TI', 'Developer')

t1 = Task('Create a user interface', 5) 
t2 = Task('Debug Code', 7)
t3 = Task('Review a pull request', 3)
t4 = Task('Create a comple algorthm', 10)
t5 = Task('Update readme doc', 5)

calc_distribution(Person.people, Task.tasks, True)
