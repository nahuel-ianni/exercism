def convert(number):
    value = get_raindrop_sound(number)

    return value if value else str(number)


def get_raindrop_sound(number):
    returnValue = ""

    if number % 3 == 0:
        returnValue += "Pling"

    if number % 5 == 0:
        returnValue += "Plang"

    if number % 7 == 0:
        returnValue += "Plong"

    return returnValue