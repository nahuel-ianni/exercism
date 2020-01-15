import random
import string


class Robot:
    namesTaken = set()

    def __init__(self):
        self.name = ""
        self.reset()

    
    def reset(self):
        formerName = self.name

        while self.name in Robot.namesTaken or not self.name:
            self.name = self.getRandomName()

        Robot.namesTaken.discard(formerName)        # Discard() doesn't throw an exception if the item is not found, remove() does
        Robot.namesTaken.add(self.name)


    def getRandomName(self):
        characters = self.getRandomLetters()
        number = self.getRandomNumber()        

        return f"{characters}{number}"

    
    def getRandomLetters(self):
        letters = random.choices(string.ascii_uppercase, k=2)

        return "".join(letters)


    def getRandomNumber(self):
        number = random.randint(0, 999)
        number = '{:03}'.format(number)
        
        return number
