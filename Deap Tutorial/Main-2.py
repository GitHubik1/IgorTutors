from deap import base

toolbox = base.Toolbox()

def calc(a, b):
    return a + b

toolbox.register('increment', calc, b=1)