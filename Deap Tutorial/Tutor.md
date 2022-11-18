
# Введение в DEAP (python)

Deap - пакет для python, каркас для разработки _эволюционных вычислений_. Установка:

`$ pip install deap`

## Модуль `Creator`

Модуль `Creator` включает в себя стандартные классы DEAP и возможность их **расширять**. Представим, у вас есть простой класс `Employer`:

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

# После набора 3 звездочек на репозитоирии выходит следующая часть!