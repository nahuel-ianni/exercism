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
    2 : "twenty",
    3 : "thirty",
    4 : "forty",
    5 : "fifty",
    6 : "sixty",
    7 : "seventy",
    8 : "eighty",
    9 : "ninety",
}


def say(number):
    output = ""

    if number < 0 or number > 999999999999:
        raise ValueError("Value out of range")

    elif number < 14:
        output = Numbers(number).name
    
    elif number < 20:
        n = number % 10
        output = f"{Numbers(n).name}teen"
    
    elif number < 100:
        q = number // 10
        r = number % 10
        
        output = f"{prefix[q]}-{Numbers(r).name}" if r else prefix[q]
    
    return output
