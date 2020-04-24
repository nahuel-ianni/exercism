from enum import Enum


class Numbers(Enum):
    zero     = 0
    one      = 1
    two      = 2
    three    = 3
    four     = 4
    five     = 5
    six      = 6
    seven    = 7
    eight    = 8
    nine     = 9
    ten      = 10
    eleven   = 11
    twelve   = 12
    thirteen = 13

prefix = {
    20       : "twenty",
    30       : "thirty",
    40       : "forty",
    50       : "fifty",
    60       : "sixty",
    70       : "seventy",
    80       : "eighty",
    90       : "ninety",
}


def say(number):
    output = ""

    if number < 0 or number > 999999999999:
        raise ValueError("Value out of range")

    elif number < 14:
        output = Numbers(number).name
    
    elif number < 20:
        number %= 10
        output = f"{Numbers(number).name}teen"
    
    return output
