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