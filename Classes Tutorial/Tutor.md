# Введение в классы (python)

## Что такое класс

Класс - _схема_ для создания объектов. К примеру, мы можем создать класс "Человек" и создать его _экземпляр_:

```python
class Human: # С помощью ключевого слова class, создаём класс Human
    # Поля класса
    gender: str # Поле "пол" типа строка
    height: int # Поле "рост" типа целое число

human = Human() # Создаём экземпляр класса Human
human.gender = 'male'
human.height = 180 # Присваиваем полям какие-то значения

human2 = Human() # Создаём другой экземпляр класса Human
human2.gender = 'female'
human2.height = 160

print(human.gender, human.height, '\n' human2.gender, human2.height) # Экземпляры класса независимы друг от друга
```

Вывод:

```python
 male 180 
 female 160
```

## Методы класса

Метод класса - обычная функция встроенная в класс. Обычно их используют для работы с ними:

```python
class Human:
    gender: str
    height: int

    def set_gender(self, gender):
        self.gender = gender

    def set_height(self, height):
        self.height = height

    def print_self(self):
        print(self.gender, self.height)

human = Human()
human.set_gender('male')
human.set_height(180)
human.print_self()
```

Вывод:

```python
male 180
```

## Указатель self

Когда мы уже создали экземпляр класса, функциям иногда нужно "работать с собой": изменять переменные данного экземпляра. Что бы мы понимали с чем работаем, как один из аргументов передаём `self`. Теперь, что бы изменять поля класса, мы должны обращаться к ним через `self`:

```python
class Example:
    
    ...

    def example(self):
        self.field = 'spam'

    ...
```

## Конструкторы

В конструкторе описывается всё, что происходит при создании объекта:

```python
class Spam:
    spam: str
    text: str

    def __init__(self, text):
        self.spam = 'spam'
        self.text = text

        print('Object created')

    def print_text(self):
        print(self.text)

something = Spam('To be, or not to be, that is the question')
something.print_text()
```

Вывод:

```python
Object created
To be, or not to be, that is the question
```