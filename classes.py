class Person:
    people = []

    def __init__(self, name: str, sector: str, job: str):
        
        assert name != '', 'Give it a name'
        assert name != '', 'Cant be sectorless'
        assert job != '', 'Give it a job'

        self.name = name
        self.sector = sector
        self.job = job

        Person.people.append(self)


class Task:
    tasks = []

    def __init__(self, name: str, weight: int):
        
        assert name != '', 'Give it a name'
        assert weight > 0, 'Weight cant be smaller or equal to 0'

        self.name = name
        self.weight = weight

        Task.tasks.append(self)

    def __repr__(self) -> str:
        print(f'Name: {self.name}, Weight: {self.weight}')

    @classmethod
    def show_tasks(self):
        for task in Task.tasks:
            task.__repr__()
