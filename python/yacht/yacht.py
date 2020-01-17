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


# Score categories.
# Change the values as you see fit.
YACHT = 1
ONES = 2
TWOS = 3
THREES = 4
FOURS = 5
FIVES = 6
SIXES = 7
FULL_HOUSE = 8
FOUR_OF_A_KIND = 9
LITTLE_STRAIGHT = 10
BIG_STRAIGHT = 11
CHOICE = 12


def score(dice, category):
    categories = {
        YACHT: lambda dice: 50 if len(set(dice)) == 1 else 0,
        ONES: lambda dice: Numbers(dice, 1),
        TWOS: lambda dice: Numbers(dice, 2),
        THREES: lambda dice: Numbers(dice, 3),
        FOURS: lambda dice: Numbers(dice, 4),
        FIVES: lambda dice: Numbers(dice, 5),
        SIXES: lambda dice: Numbers(dice, 6),
        FULL_HOUSE: Full_House,
        FOUR_OF_A_KIND: Four_of_a_Kind,
        LITTLE_STRAIGHT: lambda dice: Straight(dice, 1, 6),
        BIG_STRAIGHT: lambda dice: Straight(dice, 2, 7),
        CHOICE: lambda dice: sum(dice)
    }.get(category)

    return categories(dice)


def Numbers(values, score_modifier):
    return score_modifier * sum(i == score_modifier for i in values)


def Full_House(dice):
    value = 0
    counted = Counter(dice)

    if len(counted) == 2 and max(counted.values()) == 3 and min(counted.values()) == 2:
        value = sum(dice)

    return value


def Four_of_a_Kind(dice):
    counted = Counter(dice)

    highest_value_key = max(counted, key=counted.get)
    value = counted[highest_value_key]

    return highest_value_key * 4 if value >= 4 else 0


def Straight(dice, min_range, max_range):
    x = set(dice)
    y = set(range(min_range, max_range))

    return 30 if x == y else 0
