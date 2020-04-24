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

class Prefix(Enum):
    twenty  = 2
    thirty  = 3
    forty   = 4
    fifty   = 5
    sixty   = 6
    seventy = 7
    eighty  = 8
    ninety  = 9

# class Suffix(Enum):
#     hundred  = 3
#     thousand = 4
#     million  = 7
#     billion  = 13


def say(number):
    output = ""

    if number < 0 or number > 999999999999:
        raise ValueError("Value out of range")

    elif number < 14:
        output = Numbers(number).name
    
    elif number < 20:
        r = number % 10
        output = f"{Numbers(r).name}teen"
    
    elif number < 100:
        q, r = division(number, 10)        
        output = f"{Prefix(q).name}-{Numbers(r).name}" if r else Prefix(q).name
    
    elif number < 1000:
        q, r = division(number, 100)
        output = f"{Numbers(q).name} hundred {say(r)}" if r else f"{Numbers(q).name} hundred"
    
    # else:
    #     digits = "{number:,}".split(",")


    
    return output


def division(dividend, divisor):
    return (dividend // divisor, dividend % divisor)
