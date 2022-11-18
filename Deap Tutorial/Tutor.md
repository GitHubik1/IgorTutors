
# Введение в DEAP (python)

Deap - пакет для python, каркас для разработки _эволюционных вычислений_. Установка:

`$ pip install deap`

## Модуль `Creator`

Модуль `Creator` включает в себя стандартные классы DEAP и возможность их **расширять**. Представим, у вас есть простой класс `Employer` (Код в файле Main-1.py):

```python
from deap import creator

class Employee:
    salary: int

    def __init__(self, salary: int):
        self.salary
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

Класс `toolbox` позволяет создавать новые функциии на основе старых. Для примера создадим простую функцию (код в файле Main-2.py):

```python
from deap import base

toolbox = base.Toolbox()

def calc(a, b):
    return a + b
```

Теперь спомощью `toolbox.register` создадим новую на основе `calc`, но парамметр b будет всегда равен 1:

```python
toolbox.register('increment', calc, b=1)
```

Эта запись эквивалента следующеей:

```python
def increment(a):
    return calc(a, 1)
```

## модуль `tools`

Модуль `tools` включает в себя стандартные функции:

- `selRoulette()` - отбор по правилу рулетки;
- `selStochasticUniversalSampling()` - стохастическая универсальная вы-борка;
- `selTournament()` - турнирный отбор.
- `cxOnePoint()` - одноточечное скрещивание;
- `cxUniform()` - равномерное скрещивание;
- `cxOrdered()` - упорядоченное скрещивание (OX1);
- `cxPartialyMatched()` - скрещивание с частичным сопоставлением.
- `mutFlipBit()` - мутация инвертированием бита;
- `mutGaussian()` - нормально распределенная мутация.

# После набора 8-ми звездочек и 3-х подписок на репозитоирии выходит следующая часть!!!