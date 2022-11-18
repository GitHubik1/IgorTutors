from deap import creator

class Employee:
    salary: int

    def __init__(self, salary: int):
        self.salary