
# Введение в DEAP (python)

> :warning: Часть текста, кода и примеров взяты из книги **"Генетические алгоритмы на Python" (Эйял Вирсански)**

Deap - пакет для python, каркас для разработки _эволюционных вычислений_. Установка:

`$ pip install deap`

## Модуль `Creator`

Модуль `Creator` включает в себя возможность **расширять** классы. Представим, у вас есть простой класс `Employer` (Код в файле Main-1.py):

```python
from deap import creator

class Employee:
    salary: int

    def __init__(self, salary: int):
        self.salary = salary
```

С помощью функции `creator.create` мы можем его невероятно просто расширить (добавить туда поля):

```python
creator.create('Developer', Employee, position='Worker', programmingLanguages=set)
```

Эта запись эквивалентна следующей:

```python
class Developer(Employee):
    position = 'Worker'
    programmingLanguages: set
```

## Класс `toolbox`

Класс `toolbox` позволяет создавать новые функции на основе старых. Для примера создадим простую функцию (код в файле Main-2.py):

```python
from deap import base

toolbox = base.Toolbox()

def calc(a, b):
    return a + b
```

Теперь с помощью `toolbox.register` создадим новую на основе `calc`, но параметр b будет всегда равен 1:

```python
toolbox.register('increment', calc, b=1)
```

Эта запись эквивалента следующей:

```python
def increment(a):
    return calc(a, 1)
```

## Пишем генетический алгоритм на DEAP

Для примера, напишем OneMax.

### Определение стратегии приспособления

Стратегия приспособления - определяет что должно получится в итоге. Например, фитнес должен стать максимальным. В библиотеке DEAP встроен стандартный класс фитнеса, но его нельзя использовать. Зато можно расширить:

```python
from deap import creator
from deap import base

creator.create('FitnessMax', base.Fitness, weights=(1.0, )) # Фитнес возрастать
creator.create('FitnessMin', base.Fitness, weights=(-1.0, )) # Фитнес уменьшатся
```

### Создание индивидуума

Каждый класс индивидуума должен содержать список хромосом, т. е. индивидуум будет расширением класса `list`. Туда добавляем дополнительный атрибут - `fitness`, который будет являтся экземпляром класса `FitnessMax`:

```python
...

creator.create('Individual', list, fitness=creator.FitnessMax)
```

### Создаём константы и вспомогательные функции

```python
from deap import creator
from deap import base
import random

GENOTYPE_LEN = 100 # Длинна генотипа
POPULATION_SIZE = 50 # Размер популяции
MAX_GENERATIONS = 200 # Максимальное количество поколений
P_MUTATION = 0.05 # Вероятность мутации (от 0 до 1)

toolbox = base.Toolbox()
toolbox.register('zero_or_one', random.randint, 0, 1) # Случайное целое число от 0 до 1
```

### Функция приспособленности

Просто вернём сумму генотипа:

```python
def indFitness(individual):
    return sum(individual)

toolbox.register('evaluate', indFitness) # принятое в DEAP соглашение. evaluate - фитнес
```

# После набора 8-ми звездочек и 3-х подписок на репозитоирии выходит следующая часть!!!
