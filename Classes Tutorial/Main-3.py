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