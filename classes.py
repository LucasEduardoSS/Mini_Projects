from statistics import mean, pvariance, pstdev


class Record:
    pass


class Person(Record):
    people = []  # Stores all instances

    def __init__(self, name: str, sector: str, job: str):
        # Validate parameter values
        assert name != '', 'Give it a name'
        assert sector != '', 'Cant be sectorless'
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
    
    tasks = []  # Stores all instances
    weight_average = 0
    weight_variance = 0
    weight_deviation = 0

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

        # Update class attributes
        Task.weight_average = mean(self.get_weights())
        Task.weight_variance = pvariance(self.get_weights(), Task.weight_average)
        Task.weight_deviation = pstdev(self.get_weights())
        
    # Print all instance attributes
    def __repr__(self):
        print(f'Id: {self.id}, Name: {self.name}, Weight: {self.weight}')
    
    # Print all instances
    def show_tasks(self):
        for task in Task.tasks:
            task.__repr__()

    # Get all weights
    def get_weights(self):
        return [task.weight for task in Task.tasks]
        

class Distru(Record):
    distributions = []  # Stores all distributions

    def __init__(self, person: Person, tasks: list):
        # Validate instance arguments
        assert person != None, f'The distru needs a person.'
        assert tasks != list, f'The distru tasks should be a list.'

        # Assigne the instance attributes
        self.person = person
        self.tasks = tasks
        self.total_weight = sum([task.weight for task in self.tasks])

        # Add the distru to the distributiions list
        Distru.distributions.append(self)
        self.id = Distru.distributions.index(self)
    
    # Print all instance attributes
    def __repr__(self):
        print(f'Id: {self.id}, Person: {self.person.name}, Tasks: {[task.name for task in self.tasks]}, TTW: {self.total_weight}')
    
    # Print all instances
    def show_distrus(self):
        for d in Distru.distributions:
            d.__repr__()


'''p1 = Person('Lucas', 'IT', 'Scrum Master')
# p1.show_people()

t1 = Task('Depurar Codigo', 8)
# t1.show_tasks()

t2 = Task('Agendar Sprint', 2)
# t2.show_tasks()

t3 = Task('Avaliar um commit', 6)

print(t3.weight_average)
print(t3.weight_variance)
print(t3.weight_deviation)
'''