
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

Модуль `toolbox` включает в себя стандартные функции и позволяет создавать новые на основе старых. Для примера создадим простую функцию (код в файле Main-2.py):

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

# После набора 5 звездочек на репозитоирии выходит следующая часть!