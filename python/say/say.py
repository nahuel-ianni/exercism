from enum import Enum, unique


@unique
class Number(Enum):
    zero = 0
    one = 1
    two = 2
    three = 3
    four = 4
    five = 5
    six = 6
    seven = 7
    eight = 8
    nine = 9
    ten = 10
    eleven = 11
    twelve = 12
    thirteen = 13


@unique
class Prefix(Enum):
    twenty = 2
    thirty = 3
    forty = 4
    fifty = 5
    sixty = 6
    seventy = 7
    eighty = 8
    ninety = 9


@unique
class Suffix(Enum):
    teen = 0
    hundred = 1
    thousand = 2
    million = 3
    billion = 4


def say(number):
    if number < 0 or number > 1e12:
        raise ValueError("Value out of range")

    elif not number:
        return Number(0).name

    output = []
    digits = [n for n in f"{number:,}".split(",")]

    while digits:
        length = len(digits)
        
        output.append(parse(int(digits[0])))

        if length > 1 and int(digits[0]):
            output.append(Suffix(length).name)

        digits = digits[1:]

    return " ".join(n for n in output if n != Number(0).name)


def parse(number):
    if number < 14:
        output = Number(number).name

    elif number < 20:
        r = number % 10
        output = f"{Number(r).name}{Suffix(0).name}"

    elif number < 100:
        q, r = divmod(number, 10)
        output = f"{Prefix(q).name}-{Number(r).name}" if r else Prefix(q).name
    
    else:
        q, r = divmod(number, 100)
        output = f"{Number(q).name} {Suffix(1).name} {parse(r)}" if r else f"{Number(q).name} {Suffix(1).name}"

    return output