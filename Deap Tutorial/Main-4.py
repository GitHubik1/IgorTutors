from deap import creator
from deap import base
from deap import tools
import random

GENOTYPE_LEN = 100 # Длинна генотипа
POPULATION_SIZE = 50 # Размер популяции
MAX_GENERATIONS = 200 # Максимальное количество поколений
P_MUTATION = 0.1 # Вероятность мутации (от 0 до 1)

toolbox = base.Toolbox()
toolbox.register('zero_or_one', random.randint, 0, 1) # Случайное целое число от 0 до 1

creator.create('FitnessMax', base.Fitness, weights=(1.0, )) 
creator.create('Individual', list, fitness=creator.FitnessMax)

def indFitness(individual):
    return sum(individual)

toolbox.register('evaluate', indFitness) # принятое в DEAP соглашение. evaluate - фитнес

toolbox.register('chooce_parents', tools.selTournament, tournsize=3) # Выбор родителей методом турнира
toolbox.register('crosssover', tools.cxOnePoint) # Кроссинговер
toolbox.register('mutate', tools.mutFlipBit, indpb=1.0/GENOTYPE_LEN) # Мутация методом инвентирования бита
toolbox.register('population_creator', tools.initRepeat(list, tools.initRepeat(creator.Individual, toolbox.zero_or_one, GENOTYPE_LEN), POPULATION_SIZE))

population = toolbox.population_creator() # Первое поколение
generations = 0 # Количество поколений
maxFitnessValues = [0, ] # Сохраним максимальные значения Фитнесса

while maxFitnessValues[-1] < 100:
    fitnessValues = list(map(toolbox.evaluate, population)) # Вычисление значений приспособленности
    maxFitnessValues.append(max(fitnessValues))

    offspring = toolbox.chooce_parents(population, POPULATION_SIZE) # Выбираем родителей
    offspring = list(map(toolbox.clone, offspring)) # Клонируем

    for child1, child2 in zip(offspring[::2], offspring[1::2]):
        toolbox.crosssover(child1, child2)

    for mutant in offspring:
        if random.random() < P_MUTATION:
            toolbox.mutate(mutant)
    
    generations += 1
    population[:] = offspring