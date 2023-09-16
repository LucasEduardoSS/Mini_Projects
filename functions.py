def calc_average(_list: list):
    """Return the average of a list."""

    if len(_list) > 0:
        # List comprehension systas: newlist = [expression for item in iterable if condition == True]
        return sum([item for item in _list], 0)/len(_list)

    else:
        return 'Lista vazia'
    
def get_weights(_tasks: list):
    """Return a list with all weights from tasks"""

    return [task['Weight'] for task in _tasks]

def calc_tasks(people: dict, tasks: list, average_weight: float, view_distro=False):
    """Analyze and assigne tasks for each person fairly."""

    from time import sleep
    from random import randint

    analyzed_tasks = []
    assigned_tasks = []
    
    for person in people:
            ''' Primarily, the algorithm select and assign tasks, until the
            assigned weight achives a value about the average. Then, if possible,
            searchs for a task with a weight which can aproximate even more the
            assigned weight. '''

            while len(analyzed_tasks) < (len(tarefas) - len(assigned_tasks)):
                # Stores an index for a random task
                ind_tar = randint(0, len(tarefas) - 1)

                # Avoid selecting a already selected task
                while ind_tar in analyzed_tasks or ind_tar in assigned_tasks:
                    if view_distro:
                        print(f'Alterando tarefa {tarefas[ind_tar]["Nome"]} ', end="")
                        
                    ind_tar = randint(0, len(tarefas) - 1)

                    if view_distro:
                        print(f'para {tarefas[ind_tar]["Nome"]}...'), sleep(3)

                temp_tar = tarefas[ind_tar].copy()

                # Mostra que a tarefa pode ser analisada
                if view_distro:
                    print(f'Analisando tarefa {temp_tar["Nome"]}...'), sleep(3)

                # Atribui uma tarefa se manter o peso abaixo da media
                if person["Peso das Tarefas"] + temp_tar["Peso"] <= average_weight:
                    person["Tarefas"].append(temp_tar["Nome"])
                    person["Peso das Tarefas"] += temp_tar["Peso"]
                    assigned_tasks.append(ind_tar)

                    # Mostra que a tarefa foi atribuida a pessoa
                    if view_distro:
                        print(
                            f'Tarefa {temp_tar["Nome"]} atribuida a {person["Nome"]}.'
                        ), sleep(3)

                # Atribui uma tarefa se aproximar o peso pessoal do peso medio (Sempre vai ocorrer quando uma tarefa
                # com peso maior que o peso_medio estiver sendo executada)
                else:
                    # Module of the difference between the person's total tasks weight and the average weight
                    diff = ((average_weight - person["Peso das Tarefas"])**2)**0.5

                    if view_distro:  # Mostra passagem de teste
                        print("pass test 1"), sleep(2)

                    # Loop 4 - Analisa e atribui tarefas a pessoa caso fique mais proxima do limite de peso
                    for pos, t in enumerate(tarefas):
                        if pos not in assigned_tasks:

                            if view_distro:  # Mostra passagem de teste
                                print("pass test 2"), sleep(2)

                            if count == 0:

                                if view_distro:  # Mostra passagem de teste
                                    print("pass test 3"), sleep(2)

                                menor_dif = (
                                    person["Peso das Tarefas"] + t["Peso"]
                                ) - average_weight
                                count += 1
                            else:
                                if (
                                    person["Peso das Tarefas"] + t["Peso"]
                                ) - average_weight < menor_dif:

                                    if view_distro:  # Mostra passagem de teste
                                        print("pass test 4"), sleep(2)

                                    menor_dif = (
                                        p["Peso das Tarefas"] + t["Peso"]
                                    ) - average_weight
                                    temp_tar_men_peso = t.copy()

                    # Atribui a tarefa analizada com menor peso
                    if temp_tar_men_peso != 0:

                        if view_distro:  # Mostra passagem de teste
                            print("pass test 5"), sleep(2)

                        person["Tarefas"].append(temp_tar_men_peso["Nome"])
                        person["Peso das Tarefas"] += temp_tar_men_peso["Peso"]
                        assigned_tasks.append(tarefas.index(temp_tar_men_peso))

                temp_tar.clear()
                analyzed_tasks.append(ind_tar)

                # Mostra as tarefas analizadas
                if view_distro:
                    print("Tarefas Analisadas:", analyzed_tasks), sleep(3)

            analyzed_tasks.clear()
            count = 0

tarefas = [{'Name': 'Depurar Código', 'Weight': 5},
           {'Name': 'Participar de Reuniao', 'Weight': 10}]
