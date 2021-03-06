"""
This exercise stub and the test suite contain several enumerated constants.

Since Python 2 does not have the enum module, the idiomatic way to write
enumerated constants has traditionally been a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""


from collections import Counter


YACHT = lambda dice: 50 if len(set(dice)) == 1 else 0
ONES = lambda dice: Numbers(dice, 1)
TWOS = lambda dice: Numbers(dice, 2)
THREES = lambda dice: Numbers(dice, 3)
FOURS = lambda dice: Numbers(dice, 4)
FIVES = lambda dice: Numbers(dice, 5)
SIXES = lambda dice: Numbers(dice, 6)
FULL_HOUSE = lambda dice: Full_House(dice)
FOUR_OF_A_KIND = lambda dice: Four_of_a_Kind(dice)
LITTLE_STRAIGHT = lambda dice: Straight(dice, 1, 6)
BIG_STRAIGHT = lambda dice: Straight(dice, 2, 7)
CHOICE = lambda dice: sum(dice)


def score(dice, category):
    return category(dice)


def Numbers(values, score_modifier):
    return values.count(score_modifier) * score_modifier


def Full_House(dice):
    values = set(dice)

    return sum(dice) if len(values) == 2 and dice.count(values.pop()) in {2, 3} else 0


def Four_of_a_Kind(dice):
    counted = Counter(dice)

    highest_value_key = max(counted, key=counted.get)
    value = counted[highest_value_key]

    return highest_value_key * 4 if value >= 4 else 0


def Straight(dice, min_range, max_range):
    x = set(dice)
    y = set(range(min_range, max_range))

    return 30 if x == y else 0
