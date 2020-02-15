from secrets import choice
from string import ascii_lowercase as alphabet


class Cipher:
    def __init__(self, key=None):
        self.key = key or "".join(choice(alphabet) for _ in range(100))


    def encode(self, text):
        value = ""

        for i in range(len(text)):
            key = self.key[i % len(self.key)]
            value += alphabet[(alphabet.index(text[i]) + alphabet.index(key)) % len(alphabet)]

        return value


    def decode(self, text):
        value = ""

        for i in range(len(text)):
            key = self.key[i % len(self.key)]
            value += alphabet[(alphabet.index(text[i]) - alphabet.index(key)) % len(alphabet)]
        
        return value
