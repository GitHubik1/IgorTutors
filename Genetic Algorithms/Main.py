import random

class Individual:
    genotype: list # Класс содержит всего одно поле - генотип

    def __init__(self, genotype): # Конструктор принимает 1 аргумент - генотип
        self.genotype = genotype

    def mutate(self, other, probability=5):
        point = random.randint(1, 3)
        new_gen1 = self.genotype[:point] + other.genotype[point:]
        new_gen2 = other.genotype[:point] + self.genotype[point:]

        for i in range(len(new_gen1)):
            if random.randint(1, 100) <= probability:
                new_gen1[i] = random.randint(0, 2)
        for i in range(len(new_gen2)):
            if random.randint(1, 100) <= probability:
                new_gen2[i] = random.randint(0, 2)

        return (Individual(new_gen1), Individual(new_gen2)) # Возвращаем две новых особи

    @property
    def fitness(self):
        return 1 - sum(self.genotype) / 10

def create_first_generation(size):
    ind = [] # Список со всеми индивидууами
    for _ in range(size):
        ind.append(Individual([random.randint(0, 2) for _ in range(5)])) # создаём список из 5 случайных элементов от 0 до 2
    return ind    

def choice_parents(ind_arr):
        sum_ = 0
        p_arr = [] # Массив вероятностей
        for i in ind_arr:
            p_arr.append(i.fitness + sum_) # Добавляем в массив вероятностей фитнесс особи + сумма всех предыдущих элементов
            sum_ += i.fitness
        ind_number = random.uniform(0.0, sum_) # случайное дробное число
        ind1 = 0 # индекс первого родителя
        for i in range(len(p_arr)):
            if ind_number < p_arr[i]: # Пока p_arr[i] больше случайного числа, ни чего не делаем
                ind1 = i
                break
        ind_number = random.uniform(0.0, sum_)
        ind2 = 0
        for i in range(len(p_arr)):
            if ind_number < p_arr[i]:
                ind2 = i
                break
        return (ind1, ind2)

even_gen = []
odd_gen = []

def generate(size, gen_count):
    for i in range(gen_count):
        if gen_count % 2 == 0:
            for i in range(size // 2):
                ind1, ind2 = choice_parents(even_gen) # Выбираем родителей
                odd_gen[i * 2], odd_gen[i * 2 + 1] = even_gen[ind1].mutate(even_gen[ind2])
        else:
            for i in range(size // 2):
                ind1, ind2 = choice_parents(odd_gen) # Выбираем родителей
                even_gen[i * 2], even_gen[i * 2 + 1] = odd_gen[ind1].mutate(odd_gen[ind2])

if __name__ == '__main__':
    even_gen, odd_gen = create_first_generation(100), [None for i in range(100)]
    generate(100, 200)
    for i in range(100):
        print(f'{i} | {even_gen[i].genotype} - {even_gen[i].fitness}')