def is_armstrong_number(number):
    """ 
    Used a list(map(...)) on the exercise instead of str(number) to create a sequence as this avoids having to cast
    'd' to an integer when performing the sum, which makes the function faster from ~0.13 to ~0.09, as explained here:
    https://stackoverflow.com/questions/13905936/converting-integer-to-digit-list
    """

    sequence = list(map(int, str(number)))
    digits = len(sequence)

    return sum([d**digits for d in sequence]) == number
