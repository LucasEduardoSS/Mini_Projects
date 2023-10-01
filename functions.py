def calc_tasks(people: dict, tasks: list, average_weight: float, view_distru=False):
    """Analyze and assigne tasks for each person fairly."""

    from time import sleep
    from random import randint

    analyzed_tasks = [] 
    assigned_tasks = []
    count = temp_smallest_task_weight = 0
    
    for person in people:
            ''' Primarily, the algorithm select and assign tasks, until the
            assigned weight achives a value about the average. Then, if possible,
            searchs for a task with a weight which can aproximate even more the
            assigned weight. '''

            # Create an person element for storing the TOTAL TASKS WEIGHT
            person["TTW"] = 0

            while len(analyzed_tasks) < (len(tasks) - len(assigned_tasks)):
                # Stores an index for a random task
                task_index = randint(0, len(tasks) - 1)

                # Avoid selecting a already selected task
                while task_index in analyzed_tasks or task_index in assigned_tasks:
                    if view_distru:
                        print(f'Alterando tarefa {tasks[task_index]["Name"]} ', end="")
                        
                    task_index = randint(0, len(tasks) - 1)

                    if view_distru:
                        print(f'para {tasks[task_index]["Name"]}...'), sleep(3)

                # Temporary task
                temp_task = tasks[task_index].copy()

                # Shows that the task can be analyzed
                if view_distru:  
                    print(f'Analisando tarefa {temp_task["Name"]}...'), sleep(3)

                # Assigne a task if the total weight keeps below the avarege
                if (person["TTW"] + temp_task["Weight"]) <= average_weight:
                    person["Tasks"].append(temp_task["Name"])
                    person["TTW"] += temp_task["Weight"]
                    assigned_tasks.append(task_index)

                    # Shows the task was assgined
                    if view_distru:
                        print(f'Tarefa {temp_task["Name"]} atribuida a {person["Name"]}.')
                        sleep(3)

                # Analyze the tasks and tries a aproximation from up
                else:
                    # Module of the difference between the person's total tasks weight and the average weight
                    diff = ((average_weight - person["TTW"])**2)**0.5
                    
                    # Shows it passed the fisrt test
                    if view_distru:
                        print("test 1 - Total tasks weight higher then the average: Passed")
                        sleep(2)

                    # Analyze the tasks
                    for pos, task in enumerate(tasks):
                        if pos not in assigned_tasks:
                            
                            # Shows it passed the second test
                            if view_distru:  
                                print("Test 2 - The task isn't already assigned: Passed")
                                sleep(2)
                            
                            # First analyzed task
                            if count == 0:
                                # Shows it passed the third test
                                if view_distru:  
                                    print("Test 3 - Empty analized tasks list: Passed"), sleep(2)

                                # Smaller difference
                                smallest_diff = (person["TTW"] + task["Weight"]) - average_weight
                                count += 1
                            
                            # Verifies the other tasks
                            else:
                                # Stores the current task weight difference
                                current_task_diff = person["TTW"] + task["Weight"] - average_weight

                                # Verifies if the weight diff is smaller the than smallest
                                if current_task_diff < smallest_diff:
                                    
                                    # Shows is passed the forth test
                                    if view_distru:  
                                        print("Test 4 - Task analyzed with smaller difference: Passed")
                                        sleep(2)
                                    
                                    # New smallest difference
                                    smallest_diff = (person["TTW"] + task["Weight"]) - average_weight

                                    # Temporary smallest task weight storing variable
                                    temp_smallest_task_weight = task.copy()

                    # Assigne the smallest weight difference task
                    if temp_smallest_task_weight != 0:

                        person["Tasks"].append(temp_smallest_task_weight["Name"])
                        person["TTW"] += temp_smallest_task_weight["Weight"]
                        assigned_tasks.append(tasks.index(temp_smallest_task_weight))

                        # Shows if the aproximation was successfull
                        if view_distru:
                            print("test 5 - Weight aproximation: Passed")
                            sleep(2)

                temp_task.clear()
                analyzed_tasks.append(task_index)

                # Shows the analyzed tasks
                if view_distru:
                    print("Tarefas Analisadas:", analyzed_tasks)
                    sleep(3)

            analyzed_tasks.clear()
            count = 0

tarefas = [{'Name': 'Depurar Código', 'Weight': 5},
           {'Name': 'Participar de Reuniao', 'Weight': 10}]

pessoas = [{'Name': 'Lucas', 'Tasks': []},
           {'Name': 'Saulo', 'Tasks': []}]

# print(calc_average(get_weights(tarefas)))
