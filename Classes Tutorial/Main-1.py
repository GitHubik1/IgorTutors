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

print('', human.gender, human.height, '\n', human2.gender, human2.height) # Экземпляры класса независимы друг от друга