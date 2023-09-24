class Record:
    pass


class Person(Record):
    people = []  # Stores all instances

    def __init__(self, name: str, sector: str, job: str):
        # Validate parameter values
        assert name != '', 'Give it a name'
        assert name != '', 'Cant be sectorless'
        assert job != '', 'Give it a job'

        # Assigne instance attributes
        self.name = name
        self.sector = sector
        self.job = job

        # Add the instance to people
        Person.people.append(self)
        self.id = Person.people.index(self)

    # Print all instance attributes
    def __repr__(self):
        print(f'Id: {self.id}, Name: {self.name}, Sector: {self.sector}, Job: {self.job}')
    
    # Print all instances
    def show_people(self):
        for person in Person.people:
            person.__repr__()


class Task(Record):
    from functions import calc_average, get_weights

    tasks = []  # Stores all instances
    average_weight = calc_average(get_weights(tasks))

    def __init__(self, name: str, weight: int):
        # Validate parameters values
        assert name != '', 'Give it a name'
        assert weight > 0, 'Weight cant be smaller or equal to 0'

        # Assigne instance attributes
        self.name = name
        self.weight = weight

        # Add instance to tasks
        Task.tasks.append(self)
        self.id = Task.tasks.index(self)
    
    # Print all instance attributes
    def __repr__(self):
        print(f'Id: {self.id}, Name: {self.name}, Weight: {self.weight}')
    
    # Print all instances
    def show_tasks(self):
        for task in Task.tasks:
            task.__repr__()


class Distru(Record):
    distributions = []  # Stores all distributions

    def __init__(self, person: Person, tasks: list):
        # Validate instance arguments
        assert person != None, f'The distru needs a person.'
        assert tasks != list, f'The distru tasks should be a list.'

        # Assigne the instance attributes
        self.person = person
        self.tasks = tasks

        # Add the distru to the distributiions list
        Distru.distributions.append(self)
        self.id = Distru.distributions.index(self)


'''
p1 = Person('Lucas', 'IT', 'Scrum Master')
p1.show_people()

t1 = Task('Depurar Codigo', 10)
t1.show_tasks()

t2 = Task('Agendar Sprint', 2)
t1.show_tasks()
'''