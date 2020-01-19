import random


class Character:
    def __init__(self):
        self.strength = self.ability()
        self.dexterity = self.ability()
        self.constitution = self.ability()
        self.intelligence = self.ability()
        self.wisdom = self.ability()
        self.charisma = self.ability()

        self.hitpoints = 10 + modifier(self.constitution)
    

    def ability(self):
        dice_values = [1, 2, 3, 4, 5, 6]

        return sum(random.sample(dice_values, 3))


def modifier(coefficient):
    """ The operator // performs the operation and returns the 'floor' value,
        allowing the calculation without having the need to import the math module. """

    return (coefficient - 10) // 2
